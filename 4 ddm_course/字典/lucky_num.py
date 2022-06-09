import string
s = string.ascii_letters
print(s)


#alphabet='ABCDEFGHIJKLMNOPQrsTUVWXYZ'
alphabet = s[s.index('z') + 1:]
alphabet = list(alphabet)
print(alphabet)
#1 逐个字母取出
#2 每个字母放入字典作为key 键值 查询对应的值vaule
#3 每个字母查到value sum

value_num = [i for i in range(1,len(alphabet)+1)]
print('value:',value_num)


alphabet_dict = dict(zip(alphabet,value_num))
print(alphabet_dict)


for i in range(len(alphabet)):
    alphabet_dict[alphabet[i]] = i+1
#print(alphabet_dict)

word = 'love'
#word = 'LOve'
word = 'Attitude'
word = '    '
def magic_word(word):
    s = 0
    for i,x in enumerate(word.upper()):
        s = s + alphabet_dict[x]
        #s += alphabet_dict.get(x)
    return word + ' 的幸运总数是：', + s

print(magic_word(word))

'''
str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写


'''
