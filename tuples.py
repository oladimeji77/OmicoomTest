#tuples are immutable nd are used in brackets
#sets
#booleans 

#Tuples 
t = (1,"ball",3,4,5,6,"deji", True)
print(t)
print(t[2])  #grab the iten in index 2, this is 3
#t[0] = 10 - this is not possible
print(t) #get error because it is immutable

#Set unordered collection of unique elements
car = set()
print(car)
car.add("toyota")
car.add("Tesla")
car.add("Ferari")
car.add("Lexus")
car.add("Lexus")
car.add("toyota")
print(car)   #notice that it doesn't repeat any item, only the unique elements
mylist = [1,2,3,1,2,1,4,6,6,8,9,7,5,6,8,6]
print(set(mylist))

#Booleans
a = True
b = False
c = None
print(a)
print(b)
print(c)
print(12>5)
print(7<3)


