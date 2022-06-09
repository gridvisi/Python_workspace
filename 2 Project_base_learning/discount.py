__author__ = 'Administrator'

# 新华书店开张打惠，每满61元送16元的卷，同时享受79折扣。243.4,133.51
print(round((133.51) / 243.4, 4), 24.8 * 8 + 45, 40 * 0.79)

# 直接按总金额打折后，再用劵消费
def pay(total_price, good, step, discount):
    off_price = total_price*discount
    coupon_num = int(off_price/step)
    rate = off_price / (total_price + coupon_num*good)
    return round(off_price,2), round(rate,2),coupon_num,coupon_num*good+total_price

def coupon(total_price, good, step, discount):
    count = 1

    gap = step/discount
    while gap < total_price:
        gap = gap +(step+good)/discount
        base = step*count
        count += 1

    return base

def gap(total_price,good,step,discount):
    count = 0
    gap = step/discount
    x = [round(gap,2)]
    while gap < total_price:
        gap = gap + (step+good)/discount
        x.append(round(gap,2))
        count += 1
    return x[-2]

def gap_list(total_price,good,step,discount):
    count = 0
    gap = (step + good)/discount
    x = [round(gap,2)]
    while gap < total_price:
        gap = gap + (step+good)/discount
        x.append(round(gap,2))
        count += 1
    return x


total_price = float(input('您购买的书总价是：'))
discount = 0.79
step = 61
good = 16
if total_price < step/discount:
    print("消费不够61元，只享受79折：",total_price*discount)
else:
    coupon_total = coupon(total_price,good,step,discount)/step
    sum = coupon(total_price,good,step,discount)+(total_price-gap(total_price,good,step,discount))*discount
    sum = round(sum,2)
#round((gap-(step+good*count)/discount),2)
    print('全场79折，每满61元，即返即用16元，最低消费：', round((step + good)/ discount, 2), '元，即可获得一张16元卷')
    print(gap_list(total_price,good,step,discount))
#print(coupon(total_price,good,step,discount))
    list = gap_list(total_price,good,step,discount)
    print('实际支付：', sum, '优惠卷共计使用：', coupon_total,'张','共计优惠卷金额：',(coupon_total-1)*good, 'rmb，剩余优惠卷', 1, '张')
    print('您距离下一个优惠卷，还需要消费：', round((list[-1] - total_price), 2))
    print('综合折扣率：', round(sum/(total_price+good), 2))
    print('总额折扣后使用优惠卷和折扣率是:',pay(total_price, good, step, discount))
