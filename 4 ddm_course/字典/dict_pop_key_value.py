'''
注意：python中字典的键是不能直接修改，因为键是hash。

间接修改键的key值方法

第一种(推荐)：

dict={'a':1, 'b':2}

dict["c"] = dict.pop("a")
第二种方法：

dict={'a':1, 'b':2}

dict.update({'c':dict.pop("a")})
第三种方法：

dict={'a':1, 'b':2}

dict['c']=dict['a']

del dict['a']
 
————————————————
版权声明：本文为CSDN博主「风一样汉子」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/a1007720052/article/details/81542134
'''