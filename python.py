"""
print("Hello, World!")
"""

"""
if 5 > 2:
  print("Five is greater than two!")
"""
"""
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
"""
"""
x = 5
y = "Hello, World!"
"""
"""
x = 5
y = "John"
print(x)
print(y)
"""
"""
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
"""
"""
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
"""
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""
"""
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""
"""
x = "awesome"
print("Python is " + x)
"""
"""
x = "Python is "
y = "awesome"
z =  x + y
print(z)
"""
"""
x = 5
y = 10
print(x + y)
"""
"""
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
"""
"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
"""
"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
"""
"""
#x = 5
#x = "Hello"
#x =20.5
#x=1j
#x = ["apple","Banana"]
#x = ("apple",'Orange')
#x = range(6)
#x = {"name" : "siddharth", "age" : 23}
#x = {"apple","Banana","grapes"}
#x = frozenset({"apple", "banana", "cherry"})
#x = True
#x = b"Hello"
#x = bytearray(5)
#x = memoryview(bytes(5))
#x = str("Hello World")		
#x = int(20)	
#x = float(20.5)		
#x = complex(1j)		
#x = list(("apple", "banana", "cherry"))		
#x = tuple(("apple", "banana", "cherry"))		
#x = range(6)		
#x = dict(name="John", age=36)		
#x = set(("apple", "banana", "cherry"))		
#x = frozenset(("apple", "banana", "cherry"))		
#x = bool(5)		
#x = bytes(5)	
#x = bytearray(5)		
#x = memoryview(bytes(5))

print(type(x))
"""
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex
x = 1
y = 35656222554887711
z = -3255522
x = 1.10
y = 1.0
z = -35.59
x = 35e3
y = 12E4
z = -87.7e100
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
"""
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
"""
"""
import random

print(random.randrange(1, 10))
"""
"""
x = int(1)
y = int(2.8)
z = int("3")
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2")
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  
print(x)
print(y)
print(z)
"""
"""
print("Hello")
print('Hello')
a = "Hello"
print(a)

#a = """#Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua."""
#print(a)
#a = '''Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.'''
#print(a)
#a = "Hello, World!"
#print(a[1])
#print(a[2:5])
#print(a[-5:-2])
#print(len(a))
#print(a.strip())
#print(a.lower())
#print(a.upper())
#print(a.replace("H", "J"))
#print(a.split(","))
"""
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
"""
"""
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 
"""
"""
a = "Hello"
b = "World"
c = a + b
print(c)
"""
"""
a = "Hello"
b = "World"
c = a + " " + b
print(c)
"""
"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
"""
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
"""
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
"""
"""
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
"""
"""
f = open("demofile.txt","r")
#print(f.read())
#print(f.read(5))
print(f.readline())
f.close()
"""
"""
f = open("demofile.txt", "r")
for x in f:
  print(x)
"""
"""
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()
"""
"""
f = open("demofile.txt", "r")
print(f.read())
"""
"""
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
"""
"""
f = open("demofile.txt", "r")
print(f.read())
"""
#f = open("myfile.txt", "x")
#f = open("myfile.txt", "w")
"""
import os
os.remove("demofile.txt")
"""
"""
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
"""
"""
import os
os.rmdir("myfolder")
"""
"""
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
"""
"""
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))
"""
"""
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
"""
"""
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
"""
"""
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
"""
"""
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
"""
"""
username = input("Enter username:")
print("Username is: " + username)
"""
"""
try:
  print(x)
except:
  print("An exception occurred")
"""
"""
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
"""
"""
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
"""
"""
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
"""
"""
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
"""
"""
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
"""
"""
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
"""
"""
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
"""
"""
import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
"""
"""
import re

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
"""
"""
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 
"""
"""
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
"""
"""
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
"""
"""
import re

#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
"""
"""
​import re

#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
"""
"""
​import re

#Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
"""
"""
import re

#The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)
"""
"""
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
"""
"""
​import re

#The string property returns the search string:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
"""
"""
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
"""
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)