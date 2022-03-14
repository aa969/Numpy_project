import numpy as np
import sys

# you can use numpy to work with 1D, 2D and 3D arrays. 1D arrays have one coordinates, 2D arrays have two coordinates
# and 3D arrays have three coordinates List can be used alternatively to Numpy, however, list are much slower whereas
# Numpy is much faster because of something called Fixed types.(faster to read less bytes of memory)
# Numpy carries out contiguous memory storage where all the data is stored low to each other in memory.

# The array below is a 1D array
a = np.array([1, 2, 3, 4], dtype='int16')
print(a)

b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(b)

# To find out the dimension of the array in question you need to use the .ndim function of Numpy.
print(a.ndim)
print(b.ndim)

# You can deduce the dimension of the using another function know as  .shape which gives answer as a vector.
print(a.shape)
print(b.shape)

# You can also find out the size of memory used by a given array (.itemsize this gives you the size each item in the
# array whereas, .nbytes give you the entire size of memory used) and the type of array you have by using the
# function .dtype it should be noted that intx the int part means integer sotred using x-bytes

print(a.dtype)
print(b.dtype)
print(a.itemsize)
print(b.itemsize)

# .size function tells you the total number of elements in the array
print(a.size)

L = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [11, 12, 13, 14, 15, 16, 17, 18, 19]])
print(L)
print(L.shape)
print(L.ndim)

# if you want to get the specific element from a array you would need to use the following notation:
# name_of_array[row, column]

print(L[0, 5])

# You go through an array and obtain elements in desired steps from the array
# this can be done using the following format [row, start_index:end_index:step_size]

print(L[0, 0:8:2])

# to change an element in a array you need to give it position and then the new element which is replacing it.

L[0, 5] = 20
print(L)

Y = np.array([[[1, 2, 3], [4, 5, 6]]])
print(Y.ndim)
print(Y.shape)
print(Y)

# Initializing(making) arrays from stretch you would use the format: np.zeros((row, column)) The zero implies that
# all the elements present in the array will be a zero. Alternately you could have np.ones((row, column)).

print(np.zeros((2, 3, 3)))
print(np.ones((2, 2, 2)))

# The line of code below also makes arrays with a give element in them.

print(np.full((2, 2), 21))

# The line of code below makes a array which have random elements in them. np.random.rand(row,columns)

print(np.random.rand(4, 2))

# The line of code below makes a random array of integer values
# .np.random.randint(range_of_random_values, size (number of rows, number of columns))
print(np.random.randint(7, size=(3, 3)))

# When copying a array make sure you the function .copy along with the name of the array being copied, for example x,
# copy.

# The line of code below add x amount to each element in the array

Q = np.array([1, 2, 3, 4, 5])
q = Q + 2
print(q)

# The line of code below subtracts x amount from each element in the array

T = np.array([23, 45, 45, 21, 5])
t = T - 2
print(t)

# The line of code below multiplies each element by x amount

F = np.array([1.2, 1.5, 1.9, 1.3])
f = F * 2
print(f)

# You can even add to arrays together as show below, but the arrays would need to have the same shape:

added_arrays = Q + T
print(added_arrays)

# linear algebra, look into how matrix are multiplied
# If you want to multiple matrices you would need to use the function .np.matmul(array_1, array_2)
a1 = np.ones((2, 3))
print(a1)

b2 = np.full((3, 2), 2)
print(b2)

print(np.matmul(a1, b2))

# Statistics with Numpy

stats = np.array([[1, 2, 3], [4, 5, 6]])

# the function below gives the min and max value in the array.

print(np.min(stats))
print(np.max(stats))

# The line of code below sum all the elements in the arrays
print(np.sum(stats))

# Reorganizing Arrays
# You can reorganize the Array by using the x.reshape function

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)

after = before.reshape((8, 1))
print(after)

# The code below show how to download data from a text file

filedata = np.genfromtxt('NumPy_data.txt', delimiter=',')
print(filedata)
