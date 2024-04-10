

# задача 1 из основного дз
def logger(func):
    def wrapper(*args):
        print(f"Тип данных:{isinstance(func, int)}")
        print(f"Аннотации:{func.__annotations__}")
        func(*args)
    return wrapper

@logger
def count(num: int) -> int:
    return print(num ** 2)
count(5)




# задача 1 из доп дз
def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper
@uppercase
def gen_str():
    return "hello"
print(gen_str())




# задача 2 из доп дз
def exception(func):
    def wrapper(*args):
        try:
            res = func(10, 0)
            return (res)
        except ZeroDivisionError:
         return ValueError(f"Not correct divider")
    return wrapper
@exception
def two(x, y):
    return x / y
print(two(10, 5))




# задача 3 из доп дз
from time import sleep
def benchmark(func):
    def wrapper():
        result = func()
        sleep(5)
        return result
    return wrapper
@benchmark
def three():
    return "Hello"
print(three())




# задача 4 из доп дз
from datetime import datetime
def benchmark(func):
    def wrapper(num):
        start = datetime.now()
        func(num)
        finish = datetime.now()
        print((f"Время начало выполнения {func}"), start)
        print((f"Время окончания выполнения {func}"), finish)
    return wrapper

@benchmark
def count(num):
    return print(num ** 2)

count(114)






