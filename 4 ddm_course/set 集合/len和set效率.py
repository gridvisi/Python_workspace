import random
import time

def RandomNumber1(number, start, end):
    data = []
    n = 0
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
            n += 1
        if n == number:
            break
    return data

def RandomNumber2(number, start, end):
    data = []
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
        if len(data) == number:
            break
    return data


def RandomNumber3(number, start, end):
    data = set()
    while True:
        data.add(random.randint(start, end))
        if len(data) == number:
            break
    return data


start = time.time()
for i in range(500):
    RandomNumber1(1000, 1, 10000)
print('time1 used = ', time.time() - start)

start = time.time()
for i in range(500):
    RandomNumber2(1000, 1, 10000)
print('list_time_used = ', time.time() - start)

start = time.time()
for i in range(500):
    RandomNumber3(1000, 1, 10000)
print('set_time3_used = ', time.time() - start)
