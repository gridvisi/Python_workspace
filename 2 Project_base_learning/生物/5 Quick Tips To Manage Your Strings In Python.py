#String multiplication
#Python allows multiplying not only numbers, but also strings! Repeat a string as simply as follows:
print("a"*3)
'aaa'

#You may also multiply strings by a boolean value. For instance, the following snippet pads a number with a leading zero if it’s lower than 10:
sn = lambda n: '{}{}-{}'.format('0' * (n < 10), n,n-1)
print(sn(9)) #'09'
print(sn(10)) #'10'
sn = lambda n: '{}{}{}{}{}'.format('0' * (n < 11), n,n-1,n-2,n-3) #[i for i in range(n)])
print('2020:',sn(10)) #'09'

phone = list("19115025630")
sn = lambda n: '{}{}{}-{}{}{}{}-{}{}{}{}'.format(1,9,1,1,5,0,2,5,6,3,0)
print(sn(10)) #'10'

#Title
#Nowadays, it’s common to write titles (even in Medium), capitalizing the first letter of each word. Well, you can achieve this very easily with Python:
print("the curious frog went to denmark".title())
'The Curious Frog Went To Denmark'

#Concatenate:You may concatenate two strings using the + operator, but that’s not the best approach. Python strings are immutable, making this operator create a new string from these two strings, instead of simply adding the second one to the first one, as we could have thought. It’s better (and faster), instead, to concatenate them using the join() function:
print("".join(["abc", "def"]))
'abcdef'

#Get a substring:Obtain a substring using Python’s slicing. You just need to specify the starting index (included) and the ending index (excluded):
print("Such a good day"[7:11]) #'good'

#Reverse a string:A string slicing allows you to optionally define a third parameter: the step. If you take the full string and apply a step of -1, you’ll get the reversed string:
print("Such a good day"[::-1])#'yad doog a hcuS'

import re
def ReTel(tn):
    reg = "1[3|4|5|7|8][0-9]{9}"
    return re.findall(reg, tn)
#\(?   ?表示括号可有可无      \(表示匹配(
#0\d{2,3}  区号。0xx或0xx
#[) -]?  区号后面可以跟")"," ","-"，也可能什么都没有
#\d{7,8} 7位或8位的号码
print(ReTel("19115025630"))  # 正确
print(ReTel("xxddewl"))  # 号码不合法
print(ReTel("12698563215"))  # 号码不合法
print(ReTel("177225482"))  # 号码短

a = "19115025630"
a = "02388888888"
if (n := len(a)) > 11:
    print(f"List is too long ({n},expected > 11)")
elif (n := len(a)) <= 11:
    print(f"phone-num-length is right({a[0:3]}-{a[3:6]}-{a[7:11]},expected <= 11)")