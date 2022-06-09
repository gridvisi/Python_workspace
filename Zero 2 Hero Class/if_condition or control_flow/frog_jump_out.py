# 5米的井深，青蛙井底白天向上爬2米，晚上掉下去1米，问需要几天爬出来

hight = 5
h = 0
day = 0
while h < hight:
    h += 2
    if h >= hight:
        ans = day
    h -= 1
    day += 1
print(ans)
