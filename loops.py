#For loops to iterate through an object eg string, list, key in a dictionary

numlist = [1,2,3,4,5,6,7]
for item in numlist:
    print (item)
    print(item**2) #item squared
    print('Hello dimeji') #prints d string by the number of items in the list

name = 'oladimeji'
for char in name:
    print(char)
    print("hello " + name)

salaries = {'deji':30, 'afo':40, 'eni':78} #notice it iterates over the keys and not the value

for keys in salaries:
    print(keys)

for keys in salaries:  #to print the values of the key  
    print(salaries[keys])

salaries = {'alaka':30, 'chi':40, 'ken':78}
for employee in salaries:
    print(employee + " Hello chairman your salary is " + str(salaries[employee]))


#Tuple Unpacking ie grabbing each item in a tuple list
item = [("a",1), ("b",2), ('c',3)]
for letters,num in item:
    print(letters)
    print(num)

#While loop - continue to execute a fxn until it becomes true

i = 1
while i<5:
    print(f"{i} is less than 5")
    i=i+1


#Range  range(0,5)
for i in range(2,8):
    print(i)

for x in range(0,11,2):
    print(x)

print(range(0,12,3))

print(list(range(0,9,2)))  #or

result = list(range(0,101,10))
print(result)

#in Keyword returns a boolean, work on list and string only.

numlist = [1,2,3,4,5,6]
print(1 in numlist)

print("z" in "oladimeji")

