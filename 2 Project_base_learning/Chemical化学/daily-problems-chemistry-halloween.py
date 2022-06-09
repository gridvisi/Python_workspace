'''
https://brilliant.org/daily-problems/chemistry-halloween/
 科学和工程

糖瘾的化学反应

当你大口大口地吃糖时，你不应该感到太过内疚--毕竟，你的身体需要糖来运行，就像大多数汽车需要汽油。

你的身体不是在燃烧汽油，而是将糖燃烧成水、二氧化碳和能量来做有用的事情。但只要看一眼所涉及的分子就会知道缺少了什么：糖在没有帮助的情况下无法燃烧。

这就是，一个甜美的葡萄糖分子（最简单的糖）。一个完整的葡萄糖分子包括六个碳原子、十二个氢原子和六个氧原子。

![image](https://upload-images.jianshu.io/upload_images/184712-5990acbfead50675?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在吃完火星棒和焦糖苹果的早餐后，你的细胞将葡萄糖分解成大量的二氧化碳。你可以呼出CO2 和水

![image](https://upload-images.jianshu.io/upload_images/184712-c040fdd5ba9ac5a2?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这种化学反应也释放出大量的能量，细胞捕捉这些能量来做它们的工作（如移动肌肉、消化食物和思考每日挑战）。

但我们在这里遇到了一个问题。葡萄糖分子中氧原子与碳原子的比例为1:1，但二氧化碳的比例为2:1，如果产生水，那就需要更多氧原子。这就是为什么你需要呼吸空气来燃烧所有的糖--空气中充满了氧分子，其形式是 

![image](https://upload-images.jianshu.io/upload_images/184712-ca2a2da7f9078a50?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

我们在这里得到了正确的原材料，但需要一些算术来确保我们能做出平衡的化学反应。毕竟，原子不能被创造、破坏或转化--我们在做化学，而不是炼金术。

![image](https://upload-images.jianshu.io/upload_images/184712-253003a92be9fcf4?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

最简单的方法是先**平衡右侧的碳原子和氢原子**，使其与葡萄糖相平衡：碳只存在于CO2二氧化碳中，H氢原子只存在于H2o水中。

 每种物质都需要 6 个分子才能等于一个葡萄糖分子中的碳原子和氢原子的数量。

x O2 + C6H12O6 -> 6 H2O + 6 CO2

现在只有一个未知量。**"你需要多少额外的氧气？"** 

如果你把右边的氧元素加起来，你会得到18。这意味着你还需要6个O2 分子来平衡这个反应。

![image](https://upload-images.jianshu.io/upload_images/184712-6e08f954559fceb0?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**今天的挑战**

如果你调查典型糖果的分子组成，你不太可能找到很多葡萄糖（如果有的话）。

在糖果的制作过程中，葡萄糖和蔗糖等糖类在一个叫做焦糖化的过程中转化为更硬、更黑、味道更复杂的分子，如焦糖酸。![image](https://upload-images.jianshu.io/upload_images/184712-8a75b43169a34143?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

但你也可以烧掉一个焦糖分子。  你需要有多少个氧分子{O2}完成化学反应？ 选项如下：

1.  **18**

2.  **24**

3.  **36**

4.  这个化学反应不能被平衡。

解题思路：
左边碳和氢比例是 2：3，右边也遵守此比例

​'''

left_1 = {"O":2}
left_2 = {"C":24,"H":36,"O":18}

right_1 = {"H":2,"O":1}
right_2 = {"C":1,"O":2}

# 字符串表达
O2 = "OO"
sugar = "C"*24+"H"*36+"O"*18

water = "HHO"
C2 = "COO"

#碳只存在于sugar和C2，所以，sugar : C2 = 1: 24
#氢只存在于sugar和water, 所以，sugar : water = 18:1
# sugar初始值为s = 1，循环+1比较左右两边氧分子平衡过程


from collections import Counter
s = 1 #left_2的数量

left_O = s * sugar.count("O")
right_O = 18* s *water.count('O') + 24*s*C2.count('O')
print(left_O,right_O)
while True:

    if (right_O - left_O) % 2 == 0:
        ans = (right_O - left_O)//2
        lft = ans*O2 + s*sugar
        rgt = 18*s*water + 24*C2

        if Counter(lft) == Counter(rgt):
            print("需要氧分子数量：",ans)
        break
    else:
        s += 1

