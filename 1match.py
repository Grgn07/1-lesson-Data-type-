num = int(input())
res = 1
while num > 0:
    res *= num
    num -= 1
print(res)


date = "10-09-2024"
date_obj = date.split('-')
format_date = '.'.join(date_obj[::-1])
print(format_date)


array = input()
length_array = len(array)
middle_symbol = length_array // 2
if length_array % 2 == 0:
    print(array[middle_symbol - 1:middle_symbol + 1])
else:
    print(array[middle_symbol])


array = 'bhg kmjy bhg lkj'
word_list = array.split()
array_count = max([array.count for  x in set(array.split())])
print(array_count)
