'''
字典
# 我的车是红色宝马右舵里程是59公里，
# 女朋友的车是蓝色特斯拉左舵里程是1000公里
'''
gun = ['AK47','98K']
gun_cn = ['冲锋枪','毛瑟步枪']
dict(zip(gun,gun_cn))

phone_number = ["110","114","119","120"]
help_call = ['报警','查号','救火', '急救']

print(zip(phone_number,help_call))
re = dict(zip(phone_number,help_call))
print(re)
print(re['119'])

short_name = {'lzh':'李正浩'}

print(short_name['lzh'])

print('\n')

'''

'''

help_tips = ["police","switch","fire alert","ambulance"]
phone_book = dict(zip(phone_number,help_tips))
print(phone_book["110"])

teams = ["宝马", "奔驰", "特斯拉", "长城"]
flag = ['BMW','BENZI','TESLA','哈佛']

car_dict = {"BMW":"宝马"}

print(car_dict["BMW"])

dict_2 = zip(teams,flag)
dict_1 = {key: value for key,value in enumerate(teams)}
print(list(dict_2))
dict_3 = dict(zip(teams,flag))
for key,value in enumerate(dict_3):
    print('value = {}'.format(value))

from collections import namedtuple
Car = namedtuple('Car', 'color mileage brand LR_rudder')
my_car = namedtuple('Car', 'color mileage') #,'brand','LR_rudder'
my_car = Car('red', 5900,'BMW','Right_rudder')
print(my_car.color,my_car.mileage,my_car.brand)
print(my_car)

for key,value in dict_3.items():
    print('key = {},value = {}'.format(key,value))

for key,value in enumerate(dict_3):
    print('队名:{} , 队标:{}'.format(key,value))

for key,value in dict_3.items():
    print('队名:{} , 队标:{}'.format(key,value))
'''
输出：
red 5900 BMW
Car(color='red', mileage=5900, brand='BMW', LR_rudder='Right_rudder')
'''

her_car = namedtuple('Car','color mileage brand LR_rudder')
her_car = Car('blue',1000,'TESLA','Left_rudder')
print(her_car.brand,her_car.LR_rudder)

name = {"chuyi":["lyc","jerom"]}
#object
#phone_book = {}

'''
输出：
TESLA Left_rudder

#与元组一样，namedtuple 是不可修改的
her_car.color = 'red'
print(her_car.color)
AttributeError: "can't set attribute"
'''