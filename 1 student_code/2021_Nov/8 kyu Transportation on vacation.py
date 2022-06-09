'''
https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python

在办公室辛苦工作了一个季度后，你决定在假期中得到一些休息。
因此，你将为你和你的女朋友预订一个航班，并试图将所有的混乱抛在身后。

你需要一辆租来的汽车，以便你在假期中四处游玩。租车公司的经理给你
提供了一些好的优惠。

每一天你租车的费用是40美元。如果你租车7天或以上，你可以得到50美元
的优惠。或者，如果你租车3天或以上，你可以得到20美元的优惠。

写一个代码，给出不同天数的总金额（d）
'''

def rental_car_cost(d):
    # 1-3 days: d*40
    # 3-6 days: d*40 - 20
    # 7-> days: d*40 - 50
    return d*40 if 1<=d<3 else d*40-20 if 3<=d<=6 else d*40 - 50

# Nice solution!!!
def rental_car_cost(d):
    return d * 40 - (d > 2) * 20 - (d > 6) * 30