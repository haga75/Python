# https://towardsdatascience.com/top-3-python-functions-you-dont-know-about-probably-978f4be1e6d

from functools import reduce

def add_nums(a, b):
    return a + b

data = [5, 10, 12, 18, 25]

print(reduce(add_nums, data))
