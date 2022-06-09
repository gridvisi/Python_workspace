
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))

x = iter([1, 2, 3, 4])
print(next(x))
print(next(x))

print(list(map(len, ['abc', 'de', 'fghi'])))

print(list(map(sum, zip([1, 2, 3], [4, 5, 6]))))


def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
naive_grouper(nums, 2)
print(naive_grouper(nums, 2))
'''
$ time -f "Memory used (kB): %M\nUser time (seconds): %U" python3 naive.py
Memory used (kB): 4551872
User time (seconds): 11.04
Note: On Ubuntu, you may need to run /usr/bin/time instead of time for the above example to work.

The list and tuple implementation in naive_grouper() requires approximately 4.5GB of memory to process range(100000000). Working with iterators drastically improves this situation. Consider the following:

'''

def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iters = [iter(nums)] * 2
print(iters)
print(list(id(itr) for itr in iters))  # IDs are the same.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(better_grouper(nums, 2)))

import itertools as it

x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c']
print(list(zip(x, y)))


import itertools as it


def grouper(inputs, n, fillvalue=None):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=fillvalue)
#Now you get a better result:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(grouper(nums, 4)))

'''
Here’s a common interview-style problem:
You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills. How many ways can you make change for a $100 dollar bill?
To “brute force” this problem, you just start listing off the ways there are to choose one bill from your wallet, check whether any of these makes change for $100, then list the ways to pick two bills from your wallet, check again, and so on and so forth.
But you are a programmer, so naturally you want to automate this process.
First, create a list of the bills you have in your wallet:
'''
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
print(list(it.combinations(bills, 3)))
#[(20, 20, 20), (20, 20, 10), (20, 20, 10),  ]
#To solve the problem, you can loop over the positive integers from 1 to len(bills),
# then check which combinations of each size add up to $100:

makes_100 = []
for n in range(1, len(bills) + 1):
    for combination in it.combinations(bills, n):
        if sum(combination) == 100:
            makes_100.append(combination)