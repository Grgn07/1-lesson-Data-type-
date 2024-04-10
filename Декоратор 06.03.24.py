# from datetime import datetime
# from time import sleep
#
# def benchmark(func):
#     def wrapper():
#         start = datetime.now()
#         a = func()
#         finish = datetime.now() - start
#         if finish.seconds > 3:
#             return "Overload"
#         else:
#             return a
#     return wrapper
#
# @benchmark
# def operation_1():
#     sleep(4)
#     return "Ok 200"
#
# @benchmark
# def operation_2():
#     sleep(1)
#     return "Ok 201"
#
# print(operation_1())
# print(operation_2())






