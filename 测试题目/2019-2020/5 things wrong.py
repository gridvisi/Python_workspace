import time
def useful_function():
    for i in range(5):
        print("i swear I'm useful:{}".format(i))
        time.sleep(1.0)

print(useful_function())
#from one_main import useful_function

if __name__ == '__main__':
    useful_function()

# python one_main.py # execute result:
'''
i swear I'm useful:0
i swear I'm useful:1
i swear I'm useful:2
i swear I'm useful:3
i swear I'm useful:4
'''
# useful_function.py

#2 except
'''
while True:
    try:
        print("Wheeeee! You can't stop me")
        time.sleep(0.1)
    except:
        print("Oww... Whatever imma keep running")
'''
import time
while True:
    try:
        print("Wheeeee! You can't stop me")
        time.sleep(0.1)
        raise Exception("woah")
    except Exception:
        print("Oww... Whatever imma keep running")

import traceback
try:
    raise Exception('bad exception with stupid message')
except Exception as e:
    print("this is what print the exception is like")
    print(e)
    print()
    print("this is what traceback.print_exc() is like")
    traceback.print_exc()
    print()
    print("this is what traceback.print_exc() is like")

    str = traceback.format_exc()
    print(str)

#4
def add_names_to_agg_list(names,aggregate_list=[]):
    for name in names:
        aggregate_list.append(name)
    return aggregate_list
print(add_names_to_agg_list(['apple','banana','carrot']))
print(add_names_to_agg_list(['apple','banana','carrot']))

def add_names_to_agg_list(names,aggregate_list=None):
    if isinstance(aggregate_list,type(None)):
        aggregate_list = []
    for name in names:
        aggregate_list.append(name)
    return aggregate_list

print(add_names_to_agg_list(['apple','banana','carrot']))
print(add_names_to_agg_list(['apple','banana','carrot']))


'''
3# speed
https://blog.csdn.net/chenmozhe22/article/details/81434549
with open("names.txt") as f:
    names = f.readline()[:1000000]
    names_set = set(names)

def in_name():
    ret = []
    for i in range(100):
        ret.append(str(i) in names)
    return ret

def in_name_set():
    ret = []
    for i in range(100):
        ret.append(str(i) in names_set)
    return ret

print("Running in_names")
s = time.time()
in_name()
print("Time taken:",time.time()-s)

print("Running in_names_set")
s = time.time()
in_name_set()
print("Time taken:",time.time()-s)

'''