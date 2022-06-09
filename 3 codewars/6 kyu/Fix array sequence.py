'''
https://www.codewars.com/kata/5b7bae02402fb702ce000159/train/python

Test.it("Basic tests")
Test.assert_equals(solve([1,3]),[3,1])
Test.assert_equals(solve([4,2]),[2,4])
Test.assert_equals(solve([12,3,9,4,6,8]),[9,3,6,12,4,8])
Test.assert_equals(solve([4,8,6,3,12,9]),[9,3,6,12,4,8])

For the above example:
solve([12,3,9,4,6,8]) = [9,3,6,12,4,8].
[9,3,6,12,4,8] -- 9/3=3 -> 3*2=6 -> 6*2=12 -> 12/3=4 -> 4*2=8
'''
arr = [4,8,6,3,12,9]

def solve(arr):
    even = sorted([i for i in arr if i %2 == 0])
    modthree = sorted([i for i in arr if i %3 == 0])
    return even,modthree

def solve(arr):
    #it = iter(arr)
    i = 0
    s = arr[i]
    while s in arr and i < len(arr):
        res = []
        s = arr[i]
        if s % 3 == 0 and s // 3 in arr:
            #if s not in res and s%3 not in res:
            res.append(s)
            res.append(s//3)
            s = s//3
        else:
            i += 1

        if s % 3 != 0 and s*2 in arr:
            #if s not in res and s*3 not in res:
            res.append(s)
            res.append(s*2)
            s = s*2
        else:
            i += 1
        print(res)
        if len(res) == arr:
            return res
print(solve(arr))

def solve(a):
    for i in a:
        li = [i]
        while 1:
            if li[-1] % 3 == 0 and li[-1] // 3 in a:
                li.append(li[-1] // 3)

            elif li[-1] * 2 in a:
                li.append(li[-1] * 2)
            else:
                break
        if len(li) == len(a):
            return li
print(solve(arr))
