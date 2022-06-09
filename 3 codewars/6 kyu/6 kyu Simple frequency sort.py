'''
https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc/train/python

solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
--we sort by highest frequency to lowest frequency. If two elements have same frequency, we sort by increasing value
More examples in test cases.Good luck!

Please also try Simple time difference
ALGORITHM Spowered by
Test.it("Basic tests")
Test.assert_equals(solve([2,3,5,3,7,9,5,3,7]),[3,3,3,5,5,7,7,2,9])
Test.assert_equals(solve([1,2,3,0,5,0,1,6,8,8,6,9,1]),[1,1,1,0,0,6,6,8,8,2,3,5,9])
Test.assert_equals(solve([5,9,6,9,6,5,9,9,4,4]),[9,9,9,9,4,4,5,5,6,6])
Test.assert_equals(solve([4,4,2,5,1,1,3,3,2,8]),[1,1,2,2,3,3,4,4,5,8])
Test.assert_equals(solve([4,9,5,0,7,3,8,4,9,0]),[0,0,4,4,9,9,3,5,7,8])

'''
arr = [5, 9, 6, 9, 6, 5, 9, 9, 4, 4]
arr.sort()
print(arr)

#1st,2nd,3rd
from collections import Counter
def solve(a):
    c = Counter(a)
    return sorted(a, key=lambda k: (-c[k], k))

def solve(arr):
    return sorted(arr, key= lambda x: (-arr.count(x), x))

def solve(arr):
    return sorted(sorted(arr), key=lambda n: arr.count(n), reverse=True)

def solve(array):
    return sorted(sorted(array), key=array.count, reverse=True)



# eric's code
def solve(arr):
    return sorted(arr)
print(solve(arr))

from collections import *
def solve(arr):
    ans,arr = [],sorted(arr)
    re = Counter(arr)
    print(re)
    res = sorted([k for k in re.items()],key=lambda i:i[1],reverse=True)
    print(res)
    for i in res:
        for j in range(i[1]):
            print(ans)
            ans.append(i[0])
    return ans
#[str(i[0])*i[1] for i in res]
# #sorted(arr,key=lambda i:res[i][0])
print(solve(arr))


'''

def solve(arr):
    re = Counter(arr)
    return sorted(re,key=lambda i:len(str(i)))
print(solve(arr))

def solve(arr):
    res = [v*[str(k)] for k,v in Counter(arr).items()]
    #ans = sorted(res,key=lambda i:len(i),reverse=True)
    print(res)
    ans = sorted(res,key=lambda i:i[0],reverse=True)
    print(ans)
    ans = sorted(ans[::-1],key=lambda i:len(i),reverse=True)

    return [int(i) for i in list(''.join(ans))]
print(solve(arr))
'''