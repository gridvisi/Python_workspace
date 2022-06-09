'''
————————————————
版权声明：本文为CSDN博主「zglhs1008」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_33347071/article/details/86614883
'''

#第一步建立网格(横坐标表示[0,c]整数背包承重):(n+1)*(c+1)
def bag(n,c,w,p):
    res=[[0 for j in range(c+1)]for i in range(n+1)]
    for j in range(c+1):
        #第0行全部赋值为0，物品编号从1开始.为了下面赋值方便
        res[0][j]=0
    for i in range(1 , n+1):
        for j in range(1 ,c+1):
           # print(res[i-1][j])
            res[i][j]=res[i-1][j]
            #生成了n*c有效矩阵，以下公式w[i-1],p[i-1]代表从第一个元素w[0],p[0]开始取。
            if(j>=w[i-1]) and res[i-1][j-w[i-1]]+p[i-1]>res[i][j]:
                res[i][j]=res[i-1][j-w[i-1]]+p[i-1]
              #  print("i=%d;j=%d;p[i-1]=%d;res[i][j]=%d" %(i,j,p[i-1],res[i][j]))
    return res
#打印最大价值和要选择的商品
def show(n,c,w,res):
    print('最大价值为:',res[n][c])
    rr= res[n][c] - p[n - 1]
    print ("第%d个" %(n-1))
    flag = False
    while rr !=0:
        for i in range(1,n+1):
            for j in range(1,n+1):
                if res[i][j] == rr:
                    print("第%d个" %(i-1))
                    rr = res[i][j] -p[i-1]
                    flag = True
            if flag:
                flag = False
                break


if __name__=='__main__':
    #物品件数
    n=3
    #背包的最大承重
    c=4
    #各个物品的重量
    w=[4,3,1]
    #各个物品的价值
    p=[3000,2000,1500]
    res=bag(n,c,w,p)
    show(n,c,w,res)

'''


from pyecharts import options as opts
from pyecharts.charts import Funnel, Page
from random import randint

def funnel_base() -> Funnel:
  c = (
    Funnel()
    .add("豪车", [list(z) for z in zip(['宝马', '法拉利', '奔驰', '奥迪', '大众', '丰田', '特斯拉'],
                 [randint(1, 20) for _ in range(7)])])
    .set_global_opts(title_opts=opts.TitleOpts(title="豪车漏斗图"))
  )
  return c
funnel_base().render('./img/car_fnnel.html')
————————————————
版权声明：本文为CSDN博主「不想当码农的程序员」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/chenjianandiyi/article/details/103766263
'''

# 动态规划
import numpy as np

# 定义重量
weight = {}
weight["water"] = 3
weight["book"] = 1
weight["food"] = 2
weight["jacket"] = 2
weight["camera"] = 1
# 定义价值
worth = {}
worth["water"] = 10
worth["book"] = 3
worth["food"] = 9
worth["jacket"] = 5
worth["camera"] = 6

# 存放行标对应的物品名:
table_name = {}
table_name[0] = "water"
table_name[1] = "book"
table_name[2] = "food"
table_name[3] = "jacket"
table_name[4] = "camera"

# 创建矩阵,用来保存价值表
table = np.zeros((len(weight), 6))

# 创建矩阵，用来保存每个单元格中的价值是如何得到的（物品名）
table_class = np.zeros((len(weight), 6), dtype=np.dtype((np.str_, 500)))

