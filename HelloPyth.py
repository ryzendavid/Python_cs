#python 

import sys

#name = input("what is my name?")

#print
print("Hello, . Well done on writing first line of python")

print (sys.version)

if 5 > 2:
    print("5 is greater than 2. Shocker!")
    print("Might not be shocking for others.")

print("New block of code")

#variables... 

x = 5
y = "I don't like the indentation"

print(y)

#specifying data types of variables.. this is casting

z = str("3")
print(z)
print(type(z))

a = b = c = "Letters"

print(a,b,c)
print(b)

cars = ["Mercedes", "Volvo", "Peugot"]

M, V, P = cars

print(M,V,P)

print (cars)

print (x,y)

#global variables... 

x = 'awesome'

def myfunc():
    global x 
    x = 'bizzare but fun'
    print("Python is " + x)

myfunc()

#x = "not awesome"
print(x)

N = None

#list vs tuple... 

List = ["List 1", "List 2", "List 3","List 4"]

Tuple = ("Tuple 1","Tuple 2","Tuple 3","Tuple 4")



List = ["List 4","List 3","List 2"]



Tuple = ("Tuple 4","Tuple 3")

List[1] = ("Tup")

print(List)
print(Tuple)

print (type(Tuple))

#imaginary numbers(complex type)

i = 3  #j is imaginary number

print(type(i))

#converting number types...

e = float(i) #this is converted from int to float

#casting

num = int(4)

print (num)

#for loop in strings

for q in "Quebec":
 print(q)
quotees = "Brown cows do not produce chocolate milk 💀"
if "chocolate" in quotees:
   print(quotees)
   print("chocolate" not in quotees)
   print(quotees[6:17])


password = "    12345 68  "

passSplit = password.strip()
print(passSplit)

#concatenate strings..... 

str1 = "hello"
str2 = "Friend"
strConcat = str1 +" "+ str2
print(strConcat)

boysAge = 12

print(f"The boys ages is {boysAge}")   #f-string is used to format string and placeholders are values/variables inside the curly bracket

print (f"The price is £ {boysAge * 12:.2f}")

#Booleans??

print (10 > 19)

#if statements in python... 

tNumber = 25
qNumber = 35

if qNumber > tNumber:
   print(qNumber > tNumber) and print("qNumber is greater that the tNumber")
else:
   print(qNumber < tNumber)

print(bool(4))

def boolFunc():
   return False

print(boolFunc())

def checkFunc():
   return False

if checkFunc():
   print("Function is true")
else:
   print ("Function has returned false")


print(5%2)

""""
This is a multiline comment that has been created by me... 
More lines... 

I will create more of this on the line and then close it
"""

#Lists in python
ListExample = ["example1", "example2",  "3", 4, 6.0, 7]


print(ListExample)
print(type(boysAge))

ListExample[1:4] = "this is now example3", "now examp4" , "int changed to str", 7,8.0
ListExample.insert(3, "impostorExample")
ListExample.remove("this is now example3")
ListExample.pop(1)

print(ListExample)

print("contd.. python. I wonder if I can do this. I think I can maybe. If you really want to, then you will.....")

#looping lists... 

#listlooper= ["examp1", "examp2", "examp4"]

# for x in listlooper:
#  print(x)

#loopint with index... 

listloopRange = ["examp1", "examp2", "examp4"]
for k in range(len(listloopRange)):
   print(listloopRange[k])

#while

listwhile = ["examp1", "examp2", "examp4"]
i = 0 
while i < len(listwhile):
 print(listwhile[i])
 i += 1

 #list comprehension allows looping with the shortes syntax 

listcomp = ["examp876", "examp2", "examp4"]
[print (i) for i in listcomp] 


listTest = ["examp1", "examp2", "examp4"]
if "examp1" in listTest:
   print(listcomp)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)




def funcpen():
   pen = 23.5
   yen = 4.6
   if pen > yen:
    print("pen is greater than yen then")

funcpen()
print("I'm back")

#List comprehension

fruits = ["apple", "mango", "kiwi", "banana"]
newList = []

for f in fruits:
   if "a" in f:
      newList.append(f)

print(newList)

#with list comprehension

newListComp = [q for q in fruits if "n" in q]

print(newListComp)

print("back in trying new")

#tuples....

tupleExample = ("tupleOne", "TupleTwo", "TupleThree")

tupleOneValue = ("TpleOneValueTwo",)
print(tupleOneValue)
print(tupleExample)

#check if value in... 

if "tuple5" in tupleExample:
   print("Command Executed. Tuple1 is present in the example")
else:
   print("command not found: Error")


listedTuple = list(tupleExample)

listedTuple[1] = "changedTupleValue"
listedTuple.append("AddedTupleValue")
listedTuple.remove("AddedTupleValue")

tupleExample = tuple(listedTuple)

tupleExample += tupleOneValue
 

print(tupleExample)

#tuple unpacked... assigning values to variables... 

#looping tuples... 

for x in tupleExample:
 print(x)

for i in range(len(tupleExample)):
   print(tupleExample[i])


w = 0
while w < len(tupleExample):
   print(tupleExample[w]) 
   w += 1


countTup = tupleExample.count("tupleOne")

print(countTup)

#Python sets... 

setExample = {"SetOne", "SetTwo", "SetThree", "SetFour"}
setExample2 = {"SetNine"}
for x in setExample:
   print(x)

#adding to sets.... 

setExample.add("setFive")
setExample.update(setExample2)
setExample.update(tupleExample,ListExample)  #.update joins 2 or *more sets.. 
setExample.remove("SetNine")  #can also add other arrays as well(lists, dict, tuple)   


#use the set.clear to delete/clear the entire values of the set.. or use del set

print(setExample)


# frozenset is immutable. ensures that it cannot be changes.. 
q = frozenset({"FrozenSet1", "FrozenSet2"})
print(q)
print(type(q))


#Dictinaries... used to store data in Key value pairs (KVP)

dictExample = {
   "brand" : "Ford",
   "model" : "Mustang",
   "year" : 2018,
   "Owner" : "John Young",
   "colors" : ["red", "blue" , "green"] #values in dicts can be any data type, including lists... 
}

print(dictExample["brand"])

m = dictExample.get("model")
print(m)

k = dictExample.keys()
print(k)

v = dictExample.values()
print(v)

dictExample["Owner"] = "Sarah Banks"


print(type(dictExample))



if "Owner" in dictExample: 
 print("The car has an owner")

#use .update to add items to dict
