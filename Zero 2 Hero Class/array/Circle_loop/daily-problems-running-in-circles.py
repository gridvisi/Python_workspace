'''
https://brilliant.org/daily-problems/running-in-circles/


'''

circumference = 2 * 300 + 2 * 200
for time in [2, 3, 5, 10]:
    if time * 300 % circumference == time * 200 % circumference:
        print(time)