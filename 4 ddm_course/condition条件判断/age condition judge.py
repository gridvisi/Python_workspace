__author__ = 'MJ'

per = int(input("人数："))
str_in = input('请以空格为间隔连续输入一个age数组:')
age = [int(n) for n in str_in.split()]
i=1;a=0;b=0;c=0;d=0;
for i in range(per):
    if age[i] < 18:
        a+=1
    elif age[i]>19 and age[i]<35:
        b+=1
    elif age[i]>35 and age[i]<60:
        c+=1
    elif age[i]>60:
        d+=1
    # i+=1
print(format(a/per,'.0%'))
print(format(b/per,'.0%'))
print(format(c/per,'.0%'))
print(format(d/per,'.0%'))
# 34 3 67 45 22 33 45 53 57 88
# 1 11 21 31 41 51 61 71 81 91



