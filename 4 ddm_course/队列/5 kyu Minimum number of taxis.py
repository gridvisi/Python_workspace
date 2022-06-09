'''
https://www.codewars.com/kata/5e1b37bcc5772a0028c50c5d/train/python

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

Test.describe("Example test cases.")

one_req = [(1,4)] # One request, one taxi.
Test.assert_equals(min_num_taxis(one_req), 1)

two_reqs = [(1,4), (5, 9)] # Two requests, one taxi.
Test.assert_equals(min_num_taxis(two_reqs), 1)

three_reqs = [(1,4), (2, 9), (3, 6)] # Three requests, three taxis.
Test.assert_equals(min_num_taxis(three_reqs), 3)

four_reqs = [(1,4), (2, 9), (3, 6), (5, 8)] # Four requests, three taxis.
Test.assert_equals(min_num_taxis(four_reqs), 3)
'''

requests = [(1,4), (2, 9), (3, 6), (5, 8)]  #3

requests.sort()
#print(requests)

from collections import deque
def min_num_taxis(requests):
    if not requests: return 0
    requests.sort(key=lambda x: x[0])
    curr_pos = requests[0]
    requeu = deque(curr_pos)

    taxi = 1
    for i in requests[1:]:
        print(requeu[-1],i)
        if requeu and requeu[-1][1] >= i[0]:
            #reque.append(i)
            taxi += 1
            continue
        curr_pos = i[1]
        requeu.append(i)
        #print('**',curr_pos,i)
    return taxi

requests = [(1,4), (3, 6), (2, 9), (5, 8),(4,7),(8,10)]
print(min_num_taxis(requests))


'''
if not a1: return a2
    elif not a2: return a1
'''
# Not good short case
def min_num_taxis(requests):
    lap = requests[0]
    cunt = 1
    for t in requests[1:]:
        if t[0] <= lap[1]:cunt += 1
        lap = [max([lap[0],t[0]]),min([lap[1],t[1]])]
    return lap,cunt
print(min_num_taxis(requests))

# more input than test case 
def min_num_taxis(requests):
    if not requests: return 0
    requests.sort(key=lambda x: x[0])
    print(requests)
    curr_pos = requests[0][1]
    ans = 1
    for i in range(1,len(requests)):
        print(curr_pos, requests[i][0])
        if curr_pos >= requests[i][0]:
            ans += 1
            continue
        curr_pos = requests[i][1]
        #continue
        print(print(curr_pos, requests[i][0]))
    return ans



# Bruce force is not surtisfied with time limited accept
def min_num_taxis(requests):
    taxiMax = []
    start, end = min(requests, key=lambda x: x[0])[0], max(requests, key=lambda x: x[1])[1]
    for i in range(start, end):
        taxi = [int(slot[0] <= i <= slot[1]) for slot in requests]
        # print(taxi)
        taxiMax.append(taxi)
    return sum(max(taxiMax))