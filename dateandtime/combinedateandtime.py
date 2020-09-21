from datetime import *

d = date(2018, 7, 21)
t = time(12, 45)
dt = datetime.combine(d, t)
# ? datetime.combine(date, time) : contruct datetime object
print(dt)
