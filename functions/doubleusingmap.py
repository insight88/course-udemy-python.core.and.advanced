lst = [2, 3, 4, 5]

result = list(map(lambda n: n*2, lst))
# ? map, filter는 map object, filter object의 address value를 return, list를 붙여줘야 value에 접근 가능
print(result)
print(lst)
