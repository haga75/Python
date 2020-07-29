# https://docs.python.org/3/tutorial/introduction.html

a, b = 0, 1

while a < 10000000000000:
    print(a)
    a, b = b, a+b
