'''
https://www.codewars.com/kata/playing-with-toy-blocks-can-you-build-a-4x4-square/train/python
Test.it("Example Tests")
Test.assert_equals(build_square([3, 1, 3, 1, 3, 1, 3, 2]), False)
Test.assert_equals(build_square([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), True)
Test.assert_equals(build_square([3, 2, 3, 3, 3, 3, 3, 3, 4, 2, 4]), False)
Test.assert_equals(build_square([4, 3, 2, 1, 3, 1, 1, 2, 3, 1, 1]), True)
Test.assert_equals(build_square([1, 3, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1]), False)
'''
blocks = [1, 3, 2, 2, 4, 1, 1, 3, 1, 4, 2]
blocks = [1, 3, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1]
blocks = [4, 3, 2, 1, 3, 1, 1, 2, 3, 1, 1]
blocks = [3, 2, 3, 3, 3, 3, 3, 3, 4, 2, 4]
#blocks = [3, 1, 3, 1, 3, 1, 3, 2]

import math
import itertools

def build_square(blocks):
    re,side = [],int(math.sqrt(sum(blocks)))

    for i in range(len(blocks)):
        if sum(sorted(blocks)[i:]) >= side*side:
            #print(sorted(blocks)[i:])

            short_len = len(sorted(blocks)[i:])
            #print('s',short_len)

    for i in range(len(blocks),short_len,-1):
        #print(short_len)
        for sq in list(itertools.combinations(sorted(blocks), i)):
            #print(sum(sq))
            if sum(sq) == side * side:
                if sq not in re:
                    re.append(sq)
    if len(re) == 0: return False
    elif len(re) > 0:
        return re,len(re),side

print(build_square(blocks))

'''
print(int(math.sqrt(sum(blocks))))
print(list(itertools.combinations(blocks, 4)))
    side = int(math.sqrt(sum(blocks)))
    for sq in list(itertools.combinations(blocks, side)):
        print(sum(sq))
        if sum(sq) == side*side:
            print(sq)
            re.append(sq)
'''