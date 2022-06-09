# https://brilliant.org/daily-problems/even-plates/
'''
Garry, Harry, and Larry just bought their first cars! Each of the
proud triplets
is about to register his new vehicle. In Brilliantia where they
live, license plates consist of numbers alone that are assigned
at random.

What is the probability that at least two brothers get a plate
with an even number?
'''

plate = [i for i in range(10)]

#Garry, Harry, and Larry

cunt,cuntall = 0,0
for g in plate:
    for h in plate:
        for l in plate:
            cuntall += 1
            if sum([i%2==0 for i in (g,h,l)]) >= 2:
                cunt += 1
print(cunt,cuntall,cunt/cuntall)