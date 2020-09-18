programmers = {'python': 14, 'c': 20, 'ruby': 11}
print(programmers)
print(programmers['python'])
programmers['python'] = 10
print(programmers['python'], '\n')

print(programmers.keys())  # view on dictionary's keys
print(list(programmers.keys()), '\n')  # make new list with dictionary keys
print(programmers.values())  # view on dictionary's values
print(list(programmers.values()), '\n')

del programmers['ruby']
print(programmers)
programmers.clear()
print(programmers, '\n')

programmers_list = [('python', 14), ('c', 20), ('ruby', 11)]
print(programmers_list)
programmers_dict = dict(programmers_list)  # make dict with key-value list
print(programmers_dict, '\n')

nums = [4, 1, 2, 5, 7, 3]
print(nums)
sort_nums = sorted(nums)  # return a new sorted list
print(sort_nums)
reverse_sort_nums = sorted(nums, reverse=True)
print(reverse_sort_nums)
print(nums)
