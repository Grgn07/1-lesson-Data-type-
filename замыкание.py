# Создайте и вызовите пользовательскую функцию-матрешку my_func_1,
# состоящую из четырех вложенных друг в друга определений аналогичных функций.
# Каждая функция должна выводить сообщение в формате 'In my_func_{номер функции}.',
# а также содержать определение и вызов следующей вложенной функции
# (в последней функции эта часть будет отсутствовать)

def foon(**arguments):
    for elem in arguments.items():
        print(elem[0], '->', elem[1])
foon(a = 7, b = 42.89, c = "hello", d = [])







