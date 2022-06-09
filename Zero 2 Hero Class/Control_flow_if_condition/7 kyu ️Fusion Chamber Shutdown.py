'''
https://www.codewars.com/kata/5fde1ea66ba4060008ea5bd9/train/python

A laboratory is testing how atoms react in ionic state during nuclear fusion. They introduce different elements with Hydrogen in high temperature and pressurized chamber. Due to unknown reason the chamber lost its power and the elements in it started precipitating
Given the number of atoms of Carbon [C],Hydrogen[H] and Oxygen[O] in the chamber. Calculate how many molecules of Water [H2O], Carbon Dioxide [CO2] and Methane [CH4] will be produced following the order of reaction affinity below

1. Hydrogen reacts with Oxygen   = H2O
2. Carbon   reacts with Oxygen   = CO2
3. Carbon   reacts with Hydrogen = CH4
FOR EXAMPLE:
(C,H,O) = (45,11,100)
return no. of water, carbon dioxide and methane molecules
Output should be like:
(5,45,0)
FUNDAMENTALSNUMBERSCONTROL FLOW

一个实验室正在测试原子在核聚变过程中如何发生离子状态的反应。他们在高温高压室中引入不同元素与氢气。由于未知的原因，
试验室失去了动力，其中的元素开始析出。
给定室中碳[C]、氢[H]和氧[O]的原子数。计算按照以下反应亲和力的顺序，
将产生多少分子的水[H2O]、二氧化碳[CO2]和甲烷[CH4]。
沼气
1. 氢气与氧气反应=H2O。
2. 碳与氧气反应=二氧化碳
3. 碳与氢反应=CH4
'''
water = {'h':2,'o':1}
h = 10
#print(water[str(h)])


# Make sure you follow the order of reaction
# output should be H2O,CO2,CH4

#14th by ericlee
def burner(c,h,o):
    water = {'h':2*min(h//2,o),'o':min(h//2,o)}
    co = {'c':min(c,(o-water['o'])//2),'o':2*min(c,(o-water['o'])//2)}
    methane = {'c':min(c-co['c'],(h-water['h'])//4),'h':min(c-co['c'],(h-water['h'])//4)}
    return water['o'],co['c'],methane['c']
c,h,o = 45,11,100
c,h,o = 354,1023230,0
c,h,o = 939,3,694
print(burner(c,h,o))

'''
    for i,elem in enumerate([water,co2,methane]):
        #small = min(c//elem.get('c',0.01),h//elem.get('h',0.01),o//elem.get('o',0.01))
        small = [i for i in elem.values() if i in elem]
        ans[i] = int(small)
        print(elem,ans,c,h,o)
        h -= 0 if h not in elem else small*elem[h]
        o -= 0 if o not in elem else small*elem[o]
        c -= 0 if c not in elem else small*elem[c]
'''

#1st
# Make sure you follow the order of reaction
# output should be H2O,CO2,CH4
def burner(c, h, o):
    water = co2 = methane = 0

    while h > 1 and o > 0:
        water += 1
        h -= 2
        o -= 1

    while c > 0 and o > 1:
        co2 += 1
        c -= 1
        o -= 2

    while c > 0 and h > 3:
        methane += 1
        c -= 1
        h -= 4

    return water, co2, methane

#2nd
def burner(C, H, O):
    H2O = min(H//2, O)
    CO2 = min(C, (O-H2O)//2)
    CH4 = min(C-CO2, (H-2*H2O)//4)
    return H2O, CO2, CH4

