__author__ = 'Administrator'
'''
Fraser、乔治娜和欧文都在努力建造最高的雪人。
Fraser：“雪球越少越高。我将堆积2个半径相等的球体。
乔治娜：“我不同意，我认为更多的雪球会更高。我将堆积10个半径相等的球体。
欧文：“你制造多少球并不重要。我要做6个半径相等的球，三个雪人都是一样高的。
如果他们都有同样的降雪量，哪一个雪人最高？  球的体积计算公式：V球=(4/3)πr^3, r为球半径
'''
import math
def snowball(volume,x):

    v = volume/x;

    h = 2*x*pow(0.75*(v/math.pi),1/3)
    print(pow(0.75*(4/math.pi),1/3))

    #h1**3 = (x1**3)*(0.75*volume/x1)
    #(h1:h2:h3)**3 =(x1**3)*(volume/x1):(x2**3)*(volume/x2):(x3**3)*(volume/x3)
    #h1:h2:h3 = pow(x1,2/3) : pow(x2,2/3) : pow(x3,2/3)

    return h
volume = int(input('volume:'))
x1 = int(input('fraster:'))
x2 = int(input('Georgina:'))
x3 = int(input('Owen:'))
print('h1:h2:h3 =',snowball(volume,x1),snowball(volume,x2),snowball(volume,x3))
