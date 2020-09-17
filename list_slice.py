scores = [88, 90, 79, 50, 99, 100]
print(scores)

sliced_scores = scores[1:4]  # [start, end+!], return new sliced string
print(sliced_scores, '\n')

print(scores[2:4])
print(scores[:4])  # default start index = 0
print(scores[2:])  # default end indext = end
print(scores[:], '\n')

new_scores = scores  # ! same reference lists
new_scores.append(81)
print(new_scores)
print(scores, '\n')

next_scores = scores[:]  # ! different reference with same values
next_scores.append(44)
print(next_scores)
print(scores, '\n')

brand_new_scores = scores.copy()  # same as scores[:]
brand_new_scores.append(68)
print(brand_new_scores)
print(scores, '\n')
