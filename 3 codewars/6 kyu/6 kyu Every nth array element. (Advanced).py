'''
https://www.codewars.com/kata/every-nth-array-element-basic/train/python
With no arguments, array.every it returns every element of the array.
With one argument, array.every(interval) it returns every intervalth element.
With two arguments, array.every(interval, start_index) it returns every intervalth element starting at index start_index

javascript:                          ruby:
every(array)                         array.every
every(array, interval)               array.every(interval)
every(array, interval, start_index)  array.every(interval, start_index)
Examples
[0,1,2,3,4].every      # [0,1,2,3,4]
[0,1,2,3,4].every(1)   # [0,1,2,3,4]
[0,1,2,3,4].every(2)   # [0,2,4]
[0,1,2,3,4].every(3)   # [0,3]
[0,1,2,3,4].every(1,3) # [3,4]
[0,1,2,3,4].every(3,1) # [1,4]
[0,1,2,3,4].every(3,4) # [4]
Notes:(http://www.codewars.com/kata/every-nth-array-element-advanced

'''
array, interval, start_index = [0,1,2,3,4],2,1
array, interval = [0,1,2,3,4],2
array= [0,1,2,3,4]
array, interval, start_index = [0,1,2,3,4],3,4
#start_index = 2
def every(array, *args):
    re,interval,start_index = [],1,0
    print(array,interval,start_index)
    for i in range(start_index,len(array),interval):
        re.append(array[i])
    return re

def every(array, interval=1, start_index=0):
    return array[start_index::interval]

def every(array, interval=None, start=None):
    return array[start::interval]
print(every(array, interval, start_index ))
