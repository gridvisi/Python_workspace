
import heapq
grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]
print(heapq.nlargest(3, grades))
print(heapq.nsmallest(4, grades))

import heapq
stocks = {'Goog'   : 520.54,
          'FB'     : 76.45,
          'YHOO'   : 39.28,
          'AMZN'   : 306.21,
          'APPL'   : 99.76}

zip_1 = zip(stocks.values(), stocks.keys())
print(sorted(zip_1))
zip_2 = zip(stocks.keys(), stocks.values())
print(sorted(zip_2))


income = [10, 30, 75]
def double_money(x):
    return x*2
updated_income = list(map(double_money, income))
print(updated_income)


string = ' '
my_list = ['I', 'Love', 'Python']
for x in my_list:
   string = string + x
print(string)