

s = sum([1,2,3],5)          #in list +start
#11
print('No.1 []+num:',s)

s = sum((1,2,3))            #in tuple
#6
print('No.2 ():',s)

s = sum({1,2,3})            #in set
#6
print('No.3 {}:',s)

s = sum({1:5,2:6,3:7})      #in dictionary key
#6
print('dict():',s)

s = sum(range(1,4))         #in range()
print('range:',s)

array = [[1,2,3],[5]]
s = sum(array, [])
print('array + []:',s)

array = [[1,2,3],[5],[[1,2,3]],[[[7,8,9]]]]
s = sum(array, [])
print('array + []:',s)


#above is output proper,while below is not!!!
#print('sum([[]])',sum(array))
#s = sum([[1,2,3],[5]])          #in list +start
#s = sum([1,2,3],[5])
s = sum([[1,2,3],[5]],[])
print(s)
#print(sum([1,2,3],[]))
print(sum([[10,20,30]],[]))
