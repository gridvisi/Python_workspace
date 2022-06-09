'''
https://www.codewars.com/kata/5609fd5b44e602b2ff00003a/train/python

We need a function that receives two arrays, each of them with elements that occur only once. We need to know:

Number of elements that are present in both arrays
Number of elements that are present in only one array
Number of remaining elements in arr1 after extracting the elements of arr2
Number of remaining elements in arr2 after extracting the elements of arr1
Example
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [2, 4, 6, 8, 10, 12, 14]
The result is: [4, 8, 5, 3]

4 elements present in both arrays: 2, 4, 6, 8
8 elements present in only one array: 1, 3, 5, 7, 9, 10, 12, 14
5 elements remaning in arr1: 1, 3, 5, 7, 9
3 elements remaning in arr2: 10, 12, 14
No doubt, an easy kata to warm up before doing the more complex ones. Enjoy it!

FUNDAMENTALSDATA STRUCTURESMATHEMATICSALGORITHMSNUMBERS
'''

def process_2arrays(arr1, arr2):
    a,b = set(arr1),set(arr2)
    return [len(a&b),len(a)+len(b)-len(a&b),len(a)-len(a&b),len(b)-len(a&b)]

#list(map(len,[a&b, a+b - a&b, a-a&b, b-a&b]))

arr1 = [1, 2 ,3,4, 5 ,6 ,7 ,8 ,9]
arr2 = [2, 4, 6, 8, 10, 12, 14]
a,b = set(arr1),set(arr2)
print(a|b)
print(process_2arrays(arr1,arr2))

#1
def process_2arrays(arr1, arr2):
    s1,s2 = set(arr1), set(arr2)
    return [len(s1 & s2), len(s1 ^ s2), len(s1 - s2), len(s2 - s1)]