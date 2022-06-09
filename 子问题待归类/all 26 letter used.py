'''
“如果蜜蜂从地球上消失，人类将只能再存活4年。没有蜜蜂，没有授粉，没有植物，没有动物，也就没有人类。”— 阿尔伯特 爱因斯坦

"If All the bees die on earth, we would die due to not enough food sustain the living"  --- Albert Einstein

the quick brown fox jumps over a lazy dog
那条跑得很快的棕色狐狸跳过了一条懒狗

str,name = "A live son", "Allison"
str,name = "Just enough nice friends","Jennifer"
str,name = "pippippi","Pippi"
str,name = "Across the rivers","chris"
'''

str = 'abcdefghijklmnopqrstuvwxyz'
name = 'the quick brown fox jumps over a lazy dog'

name = " Albert Einstein"
str = "If All the bees die on earth, we would die due to not enough food sustain the living"

#str,name = "A crew that boards the ship", "chris"

def name_in_str(str, name):
    it = iter(str.lower())
    return all(c in it for c in name.lower())
print(name_in_str(str, name))

tg = 'the quick brown fox jumps over a lazy dg'  # 呵呵哒
tg = 'the uick brown fox jumps over a lazy dog'  # 呵呵哒
def alphabet_check_1(tg):    # 这段程序错误在什么地方？
    res = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    for e in alphabet:
        print(e)
        if e not in tg:
            print(e)
            res.append(e)
            return 'check_1 find tg 里没有出现的字母是', res
        return 'check_1 find tg 包含了所有26个字母'
print(alphabet_check_1(tg))

def alphabet_check(tg):    # 这段程序如何纠正上面的错误？
    res = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    for e in alphabet:
        #print(e)
        if e in tg:
            pass
        else:res.append(e)
    print(res)
    if len(res) == 0:
        return 'check find tg 包含了所有26个字母'
    return 'check find tg 里没有出现的字母是', ''.join(res)

print(alphabet_check(tg))

alphabet='ABCDEFGHIJKLMNOPQrsTUVWXYZ'
alphabet_dict={}
for i in range(len(alphabet)):
    alphabet_dict[alphabet[i]]=i+1
print(alphabet_dict)

def magic_word(word):
    s,s_list = 0,[]

    for i,x in enumerate(word.upper()):
        if x in alphabet:    # why should we add this line?
            s_list.append(alphabet_dict.get(x))
            s += alphabet_dict.get(x)
            s_list.append(s)
    return word + ' 的幸运总数是：', + s,s_list

word = 'eric'
print(magic_word(word))

word = 'lijing'
print(magic_word(word))

word = 'lijie'
print(magic_word(word))

word = 'mcree'
print(magic_word(word))

word = 'zhangmin'
print(magic_word(word))

word = 'zhangzimu'
print(magic_word(word))

word = 'lizonglin'
print(magic_word(word))

word = 'Albert Einstein'
print(magic_word(word))
'''
('eric 的幸运总数是：', 17, [5, 5, 9, 14, 3, 17])
('lijing 的幸运总数是：', 61, [12, 12, 9, 21, 10, 31, 9, 40, 14, 54, 7, 61])
第18个质数。前一个为59、下一个为67。
第7对孪生素数之一（59，61）
十进制中，61既不是右可截短质数，也不是左可截短质数。
此数字虽然是自然质数，但不是高斯质数。前一个有此性质的自然质数是53、下一个是73。（OEIS中的数列A002313） [1] 
其第一象限之高斯质数的整数分解为 -i×(5+6i)×(6+5i)。
立方素数
第9个梅森质数， 2⁶¹-1
第47个亏数，真因数和为1，亏度为60。前一个为59、下一个为62。
第40个不寻常数，大于平方根的质因数为61。前一个为59、下一个为62。
第38个无平方数因数的数。前一个为59、下一个为62。
第29个十进制的等数位数。前一个为59、下一个为64。
两个连续平方数之和：5²+6²
基思数 图示2是否存在无穷多个基思数仍然是个有待论证的问题，如图示2以下的基思数只有71个，比素数还稀有
中心正方形数、中心六边形数和中心十边形数
五角星数
1,318,820,881²= 1,739,288,516,161,616,161
-61是第6个欧拉数


('attitude 的幸运总数是：', 100)
('love 的幸运总数是：', 54)
('Knowledge 的幸运总数是：', 96)
('Hardwork 的幸运总数是：', 98)
('Health 的幸运总数是：', 54)
('luck 的幸运总数是：', 47)
('money 的幸运总数是：', 72)
('attitude 的幸运总数是：', 100)
'''