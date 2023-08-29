# Python lists
# are ordered collection of the values. values in list are also known as "items"
# The items are ordered collection
# list() will return list of provided arguments
# in and not in operators can be used to varify whether the element exists in the given list or not
# in and not in operators returns True or False based on the condition met
# Example
# Each item in list have their own index number. starting from 0.
# Accessing list from -ve index means it starts from end of list and backwards
# List methods
# del removes items from list. syntax del list1[1]
# remove() removes an element from list passed as an argument
# if remove() we used to remove item with multiple occurrences within list. It will remove only 1st occurrence.
# append() inserts a an item at the end of the list.
# insert() adds the element to list at specified position.
# It takes 2 arguments 1 argument is index , 2 argument is the item to be added
# sort() is used to sort list of either numbers or strings
# index() is used to find the index of the passed argument within list
# pop() removes an item from list and returns the removed item

list_1 = ["a", 10.9, "RAJAN"]
list_1 = [(10, 20, 30), ["RAJAN", "APPLE"]]

# Example
list_2 = list([1, 2, 3, 4])
print(list_2)
print(list("RAJAN"))

# Example of in and not in
list_1 = ["orange", "APPLE"]
print("APPLE" in list_1)
print("pineapple" in list_1)
print("pineapple" not in list_1)

# Exercise

list_1 = [1, 10.5, False, "RAJAN", [1, 2, 3, 4]]
list_2 = list("RAJAN")
print("e" in list_2)
print("a" not in list_2)

# Example
list_1 = [[1, 2, 3], ["a", "b", "c"]]
print(list_1[1][2])
print(list_2[-1])
print(list_2[-2])
print(list_2[-3])

# Items accessed using indexing can be used in the expression.
# The data type should be the same in this case.
# Example
list_1 = ["rajan", 3.14, 100]
print("Value of pie is : "+str(list_1[-2]))

# If we want to get a specific part of list we can slice the list & which results in the another list
# Example
list_1 = [1, 2, 3, 4, 5, 6]
print(list_1[2:5])
print(list_1[:3])
print(list_1[:-2])
print(list_1[1:])

# Reassignment of the list
list_1 = [1, 2, 3, 7]
print(list_1)
list_1[1:3] = [4, 5]
print(list_1)

# Exercise
list_1 = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(list_1[0])
print(list_1[3][1])
list_2 = ["chair", "table", "desk", "lamp", "bed"]
print(list_2[-5])
print("Most people own at least "+str(list_1[0][1])+" "+list_2[0])

list_3 = [0.98, 8.76, 6.54, 4.32]
print(list_3[1:])
print(list_3[1:3])
print(list_3[:2])

# Example list methods
list_1 = [1, 2, 3, 4, 5, 6, 5]
del list_1[2]
print(list_1)

list_1.remove(5)
print(list_1)

list_1.append("RAJAN")
print(list_1)
list_1.insert(1, 100)
print(list_1)
# print(list_1.sort()) this will raise an error if we use with the
list_1 = ["RAJAN", "APPLE", "kia", "SHENDE", "PEACH"]
# print(list_1.sort())
print(list_1.index("kia"))

# Example
list_1 = [1, 2, 3, 4, 5, 6, 5]
end = list_1.pop()
print(end)

# Exercise
animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del animals[-2]
print(animals)
animals.remove("elephant")
print(animals)
animals.append("arctic_fox")
print(animals)
animals.insert(2, "fox")
print(animals)
sorted = animals.sort()
print(sorted)
print(animals.index("fox"))
print(animals.pop())

# Lists vs strings
# Lists are mutable while strings are immutable
# line continuation

add = 1 + \
      3
print(add)