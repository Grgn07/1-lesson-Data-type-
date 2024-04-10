
# 1. Создать список квадратов чисел от a до b. a и b вводятся с клавиатуры.

a, b = int(input()), int(input())
a_gen = [i ** 2 for i in range(a, b + 1)]
print(a_gen)

# 2. Создать список всех четных чисел от a до b. a и b вводятся с клавиатуры.

a = input()
b = input()
a_gen = [i for i in range(a, b) if i % 2 == 0]
print(a_gen)

# 3. Создать список строк, содержащих только гласные буквы из  строки array. array вводится с клавиатуры.
array = str(input())
array_vowels = [x for x in array if x in "eyuioa"]
print(array_vowels)

# 4. Создать список всех чисел от 1 до 100, которые делятся и на 3, и на 5.
a, b = 1, 101
i_li = [i for i in range(a, b) if i % 3 == 0 and i % 5 == 0]
print(i_li)


# 5. Создать список состоящий из других списков, следующего вида:[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s_sp = [[i for i in range(1,4)], [i for i in range(4,7)], [i for i in range(7,10)]]
print(s_sp)


# 6.Создать список словарей, содержащий информацию о студентах (имя, возраст, список оценок).
# Оставьте только тех студентов в списке, средний балл которых выше 7.0

STUDENS = [{"Name": "Walter", "age": 53, "marks": [9, 9, 9, 9]},
           {"Name": "Jessi", "age": 23, "marks": [9, 5, 6, 5]},
           {"Name": "John", "age": 42, "marks": [4, 6, 7, 5]},
           {"Name": "Alex", "age": 18, "marks": [9, 6, 8, 7]}]
student_good = []
for student in STUDENS:
    if sum(student['marks']) / len(student['marks']) > 7:
        student_good.append(student)
print(student_good)


# 1. Напишите программу, которая принимает на вход символ (букву английского алфавита)
# и использует оператор match/case для определения, является ли символ гласной или согласной,
# и выводит соответствующее сообщение.

letter = input()
match letter:
    case 'a'|'e'|'y'|'u'|'i'|'o':
        print("vowel")
    case _:
        print("not vowel")


# 2. Напишите программу, которая принимает на вход день недели (название на английском)
# и использует оператор match/case для вывода сообщения о том, является ли этот день рабочим или выходным.

day = "Monday"
match day:
    case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
        print("Рабочий")
    case "Saturday"|"Sunday":
        print("Выходной")
