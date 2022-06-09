'''
There are some roses in a garden and some bees are hovering over them.
If every bee lands on a different rose, one of them won't get a rose.
If every two bees share one rose, then there will be one rose left without any bees.
Which of the following is a possible number of roses and the number of bees in the garden?
'''

def bees_rose():
    for bee in range(1,100):
        for rose in range(1, 100):
            if bee - rose == 1 and rose - (bee / 2) == 1:
                return bee,rose
print(bees_rose())