import re
str = "Take 1 up 1-3-2019 One 23 idea.One idea 45 at a Time 12-11-2020 and Once"
result = re.search(r'O\w', str)
# ? r'' : regular expression임을 선언
print(result)

result = re.findall(r'O\w\w', str)
print(result)

result = re.match(r'T\w\w', str)
print(result.group())

result = re.sub(r'One', 'Two', str)
print(result)

result = re.findall(r'O\w*', str)
print(result)

result = re.findall(r'O\w?', str)
print(result)

result = re.findall(r'O\w{1,2}', str)
print(result)

result = re.findall(r'O\w{1,}', str)
print(result)

result = re.split(r'\d+', str)
print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)

result = re.search(r'^T\w*', str)
print(result.group())

# * \d : any digit character
# * \D : any non-digit character
# * \s : white space
# * \S : non-white space
# * \w : any alpha numeric character
# * \W : any non- alpha numeric character
# * \b : space around words
# * \A : only matched at the beginning of the string
# * \Z : only matches at the end of the string

# ? quantifiers
# * \d+ : one or more digit
# * \d* : zero or more repetitions of the preceding regular expression
# * \d? : zero or one repetitions of the preceding regular expression
# * {m} : exactly m occurence
# * {m,n} : min m, max n occurence, default : m=0, n=infinite

# ? special characters

# * \ : escape, when you use special character such as '\'
# * . : any character
# * ^x : starts with x at the beginning of the string
# * $x : ends with x right at the end of the string
# * [ab] : a or b
# * [a-d] : any character in range from a to b
# * [^a-d] : any character not in range from a to b
# * [^abcd] : any character not in a,b,c,d
# * ()
