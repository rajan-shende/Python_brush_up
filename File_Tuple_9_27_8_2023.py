# Tuples can have multiple different datatypes within
# you can access tuple values using index
# We can slice tuples exactly like a string
# Example
# Tuples are immutable once are declared we cannot Modify them.
# Tuples will get 48 bytes as List gets 64 so are faster than lists
# Tuples slicing with stride length like tp_2[2::2] , tp_2[::-2]
# Count() returns the number of occurrences of a value in a tuple
# index() function will return the index of that particular tuple element

tp_1 = (1, False, "RAJAN", 3.14)
print(tp_1)
# Crating tuple from tuple() constructor
tp_1 = tuple([10, 20.3, "RAJAN"])
tp_2 = tuple("RAJAN")
print(tp_2)
print(tp_1)
print(tp_1[0])
print(tp_1[:2])
print(tp_2[1:2])
print(tp_1.__sizeof__())

# iterating over tuples
tp_1 = ("RAJAN", "SHENDE", "APPLE")
for value in tp_1:
    print(value)
# Examples of more tuple slicing
tp_2 = (10, 20, 30, 40, 50, 100, 60, 70, 80, 90, 100, 110)
print(tp_2[::2])
print(tp_2[2::7])
print(tp_2[::-2])  # from backwards stepping

# Nested tuples
tp_1 = ((10, 20, 30), (40, 50, 60), (70, 80, 90))
print(tp_1[1][1])
print(tp_2.count(100))
print(tp_2.index(20))