for i in range(0, len(weight)):
    for j in range(0, 6):
        # 获取重量
        this_weight = weight[table_name[i]]
        # 获得价值
        this_worth = worth[table_name[i]]
        # 获取上一个单元格 (i-1,j)的值
        if (i > 0):
            before_worth = table[i - 1, j]
            # 获取（i-1,j-重量）
            temp = 0
            if (this_weight <= j):
                temp = table[i - 1, j - this_weight]
            # (i-1,j-this_weight)+求当前商品价值
            # 判断this_worth能不能用，即重量有没有超标，如果重量超标了是不能加的
            synthesize_worth = 0
            if (this_weight - 1 <= j):
                synthesize_worth = this_worth + temp
            # 与上一个单元格比较,哪个大写入哪个
            if (synthesize_worth > before_worth):
                table[i, j] = synthesize_worth
                if (temp == 0):
                    # 他自己就超过了
                    table_class[i][j] = table_name[i]
                else:
                    # 他自己和(i-1,j-this_weight)
                    table_class[i][j] = table_name[i] + "," + table_class[i - 1][j - this_weight]
            else:
                table[i, j] = before_worth
                table_class[i][j] = table_class[i - 1][j]
        else:
            # 没有（i-1,j）那更没有(i-1,j-重量),就等于当前商品价值,或者重量不够，是0
            if (this_weight - 1 <= j):
                table[i, j] = this_worth
                table_class[i][j] = table_name[i]
print(table)

print("--------------------------------------")

print(table_class)
#最终结果：



'''
最终结果：如图红框部分可知：当背包重量为6kg是，选择camera, food, water可使价值最大
版权声明：本文为CSDN博主「入眸幻灭」的原创文章，遵循
版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / wcandy001 / article / details / 79714010
'''

'''
1、找零钱问题
     有数组penny，penny中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个整数aim(小于等于1000)代表要找的钱数，求换钱有多少种方法。
给定数组penny及它的大小(小于等于50)，同时给定一个整数aim，请返回有多少种方法可以凑成aim。
测试样例：
[1,2,4],3,3
返回：2

解析：设dp[n][m]为使用前n中货币凑成的m的种数，那么就会有两种情况：

             使用第n种货币：dp[n-1][m]+dp[n-1][m-peney[n]]

              不用第n种货币：dp[n-1][m]，为什么不使用第n种货币呢，因为penney[n]>m。

        这样就可以求出当m>=penney[n]时 dp[n][m] = dp[n-1][m]+dp[n][m-peney[n]]，否则，dp[n][m] = dp[n-1][m]
————————————————
版权声明：本文为CSDN博主「别再想更好的办法」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_37763204/article/details/79394397

2、走方格问题
      有一个矩阵map，它每个格子有一个权值。从左上角的格子开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，返回所有的路径中最小的路径和。
给定一个矩阵map及它的行数n和列数m，请返回最小路径和。保证行列数均小于等于100.
测试样例：
[[1,2,3],[1,1,1]],2,3
返回：4

解析：设dp[n][m]为走到n*m位置的路径长度，那么显而易见dp[n][m] = min(dp[n-1][m],dp[n][m-1]);
————————————————
版权声明：本文为CSDN博主「别再想更好的办法」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_37763204/article/details/79394397

3、走台阶问题
    有n级台阶，一个人每次上一级或者两级，问有多少种走完n级台阶的方法。为了防止溢出，请将结果Mod 1000000007
给定一个正整数int n，请返回一个数，代表上楼的方式数。保证n小于等于100000。
测试样例：
1
返回：1

4、最长公共序列数
     给定两个字符串A和B，返回两个字符串的最长公共子序列的长度。例如，A="1A2C3D4B56”，B="B1D23CA45B6A”，”123456"或者"12C4B6"都是最长公共子序列。
给定两个字符串A和B，同时给定两个串的长度n和m，请返回最长公共子序列的长度。保证两串长度均小于等于300。
测试样例：
"1A2C3D4B56",10,"B1D23CA45B6A",12
返回：6

解析：设dp[n][m] ，为A的前n个字符与B的前m个字符的公共序列长度，则当A[n]==B[m]的时候，dp[i][j] = max(dp[i-1][j-1]+1,dp[i-1][j],dp[i][j-1])，否则，dp[i][j] = Math.max(dp[i-1][j],dp[i][j-1]);

代码如下：
————————————————
版权声明：本文为CSDN博主「别再想更好的办法」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_37763204/article/details/79394397
'''

