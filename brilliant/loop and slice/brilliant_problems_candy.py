'''
https://brilliant.org/problems/candy/
Candy
Computer Science Level 1
Alice has 10 candies arranged in a row. Each of them is assigned a "yummy value":

3, \ 7, \ 5, \ 4, \ 8, \ 9, \ 6, \ 2, \ 8, \ 3.
3, 7, 5, 4, 8, 9, 6, 2, 8, 3.

Alice would prefer eating all of them, but her mother wants her to distribute 9 candies to her friends, and she can only eat the one left.

The mechanism to distribute the candies is as follows:

Pick 3 consecutive candies and give them to her friends.
Merge the other candies without changing the order.
Continue until there is only 1 candy left.
Assuming that Alice distributes the candy optimally, what is the maximum "yummy value" she can save for herself?
'''

sl = [3, 7, 5, 4, 8, 9, 6, 2, 8, 3]
# 递归 or 递推
# remove (sl[:3] + sl[-3:])
# loop til len(sl) == 4:
# comp (sl[0],sl[-1])

sl = [3, 7, 5, 4, 8, 9, 6, 2, 8, 3, 10, 8, 3, 2, 8, 3, 10, 8, 3, 23,2,12]
print(len(sl))
i = 3
ans = []
while len(sl) >= 4:
    sl = sl[3:-3]
    if len(sl) == 4 and len(sl)%3 == 1:
        print(max(sl[0],sl[-1]))
print('sl',sl)




