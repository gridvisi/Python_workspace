
n = 1000
s1,s2,s5,s55,m,p = 0,0,0,0,0,0
print(str(1007)[len(str(1007)) -2:len(str(1007))])
for i in range(1,1001):
    m += str(i)[-1].count('2')
    p += str(i)[-1].count('5')
    if i % 25 == 0 and  i % 100 != 0 and i % 10 != 0:s5 += 1
    if i % 125 == 0 and i % 100 != 0 and i % 10 != 0:s55 +=1
    if i % 100 == 0:s2 += 1
    if i % 10 == 0:s1 += 1
    s = s1 + s2*2 + s5 + 1 + s55

print(s+ (m+p)//2 + s55)

'''
    m += str(i)[-1].count('2')
    p += str(i)[-1].count('5')
  if str(i)[len(str(i)) -2:len(str(i))] == '00':s1 += 1
    if str(i)[-1] == '0':s2 += 1
    
he key insight here is the following chain of logic:

A trailing zero is equivalent to having 10 as a factor.
10=5\times210=5×2
Every even number has 2 as a factor, so the limiting quantity on factors of 10 is the number of 5's.
So, to answer this question, we need to find how many 5's are present in the factorization of 1000! = 1 \times 2 \times 3 \times \dots \times 999 \times 1000.1000!=1×2×3×⋯×999×1000.

At a first pass, we have 5, 10, 15, 20, \dots, 10005,10,15,20,…,1000: 200 multiples of 5 between 1 and 1000 (this is 1000/5=2001000/5=200).

However, some of these multiples of 5 have more than one 5 as factors (consider 25=5^225=5 
2
 ). Let's add to our count the numbers that have at least two 5's as factors: 25, 50, \dots, 100025,50,…,1000. There are 1000/25=401000/25=40 of these.

In addition, we have 8 numbers with at least three 5's: 125, 250, \dots125,250,… and exactly 1 with four 5's: 625.

Therefore the total number of 5's that can be factored out of 1000! is 200+40+8+1=249200+40+8+1=249.

The number of trailing zeros is 249.
'''