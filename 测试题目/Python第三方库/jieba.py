'''
道题用的cut方法教材上没有讲，教材上用的是lcut方法，
直接返回列表类型，通过查阅资料，了解了cut方法返回的是迭代器类型，需要转换为列表类型，否则无法输出
'''
import jieba
s = "Python是最有意思的编程语言"
l = jieba.lcut(s)
l = list(l)
print(l)

s="Python是最有意思的编程语言"
l=jieba.cut(s)#
print(type(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
l=list(l)
print(l)