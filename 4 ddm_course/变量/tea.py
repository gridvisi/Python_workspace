tea = 3
money = 10

def cup(money):
    return money//tea,money%tea
print(cup(money))

def cup(money):
    c = 0
    while money >= 3:
        money = money - tea
        c += 1
    return money,c
print(cup(money))



total = 3
package = 0
eat = 0
while total > 0:
    eat += 1
    package += 1
    if package == 3:
        eat += 1
        package -= 3
    total -= 1
print(total,eat,package)