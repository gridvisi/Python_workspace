'yellow'

def lizj():
    print([9,132,'orange'])
lizj()

def addOneYear(x):
    return sum([i+1 for i in x]), round(sum([i+1 for i in x])/len(x),2)#列表推导式

x = [9,10,13,8]
print(x[1])
print(addOneYear(x)[1])


print(addOneYear(x))


def convert(inp): #->str
    month = "January，February，March，April，May，June，July，" \
            "August，September，October，November，December"
    month = month.split("，")
    print(month)
    num = ['0' + str(i) if i < 10 else str(i) for i in range(1, 13)]
    num2month = dict(zip(num, month))
    inps = inp.split("/")
    print('inps:',inps)
    return num2month[inps[0]] +" "+ ','.join(inps[1:])
inp = '05/21/2021' #'May 21,2021'
inp = input("请输入一个日期，格式为：月/日/年:")
print(convert(inp))


#a = input("请输入一个日期，格式为：月/日/年:")
c = ['  ','January','February','March','April','May','June',
     'July','August','September','October','November','December']
print(c[12])
print(c.index('January'))








rq = c.split('/')
month = int(rq[0])
date = int(rq[1])
nian = int(rq[2])
#print(c[month],date,',',nian)