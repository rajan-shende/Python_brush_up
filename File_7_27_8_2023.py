# Loops : are used basically for iterative purpose.
# While loops
count = 0
while count <= 3:
    print("Hello")
    count += 1


# infinite while loops can be avoid by simply;
# the condition should be met to false.
# Also these(While loops) are used especially for unknown number of iterations
# Example of infinite while loop :
# while count < 5:
#     print("Hello ++")
# Exercise
var_1 = 10
while var_1 >= 1:
    print(var_1)
    var_1 -= 1

# Exercise
init = int(input("Enter a non negative & Non floating number\n"))
summed = 0
while init > 0:
    summed += init
    init -= 1

print(summed)

# For loop --> For executing the fixed number of iterations
# Example
var_1 = "RAJAN"

for letter in var_1:
    print(letter)
# Exercise
sample = "Hello world !"
for letter in sample:
    print(letter)
# Exercise
sample_2 = input("Enter a sample string value")
total_letters = 0
for letter in sample_2:
    total_letters += 1

print(sample_2)
print("Total letters in user entered string : "+str(total_letters))
# Range will return the preceding ranges starting from 0.
# Also the data type is range
# Example range used with single argument
sample_range = range(4)
print(sample_range, type(sample_range))
# Example range used with 2 arguments always starts with the first argument
# And ends with second argument-1
# Example
sample_range = range(3, 6)
print(sample_range)
for values in sample_range:
    print(values)
# Range used with 3 arguments ,
# The first two arguments ar as the same as in case range used with 2 arguments ,
# The 3rd argument is used as a step size to increment the iteration value over by that particular given value.
# Example
sample = range(1, 10, 2)
for value in sample:
    print(value)

for value in range(1, 5, 2):
    print(value)
    sample = range(10, 1, -2)

for value in sample:
    print(value)

for value in range(10, 1, -2):
    print(value)

# Exercise To print fizz if number is divisible by 3 and buzz if divisible by 5
# & FizzBuzz if divisible by both numbers
value = range(1, 51)
for a in value:
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)
# Exercise of factorial
fact = 1
value = int(input("Enter a number"))
for a in range(1, value + 1):
    fact = fact * a

print(fact)

