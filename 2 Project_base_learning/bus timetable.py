__author__ = 'Administrator'
time1="00:06:30"
time2="00:07:00"

min1=((int(time1[3]))*10+int(time1[4]))*60+(int(time1[6]))*10+int(time1[7])
min2=((int(time2[3]))*10+int(time2[4]))*60+(int(time2[6]))*10+int(time2[7])

while (min2-min1)%7!=0:
   min2 += 13
   if (min2-min1)%7==0:
      mm=min2%60
      hh=(min2-mm)/60
print("get up bus same time is:", int(hh),'时',mm,'分')