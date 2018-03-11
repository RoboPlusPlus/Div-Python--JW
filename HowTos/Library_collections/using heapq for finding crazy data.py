"""
Using heapq to create a list over the largest and smallest numbers of a data-set
"""

import heapq
#Basic dataset/list
nums = [1, 2, 3, 4, -5, -15, 45, 33, 19, 22, -4, 0]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


#can also be used in more complicated data-structures

dataset =  [
    {'name': 'Dolan', 'Money': 50, 'craziness': 80.0},
    {'name': 'Ben', 'Money': 12, 'craziness': 60.0},
    {'name': 'Morgan', 'Money': 500, 'craziness': 10.0},
    {'name': 'Hillary', 'Money': 55740, 'craziness': 40.0},
    {'name': 'Trump', 'Money': 900451, 'craziness': 170.0},
    {'name': 'Bush', 'Money': 70756, 'craziness': 180.0}
]

#Gets the most wealthy and the most crazy
wealthy = heapq.nlargest(3, dataset, key=lambda s: s["Money"])
crazy = heapq.nlargest(3, dataset, key=lambda s: s["craziness"])

#prints it out for all to see
a=0
for i in wealthy:
    wealthy_names = wealthy[a]
    wealthy_name = wealthy_names['name']
    a+=1
    print("Number ", a, "wealthy is: ",wealthy_name)

a=0
for i in crazy:
    crazy_names = crazy[a]
    crazy_name = crazy_names['name']
    a+=1
    print("Number ", a, "crazy is: ",crazy_name)
