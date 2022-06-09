
three_div = []
for i in range(100,1000+1,100):
    three_div.append([i,i // 3,i % 3])
print(three_div)

three_div_pow = []
for i in range(10):
    three_div_pow.append([10**i,10**i // 3,10**i % 3])
print(three_div_pow)

# x * 10**digit ==