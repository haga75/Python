# https://towardsdatascience.com/top-3-python-functions-you-dont-know-about-probably-978f4be1e6d

def more_than_15(x):
    return x > 15

data = [3, 17, 32, 12, 54, 3, 2, 1]

print(list(filter(more_than_15, data)))
