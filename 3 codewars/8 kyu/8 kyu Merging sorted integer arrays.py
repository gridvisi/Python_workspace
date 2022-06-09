'''
https://www.codewars.com/kata/573f5c61e7752709df0005d2/solutions/python
Write a function that merges two sorted arrays into
a single one. The arrays only contain integers. Also,
the final outcome must be sorted and not have any duplicate.

5
5
1 -3 -5 4 4
2 4 4 6 -5
-5 -3 1 2 4 6
Process finished with exit code 0

'''

n = int(input())
m = int(input())
first = [int(n) for n in input().split()]
second = [int(n) for n in input().split()]
for i in first:
    if i not in second:
        second.append(i)
second = sorted(set(second))
for i in second:
    print(i,end=' ')
'''
first, second = [1, -3, -5, 4,4], [2, 4, 4,6, -5]
def merge_arrays(first, second):
    for i in first:
        if i not in second:
            second.append(i)
    return sorted(set(second))
print(merge_arrays(first, second))

for i in first:
    if i not in second:
        second.append(i)
print(sorted(set(second)))

for i in first:
    if i not in second:
        second.append(i)
print(sorted(set(second)))
'''
