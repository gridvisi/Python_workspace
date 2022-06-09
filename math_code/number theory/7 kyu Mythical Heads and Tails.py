'''
https://www.codewars.com/kata/5751aa92f2dac7695d000fb0/train/python
The formidable "Orthus" is a 2 headed dog with 1 tail.
The mighty "Hydra" has 5 heads and 1 tail.

Before Hercules goes in, he asks you "How many of each beast am I up against!?".

You know the total number of heads and the total number of tails, that's the dangerous parts, right?
But you didn't consider how many of each beast.

test.describe("Example Tests")

test.assert_equals(beasts(123, 39), [24, 15])
test.assert_equals(beasts(371, 88), [23, 65])
test.assert_equals(beasts(24, 12), [12, 0])
test.assert_equals(beasts(113, 37), [24, 13])
test.assert_equals(beasts(635, 181), [90, 91])
'''

def beasts(heads, tails):
    headtail = {'orthus':(2,1),'hydra':(5,1)}

    for tail in range(tails+1):
        print(tail, tails-tail)
        if tail * headtail['orthus'][0] + (tails-tail)*headtail['hydra'][0]==heads:
            return [tail, tails-tail]

heads, tails = [123, 39]
heads, tails = [24, 12]

print(beasts(heads, tails))

#1st solution
def beasts(heads, tails):
    orthus = (5 * tails - heads) / 3
    hydra = tails - orthus
    return [orthus, hydra] if orthus >= 0 and hydra >= 0 else 'No solutions'

