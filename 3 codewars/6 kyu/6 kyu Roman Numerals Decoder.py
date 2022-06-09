'''
Create a function that takes a Roman numeral as its argument and returns its value as a numeric
 decimal integer. You don't need to validate the form of the Roman numeral.

创建一个函数，该函数以罗马数字作为参数，并将其值作为十进制数字整数返回。你不需要验证罗马数字的形式。
Modern Roman numerals are written by expressing each decimal digit of the number to
be encoded separately, starting with the leftmost digit and skipping any 0s.
So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered
"MMVIII" (2000 = MM, 8 = VIII).
The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
现代罗马数字是通过分别表示要编码的数字的每一个十进制数字来书写的，
从最左边的数字开始，跳过任何0。
因此1990被呈现为“M CM XC”（1000=M，900=CM，90=XC）
2008被呈现为“M M VIII”（2000=MM，8=VIII）。
1666年的罗马数字“MDCLXVI”按降序使用每个字母。
#"""complete the solution by transforming the roman numeral into an integer"""
'''

#print(max[1,1.0])
#Symbol    Value
I =         1
V =         5
X =         10
L =         50
C =         100
D =         500
M =         1000

def solution(roman):

    r = ['I','V','X','L','C','D','M'] #roman
    a = [1,5,10,50,100,500,1000] #abrabic
    dict_ra = dict(zip(r,a))
    re = [dict_ra[l] for l in roman]
    print(dict_ra)
    print('re:',sum(re))
    if len(re) == 1: return re[0]
    s,i = 0,0
    while i <= len(re)-2:
        if re[i:i+2] == sorted(re[i:i+2],reverse=True):
            s += sum(re[i:i+2])
        else:
            s += re[i:i+2][-1] - re[i:i+2][-2]
        if i+1 > len(re) -2:return s
        s -= re[i+1]
        i += 1

roman = 'MCMXC'  #=1990
#roman = 'MDCLXVI' # 2210
#roman = 'MMVIII'
roman = 'XXI'
#roman = 'IV'
#roman = 'V'
roman = 'MMMCMXCIX'  # 1000+1000+1000-100+1000-10+100-1+10
roman = 'XXI'
roman = 'MCMXC'  #=1990
roman = 'MMXX'
roman = 'CMXCVIII'
print(solution(roman))
def solution(roman):
    dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += dict[c]
        elif last > dict[c]:
            total -= dict[c]
        else:
            total += dict[c]
        last = dict[c]
    return total
roman = 'MCMXC'  #=1990
roman = 'CMXCVIII'
roman = 'VIV'
roman = 'MMXI'
roman = 'MXDCCLXXVI'
print('top:',solution(roman))
from functools import reduce
def solution(roman):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return reduce(lambda x, y: x + y if x >= y else y - x, (d[c] for c in roman))
roman = 'MCMXC'  #=1990
roman = 'CMXCVIII'
roman = 'VIV'
roman = 'MMXI'
roman = 'MXDCCLXXVI'
#print('t',solution(roman))

'''d
test.describe("Example Tests")
test.assert_equals(solution('XXI'), 21, 'XXI should == 21')
test.assert_equals(solution('I'), 1, 'I should == 1')
test.assert_equals(solution('IV'), 4, 'IV should == 4')
test.assert_equals(solution('MMVIII'), 2008, 'MMVIII should == 2008')
test.assert_equals(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')


  for i,e in enumerate(re):
      if re[i] < re[i+1]:re[i] = - re[i]
      
   while i < j <= len(re):
        if re[i:j] == sorted(re[i:j],reverse=True):
            s += sum(re[i:j])
            i += 1
            j += 1
        else:
            s -= 
            j += 1
print(solution(roman))

       for i in range(1,len(re)):
        peak = [i for i in range(1,len(re)-1) if re[i-1] < re[i] and re[i] > re[i+1]]
        bottom = [i for i in range(1,len(re)-1) if re[i-1] > re[i] and re[i] < re[i+1]]
'''