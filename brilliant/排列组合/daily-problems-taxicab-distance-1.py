'''
https://brilliant.org/daily-problems/taxicab-distance-1/

↑↑→→→
↑→↑→→
↑→→↑→
↑→→→↑
→↑↑→→
→↑→↑→
→↑→→↑
→→↑↑→
→→↑→↑
→→→↑↑
'''

from itertools import permutations

for p in sorted(tuple(set(permutations("→→→↑↑")))):
     print("".join(p))
