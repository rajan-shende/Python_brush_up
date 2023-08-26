import random
# Functions usability of a small piece code
# Avoid deduplication
# Creating a function is defining
# Function name follows the same naming conventions as variable names
# To execute the lines of code written in Function one should be giving call to them
# Samples of the functions
def my_fun():   # Function with no parameters
    print("Hello")


def my_fun(para_1):  # Function with 1 parameter
    print(para_1)


def my_fun(para_1, para_2):  # Function with multiple parameters
    print(para_1, para_2)


def my_fun_1(para_1=10, para_2=20):  # Function with default parameters
    print(para_1, para_2)


my_fun_1()
my_fun(1, 2)

# Returning something from function


def square_2(a):
    print(a ** a)


square_2(2)

# Exercise


def hello_world():
    print("Hello World !")


hello_world()


def info(phone):
    phone = input("Enter your phone")
    print("Your phone is ", phone)

info(1)

# Exercise calculate volume of rectangular prism

def cal_volume():
    length = float(input("Enter length"))
    width = float(input("Enter width"))
    height = float(input("Enter height"))
    print("Volume is :", length*width*height)

cal_volume()

#Exercise to convert celsius to ferenhit


def celcius_to_ferenhit(c):
    F = 1.8 * c + 32
    print(F)

celcius_to_ferenhit(100)

# Modules
# To use functionality within modules you must import them first and then can use the functions within
# Below are importing types
# Generic import Ex. import google to call functions within google like google.search()
# Function import Ex. from google import search
# Universal import Ex. from google import *

# Exercise

miles = random.randint(100, 200)
liters = random.randint(1, 10)
print("milage is :", round(miles / liters, 2))

# Variable scopes : Local and global
# Variables defined at the global level I can say very first declaration within python file are global
# Local variables are defined within function