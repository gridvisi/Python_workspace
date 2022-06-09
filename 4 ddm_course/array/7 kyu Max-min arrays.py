'''
https://www.codewars.com/kata/5a090c4e697598d0b9000004/train/python
Test.it("Basic tests")
Test.assert_equals(solve([15,11,10,7,12]),[15,7,12,10,11])
Test.assert_equals(solve([91,75,86,14,82]),[91,14,86,75,82])
Test.assert_equals(solve([84,79,76,61,78]),[84,61,79,76,78])
Test.assert_equals(solve([52,77,72,44,74,76,40]),[77,40,76,44,74,52,72])
Test.assert_equals(solve([1,6,9,4,3,7,8,2]),[9,1,8,2,7,3,6,4])
Test.assert_equals(solve([78,79,52,87,16,74,31,63,80]),[87,16,80,31,79,52,78,63,74])
'''
arr = [78,79,52,87,16,74,31,63,80]
def solve(arr):
    i,j,ans = 0, len(arr),[]
    arry = sorted(arr,reverse=True)
    print(arry)
    while i < j:  # Pls check if i <= j, what happen??
        if i == j-1:
            ans.append(arry[i:j][0])
        else:
            ans.append(arry[i:j][0])
            ans.append(arry[i:j][-1])
        i += 1
        j -= 1
    return ans
print(solve(arr))

#1st solution
def solve(arr):
    arr = sorted(arr, reverse=True)
    res = []
    while len(arr):
        res.append(arr.pop(0))
        if len(arr):
            res.append(arr.pop())
    return res

#2nd solution
def solve(arr):
    lmax, lmin = iter(sorted(arr)) , iter(sorted(arr)[::-1])
    return [next(lmax) if i%2==1 else next(lmin) for i in range(0,len(arr))]

#3rd solution
def solve(arr):
    return [sorted(arr)[::-1][(-1)**i*i//2] for i in range(len(arr))]

#4th solution
def solve(arr):
    arr.sort(reverse=True)
    return [arr.pop(-(i % 2)) for i in range(len(arr))]
'''
def solve(arr):
    ans = []
    i = 0
    while i < len(arr):
        ans.append(max(arr[i:]))
        ans.append(min(arr[i:]))
        i += 1
    return ans
'''