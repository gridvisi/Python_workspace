
# 十进制转二进制
# 0，1
#第一个口袋和量杯都认为是二进制最左边的bit？
#10 = 1010
s = [0,31]



for i in range(10):print(i)

num = "111010101"
def t(num):
    num = str(num)
    amath = 2
    output = 0
    for i,e in enumerate(num):
        output += int(e) * 2 ** (len(num) - i)
        #print(output)
    return output

print(int(num,2))
print(int(num,2))

print(t(num))


# not stuck
lzh = {"bull":["comments","performance","RAM","keyboard"]}

#i7处理器的性能比i5处理器高
high_performance = ["cpu",]
cpu = ["i9","i7",'i5',"i3"]
RAM = ["4G","8G","16G"]
brand = ["alienware","lenovo","MI","HUAWEI","APPLE","Acer","asus","surface"]

sys_requirment = '''64-bit versions of Microsoft Windows 10, 8
2 GB RAM minimum, 8 GB RAM recommended
2.5 GB hard disk space, SSD recommended
1024x768 minimum screen resolution
Python 2.7, or Python 3.5 or newer
'''

budget_plan = {"asus":4179,"dell":4299,"MI":3999,"lenovo":4599}
performance = {"asus":["i5-1035G1",'512GSSD MX330 2G独显']}

print(budget_plan["asus"],performance["asus"])
vote = {"asus":4}


zhy = "performance"
longxch = "ram"
lyn = "bag"
