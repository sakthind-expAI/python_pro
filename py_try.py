#python Learnings

#helloworld
print('hello world')

#version
import sys
print(sys.version)

#indentation - Python uses indentation to indicate a block of code. 	 	
if 5 > 2:
	print("Five is greater than two!") 
if 5 > 2:
	print("Five is greater than two!") 

#variables
x = 5
y = "Hello, World!"

#This is a comment - Multiline
#written in
#more than just one line
print("Hello, World!")

"""
This is a comment - Multiline
written in
more than just one line
"""
print("Hello, World!")

#Variables are containers for storing data values.
#A variable is created the moment you first assign a value to it.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


#Casting -to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#GetType
x = 5
y = "John"
print(type(x))
print(type(y))

#Case sensitive - variables
a = 4
A = "Sally"
#A will not overwrite a

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#my-var ="as" #illegal

"""
Camel Case
Each word, except the first, starts with a capital letter:
"""
myVariableName = "John"

"""
Pascal Case
Each word starts with a capital letter:
"""
MyVariableName = "John"

"""
Snake Case
Each word is separated by an underscore character:
"""
my_variable_name = "John"

#multiple values assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value assign to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z) 

#unpacking - If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
#unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = 5
y = 10
print(x + y)

"""
Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""
x = "awesome"

def myfunc():
	global x1
	x = "fantastic"
	x1 = xHi Saravana kumar, Hope you are doing well. I'm sakthi from visteon

I'm planning to explore outside based on my interest and current experience. Please let me know if you know any opening in your organization and outside as well.

Looking abroad opportunity and Chennai location if roles are good
	print("Python is " + x)

myfunc()
print("Python is " + x)
print("Python is " + x1)


#python --version
print("Hello world")

x = dict(name="John", age=36)
y = dict(name="John1", age=38)
z = dict(name="John2", age=43)


#display x:
print(x, y, z)

#display the data type of x:
print(type(x)) 

if 5 >2:
	print("Five is greater than two!") 
    
#assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

for a in x:
	print(a)
    
    
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#re
import re

s = "The quick brown fox jumps over the lazy dog"
pattern = "o"

print(re.findall(pattern, s)) # ['o', 'o', 'o', 'o']
print(re.search(pattern, s))  # <re.Match object>
print(re.split(pattern, s))   # ['The quick br', 'wn f', 'x jumps ', 'ver the lazy d', 'g']
print(re.sub(pattern, "a", s)) # The quick brawn fax jumps aver the lazy dag