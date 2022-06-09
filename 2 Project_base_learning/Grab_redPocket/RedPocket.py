
def redPacket(num):
    n = 1
    for i in range(num):
        init = n
        while n % (i+1):
            n += init
    return n


amount_of_kids = 5
print(f'{amount_of_kids}',redPacket(amount_of_kids))

amount_of_kids = 7
print(f'{amount_of_kids}',redPacket(amount_of_kids))

amount_of_kids = 10
print(f'{amount_of_kids}',redPacket(amount_of_kids))