__author__ = 'Administrator'
def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        res = 0
        for i in s:
            res += int(i)
        while res > 9:
            s = str(res)
            res = 0
            for i in s:
                res += int(i)
        return res

def getprim(n):
    p=3
    x=0
    q = []
    while(x<n):
        result=True
        for i in range(2,int(p/2)): #除数的上限设为（p/2)取整
            if(p%i==0): #如果p可以被i整除
                result=False #则不是素数，返回false
        if result==True: #如果算出来是素数
            #print(p)  #则打印出来
            q.append(p)
            x=x+1
            rst=p

        p+=2
        return q

print(getprim(10000))

print(addDigits(0,17))


'''
作者：喵在野
链接：https://www.jianshu.com/p/b6628a01b6ca
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
'''