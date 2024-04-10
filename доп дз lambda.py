# def spin_words(centence):
#   res = []
#   for word in centence.split():
#      if len(word) >= 5:
#          res.append(word[::-1])
#      else:
#          res.append(word)
#   return " ".join(res)
#   print(spin_words("Hhfv hjdfjj poipoo"))




a = [1, 2, 3, 4, 5, 6, 7, 8]
num_even = list(filter(lambda num: num % 2 == 0, a))
print(num_even)

from functools import reduce
print(reduce(lambda n, i: n + i, [8, 7]))

array = ["ty", "dfgh", "uyrl", "f"]
array_fl = list(filter(lambda el: len(el) > 3, array))
print(array_fl)

numbers = [2, 5, 7, 6, 3]
numbers_qut = list(map(lambda num: num ** 2, numbers))
print(numbers_qut)

array = ["ahydi", "jhkn", "auhdjn", "hjknac", "Aghj"]
array_a = list(filter(lambda word: word.lower().startswith("a"), array))
print(array_a)

a = [4, 8, 22, 10, 17, 29]
num_even = list(filter(lambda num: num > 10, a))
print(num_even)


a = ["fghj", "SLPCV", "jhgcv", "TGHJ"]
a_reg = list(filter(lambda array: array.isupper(), a))
print(a_reg)


a = [4, 9, 15, 22, 34, 42]
num_even = list(filter(lambda num: num % 3 == 0, a))
print(num_even)



a = [2, 8, 5, 7, 4, 10, 15]
num_even = list(filter(lambda num: num in range(5, 11), a))
print(num_even)



array = ["ahydi", "jhkno", "auhdjn", "hjknaco", "Aghj"]
array_o = list(filter(lambda word: word.endswith("o"), array))
print(array_o)