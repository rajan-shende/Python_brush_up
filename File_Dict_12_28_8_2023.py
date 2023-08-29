# Python dictionary
# dictionary are just simple key value pairs.
# Accessing value using keys
# Keys can be of different data types as well
# Dictionaries are unordered
# If you tried to get value of key which does not exists you will get key error
# in and not in for dictionary to check whether they Key exists in dictionary
# Dictionary methods
# key() returns all keys within dictionary
# values() returns all the values from that dictionary
# items() returns all key and values pairs of a dictionary If you use this method Python returns list of tuples
# If you want to use the not in and in with values in dictionary,
# you can use values() method to get values and then can check for
# get() method takes 2 arguments 1st as the key to look for and 2nd argument as a message if key not found
# If you assign the same dictionary to another one and if you make any changes;
# then the original will also change because they are referring the same
# can use len() function to get total no of key value pairs in a dictionary
# Dictionary methods some more pop() fromkeys() popitem()
# for dictionaries pop() must be used with argument as a key in that dictionary
# popitem() takes no arguments and removes the last key value pair from dictionay
# clear() method removes everything from dictionary it is called on.
# copy() creates totally new dictionary with new reference
# update() is used to update the existing dictionary if this is used on a dictionary
# and then passed another dictionary to it this will update the called dictionary.
# this setdefault() is used to check if the key exists in the given dictionary. If not we can add that using same
# The setDefault takes 2 arguments 1st as the key to look for and second is the value to assign if not found
# dict() to use dict() function we can add key values pairs as arguments to it which will result in a dictionary
# Example

dict_1 = {"key_1": 10, "Key_2": 20, 1001: 20.8, 3.14: "pie", False: 12}
print(dict_1)

print(dict_1['Key_2'])
print("we are total "+str(dict_1["Key_2"])+" people")

print(False in dict_1)
print("My" not in dict_1)

# Exercise
dict_1 = {1: 10, 2: 20, 3: 30, 4: 40}
print(dict_1[3])
print(5 in dict_1)
print(2 in dict_1)
print(dict_1.keys())

for keys in dict_1.keys():
    print(keys)
for values in dict_1.values():
    print(values)
print(dict_1.items())

for key, value in dict_1.items():
    print(key, value)

# Example
print(20 in dict_1.values())

# Example
print(dict_1.get("100", "NOT FOUND IN CURRENT DICTIONARY"))

# Exercise
dict_1 = {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive",
          "U2": "One", "Michael Jackson": "Billie Jean",
          "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
print(len(dict_1))
for key in dict_1.keys():
    print(key)
print(dict_1.values())

for key, value in dict_1.items():
    print(key, value)
print(dict_1.get("Promise of the Real", "KEY NOT FOUND !!"))

# Example
dict_1 = {}.fromkeys(["NAME"], "RAJAN")  # Here fromkeys() will create a dictionary with 1 key value pair
print(dict_1)

# Example
dict_1 = {1: 10, 2: 20, 3: 30, 4: 40}
print(dict_1.pop(2))
print(dict_1)

print(dict_1.popitem())
print(dict_1)

# Exercise

dict_1 = {}.fromkeys("aeiou", "consonant")
print(dict_1)
for key, value in dict_1.items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac",
                   "Burger King": "Whopper",
                   "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))
print(fast_food_items.popitem())
print(fast_food_items)

# Example
dict_1 = {1: 10, 2: 20, 3: 30, 4: 40}
# dict_1.clear()
print(dict_1)
dict_2 = dict_1.copy()
dict_2.popitem()
print(dict_1, dict_2)

# Exercise
internet_celebrities = {"DrDisrespect": "YouTube",
                        "ZLaner": "Facebook",
                        "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

internet_celebrities.update(another_one)
print(another_one)

var_1 = internet_celebrities.copy()
print(var_1)
internet_celebrities.clear()
print(internet_celebrities)

# Examples
dict_1 = {1: 10, 2: 20, 3: 30, 4: 40}
if 5 not in dict_1:
    dict_1[5] = 50
print(dict_1)

# Examples
dict_1.setdefault(6, 60)
print(dict_1)

new_dict = dict(a=1, b=2)
print(new_dict)