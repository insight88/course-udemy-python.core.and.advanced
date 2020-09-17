color = set()
color.add("red")
color.add("blue")
color.add("green")
color.add("white")

print(color)  # set sorts elements randomly
print('red' in color)
print('red' not in color, '\n')

color.remove('red')  # (elem), remove existing element
print(color)
color.discard('black')  # (elem), remove if elements exists, else continue
print(color)
color.discard('blue')
print(color, '\n')

color.pop()  # return and remove arbitrary element
print(color)
color.clear()
print(color, '\n')

A = set('lsldkfh')
B = set('lwoihsh')

print(A)
print(B, '\n')
print(A - B)
print(A | B)  # A,B의 합집합
print(A & B)  # 교집합
print(A ^ B, '\n')  # A,B의 여집합
print((A ^ B) | (A & B))
