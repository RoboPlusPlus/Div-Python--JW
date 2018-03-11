p = (12, 5, 3) #Tuple with three elements. Deconstructing it. 
x, y, z = p #You need a variable for every element in P, so you don't get an error
print(x) 
print(y)
print(z)


#Unpacking Dolans data
data= ['Dolan', 5, 91.1, (2015, 12, 2)] 
name, hight, silly_scale , dateOfBirth =data #assigning variables to the elements like this

#Printing it, so you can see it
print ("Name: ", name)
print("hight: ", hight)
print("Sillyness between 0 and 100: ", silly_scale)
print("Date of birth: ", dateOfBirth)

#You can also name the elements in the tuple, like this
name, hight, silly_scale, (year, mon, day) = data


#Proof of concept
print(name,": is born in: ",year,", and is ",silly_scale,"silly on a scale of 0-100.")


#This works on all iterable objects

