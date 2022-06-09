'''
https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d/train/python

Who is the killer?
Some people have been killed!
You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the day of the murders.

Task.
Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
and also a list of the names of the dead people:

['Lucas', 'Bill']
return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'

FUNDAMENTALSDICTIONARYDATA STRUCTURESLISTSOBJECTS

@test.describe("Killer")
def tests():
    @test.describe("Basic tests")
    def basic():
        test.assert_equals(killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']), 'James')
        test.assert_equals(killer({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben']), 'Megan')

2020/10/24
一男，菲菲  by 丁大喵
找到杀手为任务线索，输入格式是字典和数组表达嫌疑人名字为key，在当天见过的人员名单为value
输出则是遍历所有嫌疑人的见过的人，见过所有死者的嫌疑犯就是杀手。

一男和菲菲了解到集合set函数的使用方法，并且掌握比较两个集合的并集交集的使用
在写下代码之前，仔细梳理任务执行步骤，找到任务关键并用英文表达，最后再转为代码

老师课题提出了即兴测验：如何组织一次冬令营，选出同学们最想去的地方？
同学们想到了少数服从多数的原则：计算目的地出现的次数
也想到了所有同学提交的目的地共同选项，用set函数，所有同学理想目的地的交集


'''

#Firstly,we find the namelist who dead person met before
#secondly, we find common name in list respectively


ada_fruit = ['pear','apple','apple']
james_fruit = ['apple','pineapple','orange','pineapple']
print(set(ada_fruit) <= set(james_fruit))

print(set(ada_fruit) & set(james_fruit))
print(set(ada_fruit) | set(james_fruit))  #合并，并集 unit
print(set(ada_fruit) - set(james_fruit))

#5 < age < 200


# score > 700 OR award == True
# score > 700 AND award == True


#变量的命名规则
#a,b   lyn_age,liwang_age, name ,bottle,drink,

suspect_info, dead = {'James': ['Jacob', 'Bill', 'Lucas'],
                      'Johnny': ['David', 'Kyle', 'Lucas'],
                      'Peter': ['Lucy', 'Kyle']}, \
                     ['Lucas', 'Bill']

print('James:',suspect_info['James'])
#数组和字典遍历的区别：
for name in ['David', 'Kyle', 'Lucas']:print(name)
for key,value in suspect_info.items():
    print(key,value)


from collections import Counter

#12th solution by ericlee
def killer(suspect_info, dead):
    #names = dict(zip(dead,[]*len(dead)))
    #names = Counter(dead)
    names = {}
    print(names)
    for k,v in suspect_info.items():
        print(set(v) & set(dead))
        if set(v) & set(dead):
            names[k] = [n for n in set(v) & set(dead)]   #set(v) & set(dead)
    print(sorted([(k,v) for k,v in names.items()],key=lambda x:x[1]))
    return sorted([(k,v) for k,v in names.items()],key=lambda x:len(x[1]))[-1][0]
print('result:',killer(suspect_info, dead))

#1st solution
def killer(info, dead):
    for name, seen in info.items():
        if set(dead) <= set(seen):
            return name

# 两个列表的差集、交集、并集
print(set(suspect_info) & set(dead))
print(set(suspect_info) | set(dead))
print(set(suspect_info) - set(dead))


a_list = [1, 2, 3, 4, 5]
b_list = [1, 4, 5]
ret_list = list(set(a_list)^set(b_list))
print(ret_list)

suspect_info = {'feifei':"菲菲"}
call_number = {'114':"查号台",'110':"报警"}
call_number.update({'119':"火警"})
print(call_number)


inp = "feifei"

def hello(inp):
    return 'hello ' +'merry Xchr'+ inp

inp = 'mayi'

print(hello(inp))

