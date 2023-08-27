# Python sets
# Sets contain unordered collection of elements
# Set will always contain only Unique elements there are no duplicates
# Sets can be used in scenarios like distinct cities where olympic games happened
# Example
# Set declaration
set_1 = {10, 10, 20, "RAJAN", 30, 40}
print(set_1)

# Empty set use set() function to create an empty set
# Example

set_1 = set()
print(set_1)

# to create set using set range function we can do that
# Example
# Set of all even numbers  in 1 to 10
set_1 = set(range(0, 12, 2))
print(set_1)
# To access set elements in set we can use loops
# Example
set_1 = set(range(1, 11))
for a in set_1:
    print(a)
# we can check if a values is there in a particular set
# Example
set_1 = set(range(1, 11))
print(3 in set_1)
print(12 in set_1)

# Set methods :
# add()
# remove() if a element is not there in set and you use remove it will raise an error to avoid use discard()
# discard()
# clear() everything in the set will get removed
# copy() This will create a copy of the existing set in memory
# Union() This is used to combine all of the items from two different sets into a single set
# Also we can use | (pipe) to get result same as union().
# intersection is used to get the all common elements from two different sets
# set subtraction / difference this will return the elements which are not common in two sets.
# It will removes same elements based on intersection
# difference() this also works same as set difference like set1 - set2

# Examples
set_1 = {"stars", 3.14}
set_2 = set_1.copy()
set_3_union = set_1.union(set_2)
set_1.add("sun")
print(set_1)
set_1.remove(3.14)
print(set_1)
set_1.discard(3.14)
print()
set_1.clear()
print(set_1)
print(set_2)

set_4 = {10, 20}
set_5 = {30, 40, 10}
set_6 = set_4 | set_5
print(set_6)
print(set_4.intersection(set_5))
print(set_4 - set_5)  # remaining elements from set 4 will be returned
print(set_5 - set_4)  # remaining elements from set 5 will be returned
print(set_4.difference(set_5))

# Advanced set functions
# Set comprehension
# Example
set_1 = {even+2 for even in range(1, 10, 2)}
print(set_1)
low = {a.lower() for a in "APPLE"}
print(low)



