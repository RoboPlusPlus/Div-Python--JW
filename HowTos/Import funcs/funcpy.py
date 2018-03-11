
#Takes two iterables, and makes a dictionary with them.
#If the two dicts are of different lenghts, the dict will be ass long as the shortest of the inputs
#inputs may be any combination of tuple, set, string or list.

def two_iters_dict(key_iter, value_iter):
    dic={}
    if len(key_iter) < len(value_iter):
        dic_lenght = len(key_iter)
    else:
        dic_lenght = len(value_iter)

     
    for i in range(0, dic_lenght):
        dic.update({key_iter[i] : value_iter[i]}) 
    return(dic)


##############################################################
"""
Ideer

Merge_iters: tar verdier fra to iterables, setter de inn på en string eller tuple sammen som en entry, og så returnerer liste med alle


list_a_column: Henter ut en kolonne fra input iterable. som
listIn = [(1,2,3),("a", "b", "c", "d"), (4, 5, 6, 7, 8, 9)]
listOut = list_a_column(listIn, 2)
print(listOut) ##prints [3, "c", 6]



"""
