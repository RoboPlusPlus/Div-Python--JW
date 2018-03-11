"""
Moving average filter

"""
from collections import deque

filterWidth = 5
d_signal = (2.0, 6.3, 9.8, 8.4, 10.32, 9.7, 8.9, 7.1, 6.7, 5.4, 6.5, 7.7, 8.9, 7.1, 6.7, 5.4, 6.5)
q= deque(maxlen=filterWidth)


def avg(arg):
    try:
        a=len(arg)
        b = sum(arg)
        return b/a
    except:
        print("Could not process argument")


for i in range(0, len(d_signal)):
    q.append(d_signal[i])
    print(avg(q))


print("Final values in filter: ", *q)
