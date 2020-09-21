from datetime import date
import time

startTime = time.perf_counter()

ldates = []

d1 = date(2016, 8, 12)
d2 = date(2016, 7, 12)
d3 = date(2018, 8, 12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort(reverse=True)

time.sleep(3)
# ! time.sleep() : =setTimeout(seconds), delay execution

for d in ldates:
    print(d)


endTime = time.perf_counter()
# ? time.perf_counter() : performance time counter for benchmark

print("Execution Time", endTime-startTime)
