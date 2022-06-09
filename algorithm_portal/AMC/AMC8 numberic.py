'''
当一个正整数N被送入一台机器时。此处大喵解释为数学和编程的函数
f(n)= n/2        if n%2==0
f(n) = 3*n + 1 if n%2==1

其输出是一个根据下图所示规则计算的数字。

例如，从一个N=7的输入开始，机器将输出3*7+1=22。然后，如果再将输出重复插入机器5次，
最后的输出是26。

当同样的6个步骤应用于不同的起始值N时，最后的输出是1。所有这样的整数N的总和是多少？


(a) 73 (b) 74 (c) 75 (d) 82 (e) 83

f(n)= n/2        if n%2==0
f(n) = 3*n + 1   if n%2==1

'''

def even_odd(n,step,ans=[]):
    #print('n:',n)
    #print('n,step,ans:',n,step,ans)
    while step >= 0:

        if step == 0:
            ans.append(n)
            return n
        else:
            if n%2==1:
                n = 3*n+1
                step -= 1
                return even_odd(n,step,ans)

            elif not n%2:
                n = n//2
                step -= 1
                return even_odd(n,step,ans)

'''
1 ：[1,2,4,1,2,4,1]
2 ：[1,2,4,8,16,5,10]
3：[1,2,4,1,2,4,8] 
4、 [1,2,4,8,16,32,64]
'''
n,step = 10,6
print('ans:',even_odd(n,step,ans=[]))

ans = []
for n in range(100):
    if even_odd(n,step=8,ans=[]) == 1:
        ans.append(n)
print(ans)

#优化算法

def even_odd(n,step,ans=[]):
    #print('n:',n)
    #print('n,step,ans:',n,step,ans)
    while step >= 0:

        if step == 0:
            ans.append(n)
            return n
        else:
            if n%2==1:
                n = 3*n+1
                step -= 1
                return even_odd(n,step,ans)

            elif not n%2:
                n = n//2
                step -= 1
                return even_odd(n,step,ans)