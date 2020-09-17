# 제어문과 조합하여 data(list, set, dict) 만들기 - composition

new_squares = [n**2 for n in range(10)]
print(new_squares, '\n')

items = 'rock', 'scissors', 'paper'

results = []
for a in items:  # first statement
    for b in items:  # second statement
        if a != b:  # third statement
            results.append((a, b))  # action
print(results)

new_results = [(a, b) for a in items for b in items if a != b]  # append 생략
print(new_results, '\n')

a = set()
for x in 'abracadabra':
    if x not in 'abc':
        a.add(x)
print(a)

new_a = {x for x in 'abracadabra' if x not in 'abc'}  # add 생략
print(new_a, '\n')

squares = {}
for x in (2, 4, 6):
    squares[x] = x**2
print(squares)

brand_new_squares = {x: x**2 for x in (2, 4, 6)}
