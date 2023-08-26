# Strings

var_1 = 'RAJAN'

var_1 = "RAJAN"
print(var_1[0])
print("RAJAN"[2])

# string slicing :
# it is the different part of same string
# 3 ways of slicing string :
#   1. from starting to it's specified character [:4]
#   2. from given start point and to specified end point [2:4]
#   3. from specified point till the end of string [4:]
var_1 = "apple"
print(var_1[:3])
print(var_1[0:3])
print(var_1[3:])

# Strings concatenation
# addition operator is used to concat strings
print("app"+"le")
var_1 = "app"+"le"
print(var_1)

# Exercise
var_1 = "just do it!"
print(var_1[10])
print(var_1[5:8])
print(var_1[8:])
print(var_1[:4])
var_1 = var_1[5:]
var_2 = "Dont"
print(var_2+" "+var_1)

# Type function is used to get the data_type
print(type(var_1))
# To convert something to string we're using str() function
var_1 = 9.0
print(type(var_1))
var_1 = str(var_1)
print(type(var_1))

# Escape sequences
print("RAJAN\tIS\tMY\n\\Name")

# Exercise
var_1 = 3.5
print(type(var_1))
print(str(var_1)+" is a float")
print("\"Hello I'm Rajan Nice to meet you!\"")

# Exercise printing triangle !
print(" ****\n ***\n  *")

# Input Function : input() function is used to get input from User
fruit = input("What is your favorite fruit ? \n")
print("Your favorite fruit is "+fruit)
# here the data type assigned is string itself

#Exercise
name = input("what is your name ?\n")
color = input("what is your favorite color?\n")
fruit = input("what is your favorite fruit?\n")
print("My name is "+name+"\n"+"I like "+fruit+"\t"+fruit+"\tis\t"+color)

# float() and int() functions are used to conert the strings into respective float and integer values
# These above float() and int() functions will not work with expressions

var_1 = int(input("Enter a Number"))
print(type(var_1))
var_1 = float(input("Enter value of pi\n"))
print(type(var_1))