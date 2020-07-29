# https://towardsdatascience.com/top-3-python-functions-you-dont-know-about-probably-978f4be1e6d

def num_func(x):
    return x**2 / 2

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(num_func, data)))
