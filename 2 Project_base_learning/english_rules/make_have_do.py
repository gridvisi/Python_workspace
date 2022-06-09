# slice
# ['the shopping','business','dishes']
# python

def do_what(do_item):
    rules = {'do':['the shopping','business','dishes']}
    for key,value in rules.items():
        for i in value:
            if do_item in value:
                return f"{key} {do_item}"
do_item = 'business'
print(do_what(do_item))


ennamecn = {'thomas':"丁丁猫"}
ddm = {'dragonfly':["丁丁猫","蜻蜓"]}

ada,betty = ['french',10,'girl'],['chonqing',9,'boy']
print(ada[2],betty[0])



#len
#if ada[0] !=

rules = {'do': 'buiness'} #dict 字典
print(rules['do'])



def do_list(n):
    rules = {
        'take': ['a bite','notes','a picture'],
        'have': ['a holiday','a dream','a baby'],
        'make': ['money', 'a comment', 'friends'],
        'do':['the shopping', 'business', 'the dishes']
          }
    return [f"{n} {i}" for i in rules[n]]
#n = 'take','have','make','do'
n = 'take'
n = 'make'
print(do_list(n))