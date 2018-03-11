##Priority Queue
##
##This snippet is more or less copied from "Python Cookbook 3rd edition" from O'Reilly. Creds to them.
##Tons of cool examples in that book, check it out. 



##The heapq module allows for a heap-data-structure, which allows for quick
##pushes and pops, limiting length of structure, converting lists to heaps etc.


import heapq 


############# Classes ###########
class PriorityQueue:
    def __init__(self):
        self._queue = []            #this list will fill up with its priority queue. 
        self._index = 0         

    def push(self, item, priority): #Function for pushing items into the queue list
        heapq.heappush(self._queue, (-priority, self._index, item)) #It is required that a priority number is part of the data structure passed to the function
        self._index +=1

    def pop(self):
        return heapq.heappop(self._queue)[-1] #Pop and return the smallest item from the heap. However, we have set priority as a negative, så this will be the "largest" item, or in our case, the item with highest priority. 


class item:                         #This class will be used to push items into the priority queue
    def __init__(self, name):
        self.name = name

    def __repr__(self):             # repr: return a string containing a printable representation of an object. 
        return 'Item({!r})'.format(self.name)



##############################

## Program. Passing stuff to the priority queue and popping those with the highest priority first


q = PriorityQueue()
q.push(item('Horse'), 1)
q.push(item('dawg'), 5)
q.push(item('turtle'), 19)
q.push(item('camel'), 2)
q.push(item('camel'), 4)
q.push(item('dawg'), 5)
q.push(item('dawg'), 5)

for i in range(0, len(q._queue)):
    print(q.pop())

## PRINTS:
##Item('turtle')
##Item('dawg')
##Item('dawg')
##Item('dawg')
##Item('camel')
##Item('camel')
##Item('Horse')

#does not matter if several elements have the same priority. 
