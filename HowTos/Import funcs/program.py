import funcpy as fp

tup1=(1, 2, 3, 4, 5, 6, 7, 50)
tup2 =("a", "b", "c", "d", "e", "f", "g", "hest")
list1 =[1, 2, 3, 4, "Horse", "7", 33]
list2 = ["r", "t", "E", 2, 3, 4, "3", "dog", 50]
set1 = ([1, 2, 3, 4, 5, 6])
set2 = (["a", "b", "c", "d"])
s1 = "String1"
s2 = "String2"

##dict_from_2_tups = fp.two_iters_dict(tup1, tup2)
##dict_from_2_lists = fp.two_iters_dict(list1, list2)
##dict_from_2_sets = fp.two_iters_dict(set1, set2)
##dict_from_2_strings = fp.two_iters_dict(s1, s2)
##
##
##dict_from_1tup_1list = fp.two_iters_dict(tup1, list1)
##dict_from_1tup_1set = fp.two_iters_dict(tup1, set2)
##
##dict_from_1list_1tup = fp.two_iters_dict(list1, tup1)
##dict_from_1list_1set = fp.two_iters_dict(list1, set1)
##
##dict_from_1set_1tup = fp.two_iters_dict(set1, tup1)
##dict_from_1set_1list = fp.two_iters_dict(set2, list2)

#string

dict_from_1strings_1tup = fp.two_iters_dict(s1, tup1)


print(dict_from_1strings_1tup)
##
##print(dict_from_2_tups)
##print(dict_from_2_lists)
##print(dict_from_2_sets)
##
##
##print(dict_from_1tup_1list)
##print(dict_from_1tup_1set)
##
##print(dict_from_1list_1tup)
##print(dict_from_1list_1set)
##
##print(dict_from_1set_1tup)
##print(dict_from_1set_1list)




