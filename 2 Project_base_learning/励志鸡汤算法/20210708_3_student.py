num = [i for i in range(1,27)]
#alpha = ['a....z']

import string
alpha = string.ascii_lowercase
zidian = dict(zip(alpha,num))
print(sum([zidian[i] for i in 'cuijiarui']))
lucky = sum([zidian[i] for i in 'cuijiarui'])
factor_cui = [i for i in range(1,lucky+1) if lucky%i ==0]
# 短除法的实现
lucky = 147
factor_fei = [i for i in range(1,lucky+1) if lucky%i ==0]
lucky = 146
factor_xing = [i for i in range(1,lucky+1) if lucky%i ==0]
print(factor_cui,factor_fei,factor_xing)

lucky = sum([zidian[i] for i in 'lizonglin'])
factor_zong = [i for i in range(1,lucky+1) if lucky%i ==0]
print('zong:',factor_zong)
print('common:',set(factor_cui) & set(factor_fei) & set(factor_xing) & set(factor_zong))

#set()







alphabet_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'r': 18, 's': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
alphabet='ABCDEFGHIJKLMNOPQrsTUVWXYZ'
alphabet_dict={}
for i in range(len(alphabet)):
    alphabet_dict[alphabet[i]]=i+1
    print(alphabet_dict)

def magic_word(word):
    s = 0
    for i,x in enumerate(word.lower()):
        s += alphabet_dict.get(x)
    return word + ' 的幸运总数是：', + s
#for w in word_total:
#    print(magic_word(w))


name = ['zhangsan','lisi','wangwu']
name_cn = ['张三','李四','王五']

name = ['cathy','feifei','mike']
name_cn = ['崔','菲菲','天宝']

print(dict(zip(name_cn,name)))
namelist = dict(zip(name_cn,name))
print(namelist['菲菲'])

