'''
https://brilliant.org/daily-problems/pigeonhole-2/
'''

books = 8
sameset = 5
def persons(books,sameset):
    comb = sum([i for i in range(books)])
    return comb * sameset
print(persons(books,sameset))
