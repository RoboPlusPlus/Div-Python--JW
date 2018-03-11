"""
Python "star expression" can be used to address this problem.

You want to drop the first and last element from a list, and return the average
of the values in the middle
"""

def avg(invar): #Just a function to calculate the average of an iterable
    try:
        d= sum(invar)
        e= len(invar)
        return d/e
    except:
        print("Cannot find average of object")



def drop_first_last(values): 
    first, *middle, last = values #The "*" expression allow us to assign all values of our iterable to the "middle" variable
    return middle #returning the input(values), minus the first and the last element
    
values = [1, 4, 3, 7, 5, 6, 2, 23, 9]

values_in_the_middle = drop_first_last(values)

result=avg(values_in_the_middle) #using the avg function we made to calculate the average, and copying it into "result"
print(result)



