
tv_pcs = 28
list_price = 500

def discount_plan_a(x):
    if x >= 20:
        total = x * 0.75 * 500
    else:
        total = x * 500
    return total

def discount_plan_b(x):
    return (x - (x//10) * 3) * 500

x = tv_pcs
print(x//10)
print(discount_plan_a(x),discount_plan_b(x))