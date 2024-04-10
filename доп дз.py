def num_quatr (num: list[int]) -> list[int]:
    num_q = [n ** 2 for n in num]
    return num_q
print(num_quatr([2, 3, 4, 5, 6]))

def sp_strok (line:list[str]) -> list[str]:
 res = []
 for el in line:
    if len(el) >= 5:
        res.append(el)
 return res
print(sp_strok(['dfgh', 'fhyjfh', 'rty', 'fgvhbj']))


def even (num: list[int]) -> list[int]:
    num_ev = [n for n in num if n % 2 == 0]
    return num_ev
print(even([1, 2, 3, 4, 5, 6]))


def even_quatr (num: list[int]) -> list[int]:
    num_sum_quatr = [n ** 2 for n in num if n % 2 == 0]
    return sum(num_sum_quatr)
print(even_quatr([1, 2, 3, 4, 5, 6, 7]))



def el (words:list[str], substring: str) -> list[str]:
    result = []
    for word in words:
        if word.startswith(substring):
            result.append(word)
    return result
print(el(['asd', 'hjkjkhg', 'ajhgh'], 'a'))


def num (numbers: list[int]) -> list[int]:
    numbers_bi = [n for n in numbers if 20 > n > 10]
    return numbers_bi
print(num([5, 9, 15, 17, 12, 27]))

def stroka_li (line: list[str]) -> list[str]:
 result = []
 for word in line:
    if 'e' in word:
        result.append(word)
 return result
print(stroka_li(['ghj', 'fgvheg', 'dfge', 'edfg']))




def num (numbers: list[int]) -> bool:
    for i in numbers:
        if i < 0:
         return False
    return True
print(num([4, 5, 8]))



def list_num (array: list[str]) -> list[str]:
    result = []
    for i in array:
        if i.isdigit():
            result.append(i)
            return result
print(list_num(['gvhbj', '52', 'ghj4']))






