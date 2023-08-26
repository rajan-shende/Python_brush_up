from random import randint
# Flow control
# Comparators & booleans
# 6 Comparison operators as below : (These evaluates in boolean values)
# >
# <
# >=
# <=
# !=
# ==
# 3 Boolean operators :
# and
# or
# not

# Examples :
print(4 > 8)
print(4 == 4)
# Floats and integers might be equal as below :
print(4.0 == 4)

# Examples of boolean operators
print(4 >= 4 and True)
print(False or True)
print(False or False)
print(6 <= 3 and True or False)

# If statements
if True:
    print("it is true")
if False:
    print("it is false")

# else statements
if 1 > 2:
    print("condition is true !!")
else:
    print("The condition is false")

if 1 < 2:
    print("condition is true !!")
else:
    print("The condition is false")

# Nested if else statements
# Example of pi using if else
# We are not suppose to use type function with if else statement.
# Recommendation is to use isinstance function instead
fruit = input("Enter a fruit")
if isinstance(fruit, str) == isinstance("RAJ", str):
    if True:
        print("Fruit is string type")
# Examples
score = float(input("Enter your score"))

if score:
    if score >= 90:
        print("Congratulations , \nYour grade is A !!")
    if score >= 80:
        print("Congratulations , \nYour grade is B !!")
    if score >= 70:
        print("Congratulations , \nYour grade is C !!")
    else:
        print("Sorry the scores are too low !!!")

# elif statements :
score = float(input("Enter your score"))

if score >= 90:
    print("Congratulations , \nYour grade is A !!")
elif score >= 80:
    print("Congratulations , \nYour grade is B !!")
elif score >= 70:
    print("Congratulations , \nYour grade is c !!")
else:
    print("Scores are too low !!!!!!")

# Roman numbers example:

normal_number = randint(1, 10)
if normal_number == 1:
    print("Roman number for "+str(normal_number)+"is I")
elif normal_number == 2:
    print("Roman number for " + str(normal_number) + "is II")
elif normal_number == 3:
    print("Roman number for " + str(normal_number) + "is III")
elif normal_number == 4:
    print("Roman number for " + str(normal_number) + "is IV")
elif normal_number == 5:
    print("Roman number for " + str(normal_number) + "is V")
elif normal_number == 6:
    print("Roman number for " + str(normal_number) + "is VI")
elif normal_number == 7:
    print("Roman number for " + str(normal_number) + "is VII")
elif normal_number == 8:
    print("Roman number for " + str(normal_number) + "is VIII")
elif normal_number == 9:
    print("Roman number for " + str(normal_number) + "is IX")
elif normal_number == 10:
    print("Roman number for " + str(normal_number) + "is X")

# Truthy and falsy values
# EMp
score = 10
if score:
    print("Score is true value")
score = False

if score:
    print("score is false")

score = "Hello"
if score:
    print("score is string")

var_1 = ""
if var_1:
    print("Var_1 is false")

# Truthy and Falsy values for int = 0 , for float = 0.0
# bool() used to convert into bool values

print(bool("False"))
print(bool(True))
print(bool(False))

print(bool(0))
print(bool(0.0))
print(bool(""))