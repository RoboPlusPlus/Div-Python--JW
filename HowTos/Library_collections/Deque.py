"""deque er en slags listelignende-container med
rask append og pop i begge ender
"""
from collections import deque

q= deque(maxlen=3)#Setter maksimal lengde. 
q.append(1)
q.append(2)
q.append(3)
q.append(4) #siden maks lengde er satt = 3, vil nå den eldste verdien (1) dyttes ut)
q.append(5) # her dyttes (2) ut, deque er nå 3, 4, 5
q.appendleft(9)
print(q) # setter verdien 9 inn på venstre side. Nå detter 5 ut. deque er nå 9, 3, 4
a= q.popleft() # popper venstre, nå er det bare to verdier igjen i deque 3, 4
print(q)
