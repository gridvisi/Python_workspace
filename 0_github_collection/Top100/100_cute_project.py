# 链接：https://www.jianshu.com/p/d74659727d26
import langid
text1 = "I am a coder and love data mining"
text2 = "请注明作者和出处并保留声明和联系方式"

print(langid.classify(text1))
print(langid.classify(text2))

# ('en', 0.9999957874458753)
# ('zh', 1.0)

from freezegun import freeze_time
import datetime
import unittest

@freeze_time("2012-01-14")
def test():
    assert datetime.datetime.now() == datetime.datetime(2012, 1, 14)

'''
75、tqdm：强大、快速、易扩展的 Python 进度条库。我想通过下面的示例代码和效果展示图，
你会跑去给这个项目来个 Star 的
'''
from tqdm import tqdm
for i in tqdm(range(10000)):
    pass

#72、jieba：强大的 Python 分词库，拿来直接用就好。示例代码如下：
# encoding=utf-8
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))




'''
87、pudb：基于控制台的全屏 Python 可视化调试器。比 pdb 好用太多了，特性：

源码语法高亮，栈、断点、变量可见并且一直动态更新。变量展示还有很多可以定制化的功能。
基于键盘，简单高效。支持 VI 的鼠标移动。还支持 PDB 的某些命令
支持查找源代码，可以使用 m 代用 module browser 查看载入的模块
断点设置。鼠标移到某行代码，按 b，然后可以在断点窗口编辑断点
作者：python大数据分析
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


import synonyms
synonyms.seg("能量")