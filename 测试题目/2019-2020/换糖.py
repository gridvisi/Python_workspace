
# 第一步先不考虑糖纸换糖
rmb = 10
wrappers = 0
eaten = 0
while rmb > 0:
    rmb -= 1
    eaten += 1
    wrappers += 1
print("吃掉的糖总计total candy:", eaten,"糖纸共计:",wrappers)

# 第二步考虑糖纸换糖，wrappers变化和candy的关系
rmb = 10
wrappers = 0
eaten = 0
while rmb > 0:
    rmb -= 1
    eaten += 1
    wrappers += 1
    if wrappers == 3:
        wrappers -= 3
        eaten += 1
        wrappers += 1
print("total candy Answer:", eaten)
