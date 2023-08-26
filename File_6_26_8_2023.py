# More string functions
var_1 = "RAJAN"
var_2 = "rajan"
print(var_1.lower())
print(var_1.isupper())
print(var_2.islower())
print(var_2.upper())

print("RAJAN shende".islower())
print("Rajan ".isupper())
print("".isupper())
print("".islower())
print("RAJAN".lower().isupper())

# more methods for alphanumeric characters
print("Rajan123".isalnum())
print("123344".isdigit())
print("  ".isspace())
print("12.23".isdecimal())
print("This".istitle())
print("rAJAN".istitle())

var_1 = "rajan is my name"
print(var_1.title())

var_1 = "this is startswith"
var_2 = "apple"
print("startswith ", var_1.startswith("this"))
print("endswith", var_2.endswith("le"))
print("".join(["RAJAN ", "SHENDE"]))
list_words = "RAJAN,SHENDE".split(",")
list_words = "RAJAN SHENDE".split(" ")
print(list_words)
print(list_words)

# Exercise -------------------------------------------

mixed_case = "A Song of Ice and Fire"
print("mised_case is upper result is :", mixed_case.isupper())
print("mised_case is upper result is :", mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())

title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith("mixed_case"))
print(mixed_case.endswith("mixed_case"))

words = mixed_case.split()
print(words)
print(" ".join(words))
print(title_case.isalpha())