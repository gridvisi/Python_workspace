
#https://www.codewars.com/kata/5a61a846cadebf9738000076/train/python
def peak(arr):
    return max([i if sum(arr[:i]) == sum(arr[i+1:]) else -1 for i,e in enumerate(arr)])

arr = [1,2,3,5,3,2,1]
print(peak(arr))

def peak(arr):
    for i, val in enumerate(arr):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

def peak(arr):
    sl, sr = 0, sum(arr)
    for i,v in enumerate(arr):
        sr -= v
        if sr == sl: return i
        elif sl > sr: return -1
        sl += v

def peak(arr):
  return next(iter(i for i in range(len(arr)) if sum(arr[:i]) == sum(arr[i+1:])), -1)

# traffice peak time
'''
You work for a company that analyzes traffic count at a particular intersection during the peak hours of 4:00 PM to 8:00 PM. Each day, you are given a list that contains the number of vehicles that pass through the intersection every 10 minutes from 4:00 to 8:00 PM.
You are expected to return a list of tuples that each contain the hour and the maximum amount of traffic for each hour.

'''

a2 = [22, 31, 70, 22, 49, 62, 38, 26, 44, 43, 67, 30, 76, 77, 18, 47, 42, 57, 30, 38, 87, 94, 7, 18]
print(len(a2))
def traffic_count(array):
    time = ('4:00pm','5:00pm','6:00pm', '7:00pm')
    max_sec = [max(array[i:i+6]) for i in range(0,len(array),6)]
    return list(zip(time,max_sec)) #tuple(zip(max_sec,time))

def traffic_count(array):
    return [('{}:00pm'.format(i+4), max(array[i*6:(i+1)*6])) for i in range(4)]
print(traffic_count(a2))