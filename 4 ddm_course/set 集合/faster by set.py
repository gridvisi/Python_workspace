#https://blog.csdn.net/business122/article/details/7541486?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

#advanced api basics best-practices

print(2**38)

import time

with open("names.txt") as f:
    names = f.readline()[:1000000]
    names_set = set(names)
print(names)
'''
names = [str(i) for i in range(1000000)]
names_set = set(names)
'''
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