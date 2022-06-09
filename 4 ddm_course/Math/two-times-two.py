'''
https://brilliant.org/daily-problems/two-times-two/


'''
import random
digit = 3
# print(random.randint([i for i in range(10)])) Not work!!
print(random.randint(0,9))
print(random.choice(''.join([str(i) for i in range(9)])))

def two_times_two(digit):  # not trigger condition
    st,nd = 10**(digit-1),10**digit
    d = ''.join([str(i) for i in range(9)])
    #d = [i for i in range(10)]
    T = random.choice([int(i) for i in d if i != '0'])
    W = int(random.choice([int(i) for i in d if i != T]))
    O = random.choice([int(i) for i in d if int(i) != T and int(i) != W])
    mul = T*10**(digit-1) + W*10**(digit-2) + O*10**(digit-3)
    a = [T,W,O]
    b = [i for i in range(1,digit+1)]
    mul = list(map(lambda x,y: x*10**(digit-y),a,b))
    #print(T,W,O,mul)
    return sum(mul)
print(two_times_two(digit))


ans = []
for _ in range(10000):

    m = two_times_two(digit)
    if str(m * m)[0] == str(m)[0] and str(m*m)[-1] == str(m*m)[-2]:
        if str((m * m))[1] and str((m * m))[2] and str(m*m)[-1] not in list(str(m)):
            if str(m)[0] != str(str(m)[1]):
                ans.append(m)
print('answer:',set(ans))

ans = {138}  #收敛于此

print([i*i for i in ans])

# Brilliant solution
import itertools
digits = '0123456789'

# All possible combinations of 3 different digits from 0 to 9
for combination in itertools.permutations(digits, 3):
    t, w, o = combination  # Assign characters
    two = t + w + o  # Makes the word
    two_int = int(two)  # Treats it as a number
    three_int = two_int * two_int  # Calculates three
    three = str(three_int)  # Treats it as a word

    # We now have every possible two and three. Let's check which is the valid one:
    if three_int > 10000 and three_int < 100000 and two[0] == three[0] and three[3] == three[4] and three[0] != three[1] and three[1] != three[2] and two[2]!=three[4] and two[2] != three[2]:
            # Now show me what's left:
            print(f'Two: {two}')
            print(f'Three: {three}')
            print(f'H: {three[1]}')
'''

def two_times_two(digit):  # not trigger condition
    st,nd = 10**(digit-1),10**digit,
    x = random.randint(st, nd)
    if str(x)[0] != str(x)[0] != str(x)[0]:
        print(x)
print(two_times_two(digit))

'''

for num in range(100, 1000):
    result = num ** 2  # TWO * TWO = THREE
    if len(str(result)) != 5:  # To check if the result is a five digits number
        continue
    T, W, O = map(int, str(num))  # TWO -> T, W, O
    _T, _H, _R, _E, __E = map(int, str(result))  # THREE -> T, H, R, E, E
    if len({T, W, O, _H, _R, _E}) < 6:  # any duplicate ?
        continue
    if T != _T or _E != __E:    # T should be equal to _T, _E should be equal to __E
        continue
    print(f'{num} * {num} = {result}')