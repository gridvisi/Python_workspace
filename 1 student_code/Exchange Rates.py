
rmb = 1000
usd = 100
rate = 6.37
print(type(rate)) #浮点小数
print(type(rmb))  #Integer
#函数实现人民币和美元互换
#$ = 3
s = 3

#￥, $$
#usd = "usa dollar"
#x = "candy"


def exchange_rmb_usd(rmb): #参数
    return f"{rmb}人民币，可以换{round(rmb/rate,2)}美元"

print(exchange_rmb_usd(rmb))

# 7
usd_ls = [200,51,99,9,520,0] #google

# 列表推导式
print([exchange_rmb_usd(i) for i in usd_ls])

