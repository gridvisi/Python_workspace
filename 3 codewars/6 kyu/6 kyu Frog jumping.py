'''
https://www.codewars.com/kata/frog-jumping/train/python
 For instance:
  2 = jump two indices to the right
 -3 = jump three indices to the left
  0 = stay at the same position
Your objective is to find how many jumps are needed to jump out of the array.

Return -1 if Frog can't jump out of the array

Example:
array = [1, 2, 1, 5];
jumps = 3  (1 -> 2 -> 5 -> <jump out>)
'''

a = [1, 2, 1, 5]

#a = [1, 2, 2, -1]
a = [1, -1]
a = [1,2,1,1,2]
a = []
#print(a[-1],a[0])

#1st solution
def solution(a):
    if not a: return -1
    posSet, i = set(), 0
    while i not in posSet:
        posSet.add(i)
        i += a[i]
        if not (0 <= i < len(a)):
            return len(posSet)
    return -1


#2nd solution
def solution(a):
    step,next = 0,0
    while next < len(a):
        step += 1
        next = a[next]+next
        if step > 100:return -1
        if next >= len(a) or next <= -1: return step

#2nd solution
def solution(a):
   if not len(a): return -1
   jump = pos = step = 0
   while pos >= 0 and pos < len(a):
      if (a[pos] == 0): return -1
      step = a[pos]
      a[pos] = 0
      pos += step
      jump += 1
   return jump

a = [1, 2, 1, 5]
print(solution(a))


'''
def solution(a):
    step,next = 0,0
    while next < len(a):
        step += 1
        next = a[next]+next
        print(next,step)
        if step > 100:return -1
        if next >= len(a): return step

print(solution(a))
'''
