'''
https://brilliant.org/daily-problems/cryptogram-alpha/

A*B*100 + A*L*10 + A*A + B*B*100 + B*L*10 + B*A =
101*A*B + 10*(A+B)*L + A*A + 100*B*B

101*A*B + 10*(A+B)*L + A*A + 100*B*B = 10000*A + 1000*L + 100*P + 10*H + A
A = {1,5,6}

(10000-101*B)*A + (1000 - 10*A - 10*B)*L + 100*(P - B*B) + 10*H  + A*(1-A)  = 0

if A == 1:
    (10000-101*B) + (1000 - 10 - 10*B)*L + 100*(P - B*B) + 10*H  + 0 = 0
    return 10000-101*B > 9091,
       (1000 - 10 - 10*B)*L > 900*L
       So that 100*(P - B*B) < 0, 100 * (1 - 81) = -8000
       10*H < 90

       Conclusion:
       9091 + 900*L - 8000 + 90  = O
       1091 + 802*L - 16*A = 0

elif A == 5
    return 10000-100*B > 9091*5,
       (1000 - 10*5 - 10*B)*L > 860*L
       So that 100*(P - B*B) < 0, 100 * (1 - 81) = -8000
       10*H < 90
       9091*5 + 802*L - 8000 + 90 > O

*A + (1000 - 10*A - 10*B)*L + 100*(P - B*B) + 10*H  + A - A*A = 0
'''

from itertools import permutations

for A, B, H, L, P in permutations("0123456789", 5):
    BLA = int(B + L + A)
    BA = int(B + A)
    ALPHA = int(A + L + P + H + A)
    if BLA * BA == ALPHA:
        print(f"{BLA} x {BA} = {ALPHA}; H = {H}")

for b in range (1, 10) :
        for l in range(10) :
            for a in range(10) :
                x = b * 100 + l * 10 + a
                y = b * 10 + a
                z = x * y
                if len(str(z)) == 5 and z % 10 == a and (z //1000)%10 == l and (z//10000)%10 == a:
                    print(x, y, z)

# Output:
# 785 75 58875
# 795 75 59625
# As you can see first one can't be the answer as it has two 8's in place of L
# and P which should be different digits. Therefore, 59625 is the answer with H=2


from itertools import permutations

for perm in permutations(range(10), 5):
    a,b,l,p,h = perm
    bla = 100*b + 10*l + a
    ba = 10*b + a
    alpha = 10000*a + 1000*l + 100*p + 10*h + a
    if bla*ba == alpha:
        print('{} * {} = {}'.format(bla,ba,alpha))

# Output:
# 795 * 75 = 59625