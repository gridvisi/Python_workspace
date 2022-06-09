import numpy as np
vec = []

f = open('a.txt', encoding='utf-8')
while True:
    content = f.readline()
    if content == '':
        break
    content = content.strip().split()
    content = content[:]#复制列表
    content = [float(i) for i in content]#将content中的元素转为浮点数
    vec.append(content)
    for l in vec[:]:#遍历嵌套列表
        if len(l) != 100:#找到元素不足100的列表
            l.insert(100,10000)#在索引为100的位置插入想要插入的元素10000
    # print(vec,len(vec))

vec = np.array(vec, dtype=np.float32)#将列表转换为数组

#https://blog.csdn.net/qq_27492735/article/details/82254698