scores = [88, 90, 79, 50, 99, 100]
print(scores)

scores.append(92)  # (object)
print(scores)

scores.remove(50)  # (value
print(scores)

scores.insert(4, 77)  # (index, object)
print(scores)

score = scores.count(99)  # (value)
print(score)

scores.pop(2)  # (index)
print(scores)

scores.sort()  # default : ascending
print(scores)

scores.sort(reverse=True)  # option : descending
print(scores)

scores.clear()  # remove all items
print(scores)

scores = [55, 66, 77, 88, 99]
print(scores)

scores.extend([44, 33])  # append elements from the iterable object
print(scores)

sliced_scores = scores[1:4]
print(scores)
