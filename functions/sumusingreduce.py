from functools import reduce

lst = [5, 10, 15, 20]
result = reduce(lambda x, y: x+y, lst)
# ? reduce(function, sequence)
print(result)
