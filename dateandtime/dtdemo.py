import time
import datetime
epochseconds = time.time()
# ? time.time() : 1970.01.01부터 초를 세는 epoch time, return float
print(epochseconds)

t = time.ctime(epochseconds)
# ? time.ctime() : converted time (string) since epoch time
print(t)

dt = datetime.datetime.today()
print(dt, type(dt))
print('Current Date: {}/{}/{}'.format(dt.day, dt.month, dt.year))
print('Current Time: {}:{}:{}'.format(dt.hour, dt.minute, dt.second))
