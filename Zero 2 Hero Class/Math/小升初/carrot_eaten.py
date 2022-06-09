'''
3000个萝卜运到1000km的地方，每公里吃1个，每次最多驮1000个萝卜
问运到目的地多少个萝卜

'''
import math
carrot = 3000
print(math.ceil(1000/5),5 * math.ceil(1000/5))
carrot = carrot - 5 * math.ceil(1000/5)
first_leap = math.ceil(1000/5)

# 1000 - 2 * second_leap + carrot - 1000 - second_leap = 1000
second_leap = (carrot - 1000) / 3
print(math.ceil(second_leap),carrot)

third_leap = 1000 - first_leap - math.ceil(second_leap)
print('3rd:',third_leap)
print(carrot - 3 * second_leap - third_leap)


#2nd loop solution

def consume(carrot,distance,load,per):
    bench = []
    rate = []
    round_trip = math.ceil(carrot/load)
    for i in range(round_trip,1,-1):
        bench.append(int(load/(2*i-1)))
        carrot -= (2*i-1) * int(load/(2*i-1))*per
    rest = carrot - (distance - sum(bench))
    return rest,carrot,bench,round_trip

carrot,distance,load,per = 3000,1000,1000,1
print('solution:',consume(carrot,distance,load,per))

print('rate:',[round(consume(carrot,distance,load,per)[0]/carrot,2) for carrot in range(2000,20000,1000)])

'''
一个商人骑一bai头驴要穿越1000公里长的沙漠，去卖3000根胡萝卜。已知驴一次性可驮1000根胡萝卜，但每走1公里又要吃掉1根胡萝卜。这才是问题啊 、
假设出沙漠时有1000根萝卜，那么在出沙漠之前一定不只1000根，那么至少要驮两次才会出沙漠，那样从出发地到沙漠边缘都会有往返的里程，那所走的路程将大于3000公里，故最后能卖出萝卜的数量一定是小于1000根的。
那么在走到某一个位置的时候萝卜的总数会恰好是1000根。
因为驴每次最多驮1000，那么为了最大的利用驴，第一次卸下的地点应该是使萝卜的数量为2000的地点。
因为一开始有3000萝卜，驴必须要驮三次，设驴走X公里第一次卸下萝卜
则：5X=1000（吃萝卜的数量，也等于所行走的公里数）
X=200，也就是说第一次只走200公里
验算：驴驮1000根走200公里时剩800根，卸下600根，返回出发地
前两次就囤积了1200根，第三次不用返回则剩800根，则总共是2000根萝卜了。
第二次驴只需要驮两次，设驴走Y公里第二次卸下萝卜
则：3Y=1000， Y=333.3
验算：驴驮1000根走333.3公里时剩667根，卸下334根，返回第一次卸萝卜地点
第二次在途中会吃掉334根萝卜，到第二次卸萝卜地点是加上卸下的334根，刚好是1000根。
而此时总共走了：200+333.3=533.3公里，而剩下的466.7公里只需要吃466根萝卜
所以可以卖萝卜的数量就是1000-466=534
'''
res = []
min = float("inf")

for i in range(1,1001):
    for j in range(1,1001-i):
        if 6*i + j*3 >= 2000:
            x = 3000 - (6*i + j*3) - (1000-i-j)
            res.append([x,i,j])
ans = res[-1]
print(max(res))

max = 0
for i in range(1,1001):
    for j in range(1,1001-i):
        if 6 * i + j * 3 >= 2000 :
            if i + j > max:
                max = i + j
                res.append([i+j,6*i + j*3,i,j])
ans = res[-1]
print(3000 - ans[1] - ans[0],ans)


'''
在1000/7约为142.5处
在142.5+ 1000/5约为342.5处
在342.5 +1000/3约为676处
设3个中转点ABC
第一次运到A点留下5/7的胡萝卜
第二次运到B点留下3/5的胡萝卜（在经过A点时补充1/7的胡萝卜）
第三次运到C点留下1/3的胡萝卜（......）
第四次运到终点（......）
最后剩下的胡萝卜有676个
'''
carrot,load = 3000,1000


def consume_2(carrot,distance,load,per):
    cunt = int(carrot / load)
    distance = 1000
    turn_point = []
    s, used = 0, 0
    x = distance * (1/(2 * cunt + 1))
    used += int(x) * (2 * cunt - 1)
    s += x  # distance to start
    carrot -= used  # rest of carrot
    cunt = int(carrot/load)

    while cunt > 1:
        for i in range(cunt,1,-1):
            x = load/(2*cunt-1)
            carrot -= int(x) * per
            cunt = int(carrot/load)
            turn_point.append([used,s,x])
    return turn_point
print('2nd:',consume_2(carrot,distance,load,per))
first = 1000 / 7
print(first)
second = first - 1000


