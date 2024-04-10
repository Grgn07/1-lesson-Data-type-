square = (i ** 2 for i in range(1, 10))
for k in square:
    print(k, end=',')

even = (n for n in range(1, 20) if n % 2 == 0)
for k in even:
    print(k, end=',')



def fibonacci(n):
   f_1, f_2 = 1, 1
   for _ in range(n):
        yield f_1
        f_1, f_2 = f_2, f_1 + f_2

a = list(fibonacci(10))
for i in a:
    print(i, end=',')








