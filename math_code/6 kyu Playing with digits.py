'''
https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

test.assert_equals(dig_pow(89, 1), 1)
test.assert_equals(dig_pow(92, 1), -1)
test.assert_equals(dig_pow(46288, 3), 51)
'''


def dig_pow(n, p):
    ans = 0
    for i in str(n):
        p += 1
        ans += int(i) ** (p-1)
    if ans % n == 0:
        return ans//n
    return -1
n,p = 46288, 3
print(dig_pow(n, p))


#1st solution
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

