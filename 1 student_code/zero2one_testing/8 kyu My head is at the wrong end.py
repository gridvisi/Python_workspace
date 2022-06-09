'''
https://www.codewars.com/kata/56f699cd9400f5b7d8000b55/solutions/python

Test.describe("Basic tests")
Test.assert_equals(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
Test.assert_equals(fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])
Test.assert_equals(fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])
Test.assert_equals(fix_the_meerkat(["lower legs", "torso", "upper legs"]), ["upper legs", "torso", "lower legs"])
Test.assert_equals(fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])
'''

def fix_the_meerkat(arr):
    return arr[::-1]

def fix_the_meerkat(arr):
    temp = arr[0]
    arr[0] = arr[2]
    arr[2]= temp
    return arr

def fix_the_meerkat(arr):
    #your code here
    newarr = [ arr[2], arr[1], arr[0]]
    return newarr


#reverse
#name = [1,2,3]
#name = "李泓霏"  #str

#case str
name = "李霏泓"
print(name[0] + name[1:3][::-1]) #okay

#name[1] = '泓'
print(name)
'''
name[1] = '泓'
TypeError: 'str' object does not support item assignment
'''

name = list(name)
print('list:',name)
name[0] = 'zhang'
print('zhang:',name)

#list 逐一处理每个元素
# str 绑定一起

import math
def divisors(n):
    bench = int(math.sqrt(n))+1
    l = 2*len([i for i in range(2,bench) if n%i==0])
    return l+2-1 if math.sqrt(n) == int(math.sqrt(n)) else l+2

print(math.sqrt(100))





print(name[::-1])
print(sorted(name,reverse=True)) #反转顺序 #list
name = sorted(name,reverse=True)
name[1] = '泓'
print(name)
c = 'dog'
# 回文？是什么