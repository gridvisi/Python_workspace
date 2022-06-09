'''
https://www.codewars.com/kata/5e1b37bcc5772a0028c50c5d/train/python

You work at a taxi central.
People contact you to order a taxi. They inform you of the time they want to be picked up
and dropped off.

A taxi is available to handle a new customer 1 time unit after it has dropped off a previous
customer.

What is the minimum number of taxis you need to service all requests?

Constraints:
Let N be the number of customer requests:
N is an integer in the range [1, 100k]
All times will be integers in range [1, 10k]
Let PU be the time of pickup and DO be the time of dropoff
Then for each request: PU < DO
The input list is NOT sorted.
Examples:
# Two customers, overlapping schedule. Two taxis needed.
# First customer wants to be picked up 1 and dropped off 4.
# Second customer wants to be picked up 2 and dropped off 6.
requests = [(1, 4), (2, 6)]
min_num_taxis(requests) # => 2

# Two customers, no overlap in schedule. Only one taxi needed.
# First customer wants to be picked up 1 and dropped off 4.
# Second customer wants to be picked up 5 and dropped off 9.
requests = [(1, 4), (5, 9)]
min_num_taxis(requests) # => 1
ALGORITHMSDATA STRUCTURESPRIORITY QUEUESQUEUESARRAYSSCHEDULINGOPTIMIZATION
'''

#1st solution
from heapq import heappush, heappop
def min_num_taxis(requests):
    taxis = [-1]
    #print(taxis)
    for start, end in sorted(requests):
        print(start,end,taxis)
        if taxis[0] < start:
            heappop(taxis)
        heappush(taxis, end)
        print('taxis:',taxis)
    return len(taxis),taxis
requests = [(1, 2), (3, 6)]
requests = [(1,4), (2, 9), (3, 6), (5, 8),(10,13)]
print(min_num_taxis(requests))

#2nd solution
import numpy as np
def min_num_taxis(a):
    r = np.zeros(max(y for _, y in a) + 1)
    for x, y in a:
        r[x:y+1] += 1
    return r.max()


#ericlee solution
from collections import deque
def min_num_taxis(requests):
    if not requests: return 0
    requests.sort(key=lambda x: x[0])
    curr_pos = requests[0]
    requeu = deque(curr_pos)

    taxi = 1
    for i in requests[1:]:

        if requeu and requeu[-1] >= i[0]:
            #reque.append(i)
            taxi += 1
            continue
        curr_pos = i[1]
        requeu.append(i)
        #print('**',curr_pos,i)
    return taxi