import array as arr

my_array = arr.array("i",[1,2,3,4,5,6,7,8,9,10])
copied_array_new = arr.array(my_array.typecode,[number for number in my_array])

# print(my_array)
# print(copied_array_new)
# print(my_array[0])
# print(len(my_array))
# for number in range(0,len(my_array)+1):
#     print(number)

#  Important Array Methods

# 1️⃣ Element Access & Modification
# append(x)

# Adds one element at the end.

my_array.append(6)
# [1, 2, 3, 4, 5, 6]


# extend(iterable)

# Adds multiple elements.

my_array.extend([7, 8])
# [1, 2, 3, 4, 5, 6, 7, 8]


# insert(i, x)

# Insert at index i.

my_array.insert(2, 99)
# [1, 2, 99, 3, 4, 5]

# pop([i])

# Removes and returns element at index i (default last)

my_array.pop()
my_array.pop(1)

# remove(x)

# Removes first occurrence of x.

my_array.remove(3)

# index(x)

# Returns index of first occurrence.

idx = my_array.index(4)

# count(x)

# Counts occurrences of x.

my_array.count(2)

# 2️⃣ Array Conversion Methods
# tolist()

# Convert array to Python list.

lst = my_array.tolist()

# fromlist(list)

# Append elements from list.

# my_array.fromlist([10, 11])

# tobytes()

# Convert array to bytes.

# my_array.tobytes(b)

# frombytes(bytes)

# Append elements from bytes.

# my_array.frombytes(b)

# 5️⃣ Copying & Reversal
# reverse()

# Reverse array in place.

my_array.reverse()

# __copy__() / slicing

copy_arr = my_array[:]

# 6️⃣ Attributes
# typecode

# Shows type of array.

# my_array.typecode   # 'i'

# Common typecodes:

# Typecode	Type
# i	signed int
# f	float
# d	double
# b	signed char
# B	unsigned char
# u	Unicode char

# itemsize

# Size of one element (bytes).

# my_array.itemsize

# 7️⃣ Built-in Python Support
# Length
# len(my_array)

# Indexing & Slicing
# my_array[0]
# my_array[1:4]

# Iteration
# for x in my_array:
#     print(x)

# Membership
# 3 in my_array

# 8️⃣ Comparison with Python List
# Feature	array	list
# Type safety	✅ Same type only	❌ Mixed types
# Memory efficient	✅	❌
# Fast numeric ops	✅	❌
# Flexible	❌	✅
# ✅ When to Use array.array

# ✔ Numerical data
# ✔ Memory-efficient storage
# ✔ Binary file I/O
# ✔ Low-level / performance-critical code


# ***********************************************************************
# ***********************************************************************

#  Multidimensional Array in Python using Numpy

from numpy import *

my_numpy_array = array([1,2,3,4,5,6,7,8,9,10])

# print(my_numpy_array)

# for number in my_numpy_array:
#     print(number)


two_dimension_array = array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(two_dimension_array)

three_dimensional_array = array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(three_dimensional_array)