'''

https://www.codewars.com/kata/5436f26c4e3d6c40e5000282/train/python


test.assert_equals(sum_of_n(3), [0, 1, 3, 6])
test.assert_equals(sum_of_n(1), [0, 1])
test.assert_equals(sum_of_n(0), [0])
test.assert_equals(sum_of_n(-4), [0, -1, -3, -6, -10])

 5  -->  [0,  1,  3,  6,  10,  15]
-5  -->  [0, -1, -3, -6, -10, -15]
 7  -->  [0,  1,  3,  6,  10,  15,  21,  28]
'''

def sum_of_n(n):
    st = 0
    flag = 1 if n > 0 else -1
    i = 0
    step = 0
    ans = []
    while i < abs(n)+1:
        ans.append(i*flag+step)
        step += i*flag
        i += 1
    return ans
n = 0
print(sum_of_n(n))

#1st solution
def sum_of_n(n):
    return [(-1 if n < 0 else 1) * sum(range(i+1)) for i in range(abs(n)+1)]