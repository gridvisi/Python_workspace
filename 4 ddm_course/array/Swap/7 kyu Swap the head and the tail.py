'''
https://www.codewars.com/kata/5a34f087c5e28462d9000082/train/python

You need to swap the head and the tail of the specified array:

the head (the first half) of array moves to the end, the tail (the second half) moves to the start.
The middle element (if it exists) leaves on the same position.

Return new array.
For example:

    [ 1, 2, 3, 4, 5 ]   =>  [ 4, 5, 3, 1, 2 ]
     \----/   \----/
      head     tail

    [ -1, 2 ]  => [ 2, -1 ]
    [ 1, 2, -3, 4, 5, 6, -7, 8 ]   =>  [ 5, 6, -7, 8, 1, 2, -3, 4 ]
ALGORITHMSARRAYSBASIC LANGUAGE FEATURESFUNDAMENTALS

Test.it("Basic tests")
Test.assert_equals(swap_head_tail([ 1, 2, 3, 4, 5 ] ), [ 4, 5, 3, 1, 2 ])
Test.assert_equals(swap_head_tail([ -1, 2 ]), [ 2, -1 ])
Test.assert_equals(swap_head_tail([ 1, 2, -3, 4, 5, 6, -7, 8 ]), [ 5, 6, -7, 8, 1, 2, -3, 4 ])
'''

#10th solution by ericlee
def swap_head_tail(arr):
    lmid,rmid = len(arr)//2,len(arr)//2+len(arr)%2
    print(arr[:lmid],arr[rmid:],lmid,rmid)
    arr[:lmid],arr[rmid:] = arr[rmid:],arr[:lmid]
    return arr


arr = [ 1, 2, -3, 4, 8, 5, 6, -7, 8]
print(arr.index(8,5))
print(len(arr) , arr.index(8)+1)
print(len(arr) == arr.index(8)+1)

usa_president_name = '唐纳德特朗普'
print(usa_president_name[3:6])
print(usa_president_name[3:-1])
print(usa_president_name[3:-0])

i = 1
print([i for i in range(1,11)])
print('-1:',arr[i : -i])
print(arr[1:-1])

#arr = [ 1, 2, 3, 4, 5 ]

#print(arr[4:])
print(swap_head_tail(arr))

#1st solution
def swap_head_tail(arr):
    i = len(arr) / 2
    print(arr[-i:] , arr[i:-i] , arr[:i])
    return arr[-i:] + arr[i:-i] + arr[:i]
print(swap_head_tail(arr))


#2nd solution by ericlee
def swap_head_tail(a):
    r, l = (len(a)+1)//2, len(a)//2
    return a[r:] + a[l:r] +  a[:l]

