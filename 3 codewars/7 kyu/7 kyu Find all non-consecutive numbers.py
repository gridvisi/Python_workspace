'''
https://www.codewars.com/kata/58f8b35fda19c0c79400020f/train/python

Your task is to find all the elements of an array that are non consecutive.
A number is non consecutive if it is not exactly one larger than the previous element
in the array. The first element gets a pass and is never considered non consecutive.
Create a function name all_non_consecutive
E.g., if we have an array [1,2,3,4,6,7,8,15,16] then 6 and 15 are non-consecutive.
You should return the results as an array of objects with two values
i: <the index of the non-consecutive number> and
n: <the non-consecutive number>.
E.g., for the above array the result should be:

[
  {'i': 4, 'n': 6},
  {'i': 7, 'n': 15}
]
'''
arr = [1,2,3,4,6,7,8,15,16]
def all_non_consecutive(arr):
    ans = []
    start = arr[0]
    i = 0
    #for i,e in enumerate(arr):
    while i < len(arr):
        if arr[i] == start:
            start += 1
            i += 1
        else:
            ans.append({'i':f"{i}",'n':f"{arr[i]}"})
            start = arr[i]
            #print(arr[i], start)
        #i += 1
    return ans
'''
Time: 818ms Passed: 103 Failed: 0
Test Results:
 A simple example
Test Passed
 A larger example
Test Passed
 All sequential
Test Passed
 Random cases
'''
print(all_non_consecutive(arr))

#1st
def all_non_consecutive(a):
    return [{"i": i, "n": y} for i, (x, y) in enumerate(zip(a, a[1:]), 1) if x != y - 1]

#2st
def all_non_consecutive(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i + 1] - arr[i] != 1:
            answer.append({'i': i + 1, 'n': arr[i + 1]})
    return answer