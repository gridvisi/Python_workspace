'''
https://brilliant.org/daily-problems/play-the-odds-1/
'''

numbers = {True: 0, False: 0}

for i in range(3, 25):  # 0b00011 - 0b11000
     if str(bin(i)).count("1") == 2:
        numbers[i % 2 == 0] += 1
        print(f"{i:05b} = {i}")

print(f"even: {numbers[True]}, odd: {numbers[False]}")