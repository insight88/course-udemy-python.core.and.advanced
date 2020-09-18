s = "  You are awesome  "
print(s)

s1 = """You are
the creator
of your destiny"""
# ? multiple line exression with line break
print(s1)

print(s[2])

print(s*3)

print(len(s1))
print(len(s))

print(s[0:5])
print(s[0:])
print(s[:8])
print(s[-3:-1])
# ? minus sign : reverse order

print(s[0:9:2])
# ? s[start:end:step] slicing
print(s[15::-1])
print(s[::-1])

print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(s.find("awe", 0, 8))
# ? find(subs, start, end), return -1 if it fails to find certain substring
print(s.count("a"))
print(s.replace("awesome", "super"))

print(s.upper())
print(s.lower())
print(s.title())
