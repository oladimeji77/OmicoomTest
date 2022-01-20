#to reuse a code

def fxn():
    pass

def squareroot(name):
    return name**2
sqr3 = squareroot(6)
print(sqr3)

def add2(num=0):   #you can save the result of a print function, use return instead so that the value can be stored in a variable
    return num+2
seven = add2(7)
nothing = add2() # it will not fail because it was set to a value by default.
print(seven)
print(nothing)


##Built-in python  functioms
# max and min
print(max(2,3))  #return max number 3
print(max([1,4,3,6,8,9])) #returns max number in a list
print(min(5,7))  #return min number

#Enumerate fxn

mylist = ['a', 'b', 'c']
index = 0
for letter in mylist:
    print(letter) 
    print(f'is at {index}')
    index = index+1
    print("")

mylist2 = ['d', 'e', 'f']
for item in enumerate(mylist2):
    print(item)

#Now unpack the tuple pair
for index,item in enumerate(mylist2):
    print(item)
    print(f"is at index: {index}")
    print("")

#Join function

mylist3 = ['a', 'b', 'c']
print("".join(mylist3))
print("--".join(mylist3))
print("+".join(mylist3))

#Fxn excersie Secret check

def secret_check(text):
    if "secret" in text:
        return True
    else:
        return False
print(secret_check("my little secret"))
#Alternatively, which is also d best way
def secret_check(text):
    return "secret" in text.lower()        # "secret in text"this is going to return a boolean, .lower incase of an edge case of capital letter "SECRET"
print(secret_check("my little SEcret"))
