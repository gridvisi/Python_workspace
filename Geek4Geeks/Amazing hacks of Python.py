'''
https://www.geeksforgeeks.org/amazing-hacks-python/


'''

# Declaring the list geek
geek = ['Geeks', 'Programming', 'Algorithm', 'Article']

# Directly printing the list
print("Simple List:", geek)

# Printing the list by join method
print('List by using join method: %s' % ', '.join(geek))

# Direct use of join method
print('Direct apply the join method:', (", ".join(geek)))

'''
Cool Zip tricks

Transpose a matrix: You can Read Here about this.
Partition a list into N groups: We used iter() as an iterator over a sequence
'''

# Declaring the list geek
geek = ['Sun', 'Flowers', 'Peoples', 'Animals', 'Day', 'Night']

partition = list(zip(*[iter(geek)] * 2))
print(partition)

'''
Explanation: [iter(geek)] * 2 produces a list containing 2 items of geek[] list, i.e. a list of length 2. *arg unpacks a sequence into arguments for a function call. Therefore we are passing the same iterator 2 times to zip().


'''
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

# Here zip() function takes two equal length list and merges them
# together in pairs
for a, b in zip(list1, list2):
    print(a, b)

'''
Take the string as input and convert it into list:

# Reads a string from input and type case them to int 
# after splitting to white-spaces
  
formatted_list = list(map(int, input().split()))
print(formatted_list)
'''

Convert
list
of
list
into
single
list

# import the itertools
import itertools

# Declaring the list geek
geek = [[1, 2], [3, 4], [5, 6]]

# chain.from_iterable() function returns the
# elements of nested list
# and iterate from first list
# of iterable till the last
# end of the list

lst = list(itertools.chain.from_iterable(geek))
print(lst)