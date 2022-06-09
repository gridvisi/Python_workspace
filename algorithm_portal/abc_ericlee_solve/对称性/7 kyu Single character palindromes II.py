'''
https://www.codewars.com/kata/5a66ea69e6be38219f000110/train/python

solve ("abbx") = True, because we can convert 'x' to 'a' and get a palindrome.
solve ("abba") = False, because we cannot get a palindrome by changing any character.
solve ("abcba") = True. We can change the middle character.
solve ("aa") = False
solve ("ab") = True
'''

#18th solution by ericlee
def solve(s):
    #isPair = [int(s[i] == s[len(s)-1-i]) for i in range((len(s)-1)//2)]
    isPair = [int(s[i] == s[- 1 - i]) for i in range(len(s) // 2)]
    print(isPair)
    if len(s) % 2:return sum(isPair)==len(s)//2 or sum(isPair)+1 == len(s)//2
    return isPair.count(0)==1

s = 'aa'
s = 'ab'
s = "abbx"
s = "abcba"
#s = "abbaa"
print(solve(s))


#1st solution
def solve(s):
    v = sum(s[i] != s[-1-i] for i in range((len(s))//2) )
    return v == 1 or not v and len(s)%2
