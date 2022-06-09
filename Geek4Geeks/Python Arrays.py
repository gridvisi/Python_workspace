# https://www.geeksforgeeks.org/python-arrays/


# Python program to demonstrate
# Creation of Array

# importing "array" for array creations
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print('a:',a)
# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")

#Output:

'''
向数组中添加元素
可以通过使用内置的insert()函数将元素添加到数组中。
Insert用于向数组中插入一个或多个数据元素。根据要求，
一个新的元素可以被添加到数组的开头、结尾或任何给定的索引。
append()也被用来在数组的结尾添加其参数中提到的值。

'''
# Python program to demonstrate
# Adding Elements to a Array

# importing "array" for array creations
import array as arr

# array with int type
a = arr.array('i', [1, 2, 3])

print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# inserting array using
# insert() function
a.insert(1, 4)

print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")
print()

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()

# adding an element using append()
b.append(4.4)

print("Array after insertion : ", end=" ")
for i in (b):
    print(i, end=" ")
print()


'''
Accessing elements from the Array
In order to access the array items refer to the index number. 
Use the index operator [ ] to access an item in a array. 
The index must be an integer. 
'''

# Python program to demonstrate
# accessing of element from list

# importing array module
import array as arr

# array with int type
a = arr.array('i', [1, 2, 3, 4, 5, 6])

# accessing element of array
print("Access element is: ", a[0])

# accessing element of array
print("Access element is: ", a[3])

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# accessing element of array
print("Access element is: ", b[1])

# accessing element of array
print("Access element is: ", b[2])


'''
Removing Elements from the Array
Elements can be removed from the array by using built-in remove() function 
but an Error arises if element doesn’t exist in the set. 

Remove() method only removes one element at a time, to remove range of 
elements, iterator is used. pop() function can also be used to remove and 
return an element from the array, but by default it removes only the last 
element of the array, to remove element from a specific position of the 
array, index of the element is passed as an argument to the pop() method.
Note – Remove method in List will only remove the first occurrence of the 
searched element. 
 
'''
# Python program to demonstrate
# Removal of elements in a Array

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 5])

# printing original array
print("The new created array is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")

print("\r")

# using pop() to remove element at 2nd position
print("The popped element is : ", end="")
print(arr.pop(2))

# printing array after popping
print("The array after popping is : ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")

print("\r")

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print("The array after removing is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")

'''
Slicing of a Array
In Python array, there are multiple ways to print the whole array 
with all the elements, but to print a specific range of elements 
from the array, we use Slice operation. 

Slice operation is performed on array with the use of colon(:). 
To print elements from beginning to a range use [:Index], to print 
elements from end use [:-Index], to print elements from specific 
Index till the end use [Index:], to print elements within a range, 
use [Start Index:End Index] and to print whole List with the use of 
slicing operation, use [:]. 

Further, to print whole array in reverse order, use [::-1]. 
'''

# Python program to demonstrate
# slicing of elements in a Array

# importing array module
import array as arr

# creating a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")

# Print elements of a range
# using Slice operation
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)

# Print elements from a
# pre-defined point to end
Sliced_array = a[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_array)

# Printing elements from
# beginning till end
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)


'''
Searching element in a Array
In order to search an element in the array we use a python in-built 
index() method. 

This function returns the index of the first occurrence of value 
mentioned in arguments. 
'''

# Python code to demonstrate
# searching an element in array


# importing array module
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print("The new created array is : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")

print("\r")

# using index() to print index of 1st occurrenece of 2
print("The index of 1st occurrence of 2 is : ", end="")
print(arr.index(2))

# using index() to print index of 1st occurrenece of 1
print("The index of 1st occurrence of 1 is : ", end="")
print(arr.index(1))


'''
Updating Elements in a Array
In order to update an element in the array we simply reassign a new value to the desired index we want to update. 
'''

# Python code to demonstrate
# how to update an element in array

# importing array module
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print("Array before updation : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")

print("\r")

# updating a element in a array
arr[2] = 6
print("Array after updation : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")
print()

# updating a element in a array
arr[4] = 8
print("Array after updation : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")