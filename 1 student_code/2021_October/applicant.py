import time
start_time = time.time()
num = [i for i in range(0,100000000,2)]
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
num = [i for i in range(0,100000000) if i % 2 == 0]
end_time = time.time()
print(end_time - start_time)



num = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(num)

print(3 / 2)
print(3 // 2)
print(13 % 10)
print(num)



