'''
多边形的内角和公式 eg:1510

vector*(vector-3)/2,vector
'''
# 多变形的角数量等于边的数量，等于顶点数量
# 对角线数量等于顶点数量除以2
# 顶点数和对角线数的关系：vector*(vector-3)/2,vector
vector = 3
angle = 1510
#for i in range(100):
while 180 * (vector-2) < angle:
    vector += 1
print(vector*(vector-3)/2,vector)
