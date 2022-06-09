

a = "5.33"

x,y = a.split(".")
s = int(x) + round(int(y)/100,2)
print(round(s ** 2,2))
print(x,y)