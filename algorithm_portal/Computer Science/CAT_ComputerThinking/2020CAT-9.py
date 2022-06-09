print(f"{10000000:,}")

#Which code snippet will return [1, 2, 3, [4, 5]]?

x = [1, 2, 3]
x.append([4, 5])
print(x)

x = [1, 2, 3]
x.extend([4, 5])
print(x)

my_set = {1, 'Python', ('John', 'Jeanne'), True}
print(my_set)


import copy
grass = [7,1,14,3,8,2,7,2,0,6]
print(id(grass),id(grass[:-1]))

grassbackup = copy.copy(grass)
print(sum(grass)/len(grass))

cost = 0
step = 0
t = []
for i,e in enumerate(grass[:-1]):
    print(i,cost,e,grass[i],grass)
    st = grass[i] - 5
    cost += abs(st)
  
    grass[i+1] += st
    grass[i] -= st
print(cost,grass)


#2
cost = 0
step = 0
grass = [7,1,14,3,8,2,7,2,0,6]
for i,e in enumerate(grass[:-1]):
    print(i,e,grass[i],grass)
    st = e - 5
    cost += abs(st)

    grass[i+1] += st
    grass[i] -= st
print(cost,grass)

#2 solve
cost = 0
step = 0
for i,e in enumerate(grass[:-1]):
    step += 1
    #print(f"{step}",grass)

    if e > 5:
        m = grass[i]-5
        grass[i] = 5
        grass[i+1] += m
        cost += m

    elif e < 5:
        a = 5 - e
        grass[i] = 5
        grass[i+1] -= a
        cost += a
    else:pass
#print(grass,cost)

# 级数
