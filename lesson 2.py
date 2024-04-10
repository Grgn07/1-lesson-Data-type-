# 1. Вы вводите с клавиатуры последовательность чисел, разделённых запятой.
# Составьте список и кортеж с этими числами.

array = input()
array_lst = array.split(',')
array_tpl = tuple(array_lst)
print(array_lst, array_tpl)


# 2. Написать программу, которая может принимать любое неотрицательное целое число
# в качестве аргумента и возвращать новое максимально возможное значение,
# составленное из цифр этого же числа. По сути, просто переставить цифры,
# чтобы создать максимально возможное число.

number = int(input())
num_lst = list(str(number))
num_lst.sort(reverse=True)
print(int("".join(num_lst)))

# 3.  С клавиатуры вводится натуральное число. Найти его наибольшую цифру.
# Например, введено число 764580. Наибольшая цифра в нем 8.

array = int(input())
array_lstr = list(str(array))
print(max(array_lstr))



# 4*. Напишите программу которая настроит отображение комментария к отметке
# 'мне нравится' в условном посте. Список имен передается в кач-ве аргумента.
# Например:
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

username_list = ["Mark", "Alex"]
if len(username_list) == 0:
    print("No one likes this")
elif len(username_list) == 1:
    print(f"{username_list[0]}likes this")
elif len(username_list) == 2:
    print(f"{username_list[0]} and {username_list[1]}likes this")
elif len(username_list) == 3:
    print(f"{username_list[0]}, {username_list[1]} and {username_list[2]} likes this")
else:
    print(f"{username_list[0]}, {username_list[1]} and {len(username_list)-2} likes this")

# 1.Даны списки:
# Нужно вернуть список, который состоит из элементов, общих  для этих двух списков.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



# 2.Пользователь вводит слово с клавиатуры, необходимо
# проверить, является ли это слово изограммой(то есть не содержит одинаковых символов)

word = input()
if len(word.lower()) == len(set(word.lower())):
    print("Не изограмма")
else:
    print("Изограмма")