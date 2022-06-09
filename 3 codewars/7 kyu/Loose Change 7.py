def change_count(change):
    change = change.split(' ',change.count(' '))
    money = 0
    for i in range(0,len(change)):
        if change[i] == "penny":
            money += 0.01
        elif change[i] == "nickel":
            money += 0.05
        elif change[i] == "dime":
            money += 0.10
        elif change[i] == "quarter":
            money += 0.25
        elif change[i] == "dollar":
            money += 1.00
    money = str(money)
    money = list(money)
    money_out = ''.join(money)
    return '$'+str('%.2f' % float(money_out))
print(change_count("dollar"))