'''
https://www.codewars.com/kata/5b165654c8be0d17f40000a3/train/python


In this Kata, you will be given a number and your task will be to rearrange the number so that it is divisible by 25, but without leading zeros. Return the minimum number of digit moves that are needed to make this possible. If impossible, return -1 ( Nothing in Haskell ).

For example:

solve(521) = 3 because:
    a) Move the digit '1' to the front: 521 -> 512 -> 152. The digit '1' is moved two times.
    b) Move '5' to the end: 152 -> 125. The digit '5' is moved one time, so total movement = 3.
Of all the ways to accomplish this, the least digit moves = 3.

solve(100) = 0. Number already divisible by 25.
solve(1) = -1. Not possible to make number divisible by 25.

solve(0) is not tested.

Test.it("Basic tests")
Test.assert_equals(solve(3848363615),-1)
Test.assert_equals(solve(75733989998),17)
Test.assert_equals(solve(87364011400),0)
Test.assert_equals(solve(2992127830),-1)
Test.assert_equals(solve(98262144757),1)
Test.assert_equals(solve(81737102196),-1)
'''
from collections import Counter
def solve(n):
    it = iter(str(n)[::-1])#print(Counter(n))
    cunt = 0
    nkey = ['0','2','5','7']
    ans = []
    #avoid = [['2,','7'],['0','7'],['0','2']]
    for i in it:
         print(i)
         if i in nkey:  #[k for k,v in ndict.items()]
             ans.append((i,str(n)[::-1].index(i)))
             for i in it:
                 print(ans)
                 if i in ['0','5']:
                     ans.append((i,str(n)[::-1].index(i)))

    return sorted(ans,key=lambda x:ans[1])

n = 75733989998  #for i in str(n)
n = 3848363615
n = 98262144757
n = 502305
n = 87364011400
n = 2992127830
print(solve(n))

'''
 from collections import Counter
def solve(n):
    #print(Counter(n))
    cunt = 0
    nkey = ['0','2','5','7']
    ndict = dict([(k,v) for k,v in Counter(str(n)).items() if k in nkey])
    print(ndict)
    avoid = [['2,','7'],['0','7'],['0','2']]
    for k,v in ndict.items():
         print(sorted(ndict))
         if sorted(ndict) in avoid:  #[k for k,v in ndict.items()]
             print('if')
             return -1

         elif ndict.get('0',None):
             if ndict.get('0',None) >= 2:
                print('elif')
                cunt += sum([str(n)[::-1].index(i) for i in str(n) if i == '0']) -1
             return cunt

         else:
             print('else',[str(n)[::-1].index(i) for i in str(n) if i in sorted(ndict)])
             cunt += sum([str(n)[::-1].index(i) for i in sorted(ndict)])
             return cunt


'''