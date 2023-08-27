# More string functions
# rjust() and ljust() are used to add spaces just to the left or right of the string
# provided that the number of characters to those functions
# Example
string_1 = "RAJAN"
print(string_1.rjust(8))
print(len(string_1.rjust(8)))
print(string_1.ljust(8))
print("Hello".ljust(6)+"world!")
# Center method to add spaces based on the total characters
# Example , also adding second argument to centre function changes fill character
print("RAJAN".center(6))
print("RAJAN".center(6, ":"))

# strip() removes from right side of string
# rstrip() removes from right side of a string
# lstrip() removes from left side of a string
# replace() searches and replace with given string , takes 2 arguments 1 to search for
# 2nd argument in replace is to replace with
# Example
print("    Rajan")
print("    Rajan".lstrip())
print("RAJAN".lstrip("R"))
print("RAJAN".rstrip("N"))
print("blueYELLOWblue".strip("buel"))
print("RAJAN".replace("A", "@"))

# Exercise
sample = "North Dakota"
print(sample.rjust(17))
print(sample.ljust(17, "*"))
print(sample.center(16, "+"))
print(sample.lstrip("North"))
print(sample.center(16, "+").rstrip("+"))
print(sample.center(16,"+").strip("+"))
print(sample.replace("North", "South"))

# len() returns length of string
# Example
print(len("RAJAN"))

# Exercise string reverse
sample = input("Enter a string")
sample_2 = ""

for a in range(len(sample) - 1, -1, -1):
    sample_2 += sample[a]

print(sample_2)

# Formatting strings with inbuilt functions
# Format() method

name = "RAJAN"
phone = "7887909187"
print("Name is : "+name+"Phone number is : "+phone)
print("Name is : ,{},Phone number is : ,{}".format(name, phone))
