'''
https://brilliant.org/daily-problems/cryptogram-the-eye/
'''

ans = []
three_digit = list(range(100,1000))
for x in three_digit:
    for y in three_digit:
        total = x + y
        if len(str(total)) >= 4:
            if str(x)[-1]== str(y)[-1] == str(y)[0] == str(total)[-2]:
                ans.append([x,y])
print(len(ans),ans)


#2nd filter
ans_2 = []
for x in three_digit:
    for y in three_digit:
        total = x + y
        if len(str(total)) >= 4:
            if str(x)[-1]== str(y)[-1] == str(y)[0] == str(total)[-2]:
                if str(total)[0] == str(x)[0]:
                    ans_2.append([x,y])
print(len(ans_2),ans_2)


#3rd
#2nd filter
ans_2 = []
for x in three_digit:
    for y in three_digit:
        total = x + y
        if len(str(total)) >= 4:
            if str(x)[-1]== str(y)[-1] == str(y)[0] == str(total)[-2]:
                if str(total)[0] == str(x)[0] and str(x)[1] == str(total)[1]:
                    # 最后一个条件没有用到 Y
                    ans_2.append([x,y])
print(len(ans_2),ans_2)


'''
The highest possible result of adding two three-digit numbers is 999+999=1998,999+999=1998, so \yellow{T}T must be 1.1.

Because \yellow{T} \blue{H}\red{E}\green{Y}>1000THEY>1000 and \yellow{T} \blue{H}\red{E}<200,THE<200, we know that \red{E} \green{Y}\red{E}EYE must be larger than 800.800. So, \red{E}=8E=8 or \red{E}=9.E=9.

If \red{E}=8,E=8, then \red{E}+\red{E}=16,E+E=16, so \green{Y}=6.Y=6. Then, looking at the tens column, we see that 1+\blue{H}+6=8,1+H+6=8, so \blue{H}H must equal 1,1, which contradicts the uniqueness condition.

So, \red{E}=9E=9 and \green{Y}=8.Y=8. Again, the tens column tells us that 1+\blue{H}+8=9,1+H+8=9, so \blue{H}=0.H=0. Indeed,

109+989=1098.
109+989=1098.

This means that the smallest digit in the puzzle is 0.0.
'''
