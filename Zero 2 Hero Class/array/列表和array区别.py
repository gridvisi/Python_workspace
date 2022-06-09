'''
1. 列表list与数组array的定义：

列表是由一系列按特定顺序排列的元素组成，可以将任何东西加入列表中，
其中的元素之间没有任何关系；

Python中的列表(list)用于顺序存储结构。它可以方便、高效的的添加删除
元素，并且列表中的元素可以是多种类型。

数组也就是一个同一类型的数据的有限集合。

2. 列表list与数组array的相同点：

    a. 都可以根据索引来取其中的元素；

3. 列表list与数组array的不同点：

    a.列表list中的元素的数据类型可以不一样。数组array里的元素的数据类型必须一样；

    b.列表list不可以进行数学四则运算，数组array可以进行数学四则运算；

    c.相对于array，列表会使用更多的存储空间。

例子：（从例子中可以看出list 和array的相同与不同之处）
'''

import numpy as np
lis1=[1,2,3,4]  #lis1是列表类型
a = np.array([1,2,3,4])  #a是数组类型

#从下面print可以看出 list和array都可以根据索引来操作；
print("list",lis1,lis1[0],'\n','array',a,a[0])

#从下面print可以看出list的+法运算是列表长度的增删，与数学计算无关；
#而array的＋法运算是真正的数学四则运算；
print("list+list",lis1+lis1,'\n','array+array',a+a)