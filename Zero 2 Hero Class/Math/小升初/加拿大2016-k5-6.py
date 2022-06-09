
'''
# 19. Richard writes down all the numbers with the following properties: (i) the first digit
is 1, (ii) each of the following digits is at least as big as the one before it, (iii) the sum of the
digits is 5. How many numbers does he write?
'''
from itertools import combinations
d = [i for i in range(1,10)]
result = []
for x in d:
    if 1 + sum([int(i) for i in list(str(x))]) == 5:
        result.append(f"1{x}")
print(result)

'''
20. Luigi started a small restaurant. His friend Giacomo gave him some square tables and
chairs. If he uses all the tables as single tables with 4 chairs each, he would need 6 more chairs.
If he uses all the tables as double tables with 6 chairs each, he would have 4 chairs left over.
How many tables did Luigi get from Giacomo?
'''

table = 0
while 4*table - 6 != 0.5*table*6 + 4:
    table += 1
print(table)

'''
# 24. A little kangaroo is playing with his calculator. He starts with the number 12. He
multiplies or divides the number by 2 or 3 for 60 times in a row. Which of the following results
cannot be obtained?
'''
# x:乘以2，y：除以2，m：乘以3，n：除以3
# x + y + m + n == 60
# result = (x - m) * 2 + (y -n) * 3
# 2*x - 2*m + 3*y - 3*n
# 3*x - m + 4*y