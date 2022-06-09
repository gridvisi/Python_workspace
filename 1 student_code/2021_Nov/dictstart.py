
import translate



n = [1,2,3,4,5]
num = ["one","two","three","four","five"]

#zip(n,num)
print('zip:',list(zip(n,num))) #tuple
print("dict:",dict(zip(n,num)))
dictEnCN = dict(zip(n,num))
print(dictEnCN[6]) #[key]:value
print(dictEnCN.get(6,'None'))



#阿拉伯数字：英文
def nTonum(x=1):
    if x == 1:return "one"
    if x == 2:return "two"
x = 2
print('输出：',nTonum(x))



infect = {
            "limin":  ["yangyi","wangwu","zhaoliu"],
            "wangwu": ["maba","niushi","limin"],
            "liming":  ["yangyi","wangwu","zhaoliu"],
         }

#key:钥匙，关键次keyword，键值
#value:
'''
print(infect.items())
print(infect.keys())
print(infect.values())
'''