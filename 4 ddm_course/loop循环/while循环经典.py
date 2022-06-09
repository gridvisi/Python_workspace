







'''
1979年，李政道博士给中国科技大学少年班出过一道知趣题：5只猴子分一堆桃子，怎么也分不成5等分，
只好先去睡觉，准备第二天分。夜里1只猴子偷偷爬起来，先吃掉一个桃子，然后将其分为5等份，
藏起自己的一份就去睡觉了；第二只猴子又爬起来，吃掉一个桃子后，也将桃子分成5等份，藏起自己的一份睡觉去了；
以后的3只猴子都先后照此办理。问最初有多少个桃子？
'''
total=1

for i in range(5):
    total=total*5+1
print(total)

#https://blog.csdn.net/weixin_34269583/article/details/93930002

'''
质数因子的团圆
我们发现任意一个正整数可以分解为若干质数因子的乘积。这在我们前面一期有介绍列表推导式一行代码生产所有因子。
今天的任务稍有不同。不仅要知道有哪些因子，而且得出每个因子出现次数。譬如
2019 = 3 * 673
1000 = (2**3)(5**3)
86729 = (86729)      #质数无法进一步分解质因数
1474393 = 17 * 86729
86240 = (2**5)(5)(7**2)(11)

Input: 第一个数据 n
实例1：1474393
实例2：86240

output
"(p1**n1)(p2**n2)...(pk**nk)"

实例1：（17)(86729)
实例2：  (2**5)(5)(7**2)(11)
'''

def primeFactors(n):
    res = ''
    for i in range(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            res += '({}{})'.format(i, '**%d' % num if num > 1 else '')#“ 此空白处，请您补齐代码”
            if n == 1:
                return res
n = 86240
print(primeFactors(n))

'''
NOIP的竞赛训练 Description
有一堆桃子和N只猴子，第一只猴子将桃子平均分成了M堆后，还剩了1个，它吃了剩下的一个，并拿走一堆。
后面的猴子也和第1只进行了同样的做法，请问N只猴子进行了同样做法后这一堆桃子至少还剩了多少个桃子
(假设剩下的每堆中至少有一个桃子)？而最初时的那堆桃子至少有多少个？
https://blog.csdn.net/oopos/article/details/1829882
Input
第一个数据为猴子的只数N(1≤N≤10)
第二个数据为桃子分成的堆数M(2≤M≤7)。

Output
输出包含两行数据，第一行数据为剩下的桃子数，第二行数据为原来的桃子数。

Sample Input
3 2

Sample Output
1 15
'''


# sub_total = (m - 1)*(sub_total_prior - 1)//m ->
# sub_total_prior = 1 + sub_total * m // (m-1)


n,m = 6,3
def peach_divide(n,m):
    i,k = 0,1
    prev = k*(m-1)
    #prev = 6
    while i < n:
        print('test',prev,i,k)
        if prev % (m-1) != 0:
            i = 1
            k += 1
        else: prev = 1 + prev * m / (m - 1)
        i += 1
    return k*(m-1),prev

print(peach_divide(n,m))
'''
rem = 0
for i in range(n):
    rem = (m-1)*(n-1)//m
print('rem:',rem)

#include<iostream>
using namespace std;
int main(){
	int n,m;
	cin>>n>>m;
	int i=1,j=0,k=1,p=1;
	p=k*(m-1);
	while(i<=n) {
  		if(p%(m-1)!=0) {
   			i=1;
   			k++;
   			p=k*(m-1);
  		}else{
   			p=p/(m-1)*m+1;
   			i++;
  		} 
	} 
	cout<<k*(m-1)<<endl<<p;
	return 0;
}

1979年，李政道博士给中国科技大学少年班出过一道知趣题：5只猴子分一堆桃子，怎么也分不成5等分，
只好先去睡觉，准备第二天分。夜里1只猴子偷偷爬起来，先吃掉一个桃子，然后将其分为5等份，藏起自
己的一份就去睡觉了；第二只猴子又爬起来，吃掉一个桃子后，也将桃子分成5等份，藏起自己的一份睡觉
去了；以后的3只猴子都先后照此办理。

问最初有多少个桃子？
 '''


def consume(count, num):
    if count == 0:
        return 1

    elif (num - 1) % 5 != 0:
        return -1

    num = (num - 1) * 4 / 5
    return consume(count - 1, num)


count=5
num=1
while num <10000:
    num+=1
    result=consume(count,num)

    if result == 1:
        print(num)

