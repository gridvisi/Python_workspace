import string
print(string.ascii_lowercase[:26])
print(''.join([chr(i) for i in range(97,123)]))


new_list = [i for i in range(101) if i % 3 == 0]
print(new_list)
##推荐
l = ['David', 'Pythonista', '+1-514-555-1234']
first_name, last_name, phone_number = l
print(first_name,last_name,phone_number)
# Python 3 Only
person = ['liu','qiang','dong']

person = ['liu','dong']
first_name, last_name = person
print('name:',first_name,last_name)

person = ['liu','cheng','xin']
first, *middle, last = person
print(first, *middle, last)


print("{}+{}={}".format(1,1,2))
#print("{}{}{}-{}{}{}{}-{}{}{}{}".format(list(str(13701183019))))



name_ls = ['张三','李林','王五', '赵六','Lucas']
all_name = ['张三','李林','王五', '赵六','Lucas','钱七']

res = [name for name in all_name if name in name_ls]
print('谁可以吃饭？',res)


for name in  ['张三','李林','王五', '赵六','钱七']:
    if name not in ['张三','李林','王五', '赵六']:
        print('不吃饭:',name)
    else:print('吃饭',name)