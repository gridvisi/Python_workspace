import random
# 多个字符中选取指定数量的字符组成新字符串：
print(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))

# 随机选取字符串：
print(random.choice(['剪刀', '石头', '布']))

# 打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print (random.shuffle(items))