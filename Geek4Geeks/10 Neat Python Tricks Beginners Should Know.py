
#Trick #1
#Reversing a string in Python
a =  "codementor"
print ("Reverse is",a[::-1])
#Reverse is rotnemedoc

#2 Trick
#Transposing a Matrix
mat = [[1, 2, 3], [4, 5, 6]]
zip(*mat)
#[(1, 4), (2, 5), (3, 6)]

#3 Trick
a = [1,2,3]
#Store all three values of the list in 3 new variables
a = [1, 2, 3]
x, y, z = a
print(x,y,z)

#4 Trick
a = ["Code", "mentor", "Python", "Developer"]
#Create a single string from all the elements in list above.
print(" ".join(a))

#Code mentor Python Developer
#5 Trick
list1 = ['a', 'b', 'c', 'd']
list2 = ['p', 'q', 'r', 's']
#Write a Python code to print
'''
ap
bq
cr
ds
'''
for x, y in zip(list1,list2):
   print(x, y)

#6 Trick
#Swap two numbers with one line of code.
a=7
b=5
b, a =a, b


#7 Trick
print("codecodecodecode mentormentormentormentormentor") #without using loops
print("code"*4+' '+"mentor"*5)
#codecodecodecode mentormentormentormentormentor

#8 Trick
a = [[1, 2], [3, 4], [5, 6]]
#Convert it to a single list without using any loops.
# Output: [1, 2, 3, 4, 5, 6]
import itertools
list(itertools.chain.from_iterable(a))
#[1, 2, 3, 4, 5, 6]


#9 Trick
# Checking if two words are anagrams
def is_anagram(word1, word2):
    """Checks whether the words are anagrams.
    word1: string
    word2: string
    returns: boolean
    """
#Complete the above method to find if two words are anagrams.

from collections import Counter
def is_anagram(str1, str2):
     return Counter(str1) == Counter(str2)
print(is_anagram('abcd','dbca'))
#True
print(is_anagram('abcd','dbaa'))
#False

#10.Trick
#Taking a string input.
#For example "1 2 3 4" and return [1, 2, 3, 4]

#Remember list being returned has integers in it.
#Don't use more than one line of code.

result = map(lambda x:int(x) ,input().split())
#1 2 3 4
print(result)
#[1, 2, 3, 4]
