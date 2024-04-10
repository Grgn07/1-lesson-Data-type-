# # 1. Напишите программу, которая выводит на экран все числа от 1 до 10.
number = int(input())
start = 1
result = []
while start <= number:
    result.append(start)
    start += 1
print(result)
#
# # 2. Напишите программу, которая запрашивает у пользователя число n,
# # а затем выводит на экран все числа от 1 до n.
#
n = int(input())
start = 1
result = []
while start <= n:
    result.append(start)
    start += 1
print(result)
# # 3. Напишите программу, которая выводит на экран все четные числа от 2 до 20.
#
for num in range(2, 21):
    if num % 2 == 0:
     print(num, end=",")
# # 4. Напишите программу, которая запрашивает у пользователя число n,
# # а затем выводит на экран все четные числа от 2 до n.
start = 2
res = 20
while start <= res:
    if start % 2 == 0:
        print(start, end=",")
    start += 1
#
# # 5. Напишите программу, которая выводит на экран таблицу умножения от 1 до 10.
#
n = 10
k = 1
while k <= 10:
    print(f"{n} * {k} = {n * k}")
    k += 1
#
# # 6. Напишите программу, которая запрашивает у пользователя число n,
# # а затем выводит на экран таблицу умножения от 1 до n.
#
n = int(input())
k = 1
while k <= 10:
    print(f"{n} * {k} = {n * k}")
    k += 1
#
# # 7. Напишите программу, которая запрашивает у пользователя число n,
# # а затем выводит на экран все числа от n до 1 в обратном порядке.
#
#
# # 8. Напишите программу, которая выводит на экран все буквы английского алфавита.
#
import string
print(string.ascii_letters)
# # 9. Напишите программу, которая запрашивает у пользователя слово,
# # а затем выводит на экран все буквы этого слова в обратном порядке.
#
word = input()
word_reversed = word[::-1]
for letter in word_reversed:
    print(letter, end="")
# 10. Напишите программу, которая запрашивает у пользователя слово,
# а затем выводит на экран все буквы этого слова, кроме буквы "а".

word = input("Word:")   #вводить на английском
for letter in word:
    if letter != "a":
     print(letter, end="")

# 1. Пользователь вводит строку. Посчитайте количество гласных букв в этой строке.
vowels = "euioay"
array = input()
vowels_counter = 0
for symbol in array.lower():
    if symbol in vowels:
        vowels_counter += 1
print(vowels_counter)


# 2. Пользователь вводит строку, посчитайте количество слов с буквой “a”  независимо от регистра.

array = input()
word_lst = array.split()
word_counter = 0
for word in word_lst:
    if "a" in word or "A" in word:
        word_lst += 1
print(word_counter)

# 3. Напишите программу, которая принимает два числа и считает наименьшее общее кратное для этих чисел.

from math import lcm #наименьшее общее кратное
print(lcm(12, 8))

from math import gcd #наименьший общий делитель
print(gcd(12, 8))

# 4*. Написать программу на определение, является ли введенное число простым.
# Число должно вводится с клавиатуры любое количество раз без запуска программы заново,
# завершение программы произойдет только при вводе пользователем слова "exit" вместо числа.



# 5*. Написать программу, принимающую строку вида: "The sunset sets at twelve o' clock."
# и возвращающую строку: "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
# где каждое число это порядковый номер буквы в алфавите. Например при передаче строки: "abc" должно
# вернуться "1 2 3". *Без учета регистра.

punctuation =" !#$%&'()*+,-./:;<=>?@[]^_`{|}~\\"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
array = "abc dex"
result = []
for letter in array.lower():
    if letter not in punctuation:
        result.append(str(alphabet.index(letter)+1))
    else:
        continue
print("".join(result))