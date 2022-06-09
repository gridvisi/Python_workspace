'''
https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python


'''
#  list 列表
sheep = 100
sheep = "重庆山羊"
team = ["people","sheep", "sheep","sheep", "sheep", "sheep","wolf", "sheep", "sheep","pig"]

for name in team:         #遍历
    if name == 'wolf':
        print(team.index(name))

print(team.index("pig"))

#x if x > 4: return 'kingguarden k4'


n = 123 # [1,2,3]
n = 'ada'
#integer
n = "123"
print(int(n) + 8)

print(list(str(n)))

print(str(n) + "hello")
print(str(n) + 'hello')
#string
print(str(n)[:-1])