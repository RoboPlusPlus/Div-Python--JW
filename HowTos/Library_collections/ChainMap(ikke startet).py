
from collections import deque
from collections import ChainMap

q= deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.appendleft(9)
a= q.popleft()
print(q)
