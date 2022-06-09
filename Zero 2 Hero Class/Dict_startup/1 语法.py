'''
Python 有一组可以在字典上使用的内建方法。

方法	描述
clear()	删除字典中的所有元素
copy()	返回字典的副本
fromkeys()	返回拥有指定键和值的字典
get()	返回指定键的值
items()	返回包含每个键值对的元组的列表
keys()	返回包含字典键的列表
pop()	删除拥有指定键的元素
popitem()	删除最后插入的键值对
setdefault()	返回指定键的值。如果该键不存在，则插入具有指定值的键。
update()	使用指定的键值对字典进行更新
values()	返回字典中所有值的列表
'''
#Python 有一组可以在字典上使用的内建方法。

#方法	描述
import string
key = list(range(26))
value = string.ascii_lowercase
alpha = dict(zip(key,value))

#clear()	删除字典中的所有元素
print(alpha.clear())

#copy()	返回字典的副本
print(alpha.copy())

#fromkeys()	返回拥有指定键和值的字典
#get()	返回指定键的值
#items()	返回包含每个键值对的元组的列表
#keys()	返回包含字典键的列表
#pop()	删除拥有指定键的元素
#popitem()	删除最后插入的键值对
#setdefault()	返回指定键的值。如果该键不存在，则插入具有指定值的键。
#update()	使用指定的键值对字典进行更新
#values()	返回字典中所有值的列表