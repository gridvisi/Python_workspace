'''
https://www.codewars.com/kata/frog-jumping/python

You have an array of integers and have a frog at the first position

[Frog, int, int, int, ..., int]

The integer itself may tell you the length and the direction of the jump

 For instance:
  2 = jump two indices to the right
 -3 = jump three indices to the left
  0 = stay at the same position
Your objective is to find how many jumps are needed to jump out of the array.

Return -1 if Frog can't jump out of the array

Example:
array = [1, 2, 1, 5];
jumps = 3  (1 -> 2 -> 5 -> <jump out>)
All tests for this Kata are randomly generated.
Test.assert_equals(solution([1, 2, 2, -1]), 4)
Test.assert_equals(solution([1, 2, 1, 5]), 3)
Test.assert_equals(solution([1, -1]), -1)
ALGORITHMSFUNDAMENTALSARRAYS
'''

def solution(a):
   if (len(a) == 0):
     return -1
   pos = 0
   jump = 0
   while pos >= 0 and pos < len(a):
      if (a[pos] == 0): return -1
      step = a[pos]
      a[pos] = 0
      pos += step
      jump += 1
   return jump

def solution(a):
    if not a: return -1
    posSet, i = set(), 0
    while i not in posSet:
        posSet.add(i)
        i += a[i]
        if not (0 <= i < len(a)):
            return len(posSet)
    return -1

def solution(a):
    pos = 0
    jumps = 0
    for i in range(len(a)):
        pos += a[pos]
        jumps += 1
        if pos >= len(a) or pos < 0:
            return jumps
    return -1

def solution(a):
    step,next = 0,0
    while next < len(a):
        step += 1
        next = a[next]+next
        #print(next,step)
        if step > 100:return -1
        if next >= len(a) or next <= -1: return step