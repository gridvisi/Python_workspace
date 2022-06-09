'''
Re：递归 函数参数

n个正整数之和等于100，列出包含所有的数字组合。

'''

solutions = set()

def calc(n, dogs, last):
    if n == 6:

        if sum(dogs) == 100:
            d = sorted(dogs, reverse=True)

            solutions.add((tuple(d), (d[1] + d[2]) / 2))

        print(n)

        #print(solutions,n,end=',',flush=10)

        return

    # 由于此处条件判断的条件是n == 6，

    # sum(dogs) 不等于100时,return 停在当前状态

    else:

        print(n)

        for i in range(last, 100):

            dogs[n] = i

            if sum(dogs[:n + 1]) > 100:

                return

            else:

                calc(n + 1, dogs, i)

#n, dogs, last = 1,[17, 17, 4, 20, 1, 20, 17, 6, 18, 17, 12, 11, 10, 7, 19, 6, 16, 5, 6, 21, 22, 21, 10, 1, 10, 12, 5, 10, 6, 18],1


print(calc(n, dogs, last))

