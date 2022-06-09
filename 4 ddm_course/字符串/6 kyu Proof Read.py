'''
https://www.codewars.com/kata/583710f6b468c07ba1000017/train/python

You've just finished writing the last chapter for your novel when a virus suddenly infects
your document. It has swapped the 'i's and 'e's in 'ei' words and capitalised random letters.
Write a function which will:

a) remove the spelling errors in 'ei' words. (Example of 'ei' words: their, caffeine,
deceive, weight)

b) only capitalise the first letter of each sentence. Make sure the rest of the
sentence is in lower case.

Example: He haD iEght ShOTs of CAffIEne. --> He had eight shots of caffeine.
'''
# key point : re find and replace

import re
def proofread(string):
    #ans = compile(r'\w+')
    #sl = re.findall('ie',string.lower().capitalize())
    #st = list(map(lambda x:x.lower().capitalize(),string.split('. ')))
    st = list(map(lambda x: x.lower(), string.split('. ')))
    print(st)
    sl = re.sub(r'ie','ei','. '.join(st))
    return '. '.join(list(map(lambda x: x.capitalize(), sl.split('. '))))

# 先替换再解决‘。’每一句的首字母大写
string = "Protien intAkE miGHt afFect aNy pOteNtIaL wieght LOSs."  # dot at end
string = "The neighbour's ceiling fell on his head. the weight of it crushed him to the ground."
string = 'Feeiaxhmei. Ieeixmnfdkevg efsc. Yncjlmth siyjei shrlueic. Wn nn. Didhznupcs.'
#蛋白质的摄入可能会影响任何潜在的体重减轻。
#answer = "Protein intake might affect any potential weight loss."

#1st solution
def proofread(s):
    return '. '.join(i.lower().replace('ie', 'ei').capitalize() for i in s.split('. '))

#2nd solution
import re

def proofread(text):
    return re.sub("(\w[^.]*)", lambda m: m.group(1).capitalize(), text.lower().replace("ie", "ei"))


# Non re.complile solutiion

def proofread(string):
    if not string:
        return string;
    s = string.lower();
    s = s.replace("ie", "ei");
    s = s.replace(s[0], s[0].upper(), 1);
    print(s)
    s = s.split();
    for i, word in enumerate(s):
        if '.' in word and i != len(s) - 1:
            s[i + 1] = s[i + 1].replace(s[i + 1][0], s[i + 1][0].upper(), 1);
    s = " ".join(s);
    print(s)
    return s

#5th solution
def proofread(s):
    return ". ".join([x.capitalize() for x in s.lower().replace('ie', 'ei').split('. ')])

#6th solution
def proofread(string):
    ans = string.lower()
    ans = ans.replace('ie', 'ei')
    ans = ''.join(ans).split('. ')

    for i in range(0, len(ans)):
        ans[i] = ans[i].capitalize()
    return '. '.join(ans)

'''
"The neighbour's ceiling fell on his head. the weight of it crushed him to the ground." should equal 
"The neighbour's ceiling fell on his head. The weight of it crushed him to the ground."

'Neither of the fencers wanted to forfeit the match. they both expected to seize victory.' should equal 
'Neither of the fencers wanted to forfeit the match. They both expected to seize victory.'

'She lifted her veil. the sheik looked at her expectantly' should equal 
'She lifted her veil. The sheik looked at her expectantly'

'Peter was not sure of what he was seeing. he had to rein in his shock.' should equal 
'Peter was not sure of what he was seeing. He had to rein in his shock.'

It should work for random inputs too: 
'Feeiaxhmei. Ieeixmnfdkevg efsc. Yncjlmth siyjei shrlueic. Wn nn. Didhznupcs.' should equal 
'Feeiaxhmei. Eieixmnfdkevg efsc. Yncjlmth siyjei shrlueic. Wn nn. Didhznupcs.'
'''
print(proofread(string))

'''
# list = re.findall(regex,string,flag)

import re
string0 = 'abcdefgh'
list0 = re.findall('ab',string0)
print(list0)
# ['ab']


string1 = 'abcdefghab'
list1 = re.findall('ab',string1)
print(list1)
# ['ab', 'ab']


string2 = 'abcdefghab'
list2 = re.findall('(ab)cd',string2)
print(list2)
# ['ab']


string3 = 'abcdefghabcd'
list3 = re.findall('(ab)cd',string3)
print(list3)
# ['ab', 'ab'] 一个字组匹配到两处 只显示子组内容


string4 = 'abcdefghabcd'
list4 = re.findall('(ab)cd(ef)',string4)
print(list4)
# [('ab', 'ef')]

string5 = 'abcdefghabcd'
list5 = re.findall('((ab)cd(ef))',string5)
print(list5)
# [('abcdef', 'ab', 'ef')]  整体匹配到1处，有3个子组

string6 = 'abcdefghabcdef'
list6 = re.findall('(ab)cd(ef)',string6)
print(list6)
# [('ab', 'ef'), ('ab', 'ef')]


# 注意：
# 1.用findall来匹配时，如果正则表达式中没有子组，则返回的列表中的每一项都是匹配到的字符串，匹配到几处就有几个
#
#
# 2.如果正则表达式中含有一个子组，
# 则返回的列表中的各项是匹配到的字符串的子组内容，整体匹配到几处就有几个子组内容
#
#
# 3.如果正则表达式中含有多个子组
# 则返回含有元组的列表
# 正则字符串整体匹配到几处就有几个元组
# 每个元组中的内容是 正则表达式每个子组匹配到的内容
'''