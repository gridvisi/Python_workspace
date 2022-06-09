__author__ = 'Administrator'
'''
I will walk from A to B moving only North and East along the grid lines. Then, I will walk back to A along the gridlines, visiting only locations that I have not visited before.
我将沿着网格线从A走到B，只向北和东移动。然后，我将沿着网格线回到A，只访问我以前没有访问过的位置。
x= 0,1,2,3,4,5  y = 0,1,2,3
How many paths are there from A to B that allow me to walk back to A in this way?
从A到B有多少条路可以让我这样走回A？

字典的value反过来求key
student = {'小萌': '1001', '小智': '1002', '小强': '1003', '小明': '1004'}
list (student.keys()) [list (student.values()).index ('1004')]
'''
pace = {}

def node(x,y,key):
    if x == 0 and y == 0:
        pace = {0:[0,0]}
        return pace
    else:
        xy_list = []
        rate = 0
        pace = {0:[0,0]}
        for i in range(x+1):
            for j in range(y+1):
                xy_list.append([i,j])

        step = 1
        key_list = []
        for i in range(len(xy_list)):
            key_list.append(i)
            pace[key_list[i]] = xy_list[i]

        #list(pace.keys())[list(pace.values()).index('a')
        for key,val in pace.items():
            if val[0] == 0:
                return
            while val[0] == 0 and val[1] > 0:
                return val
        #return pace,key




print(node(5,3,0))





'''
        #i = 0
        #j = 0
        for i in range(x+1):
            for j in range(y+1):
                pace[]
for key,val in pace.items():
                #for k in range(x):
                 result = []
                 if val[0] == 0 and val[1] == 1:
                    key = 1
                    result.append(val)
                 if val[0] == 1 and val[0] == 0:
                    key = 1
                    result.append(val)
                    return key,result

print(node(0,0,0))

while step < len(pace):
            if pace[step][0] -1 < 0:
                pace[step] = pace[step - 1]
            if pace[step][1] - 1< 0 and step > y:
                pace[step] = pace[step - y]

            elif pace[step][0] - pace[step - 1][0] == 1 or xy_list[step][1] - xy_list[step - 1][1] == 1:
                key_list[step] = key_list[step - 1] + key_list - 2



        pace[key+j] = [i,j]
        pace[key+i] = [i,j]
        pace[0] = [0,0]
return xy_list



     key_list = []
      #xy_list.append([i,j])
for k in range(1,x * y):
    key_list[k]
        pace[key_list[k]] = {key_list[k]:[i,j]}
            #pace[key] = [i,j]
        return pace,key_list



'''