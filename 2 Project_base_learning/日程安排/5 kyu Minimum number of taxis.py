# https://www.codewars.com/kata/5e1b37bcc5772a0028c50c5d/train/python
'''
Test.describe("Example test cases.")

one_req = [(1,4)] # One request, one taxi.
Test.assert_equals(min_num_taxis(one_req), 1)

two_reqs = [(1,4), (5, 9)] # Two requests, one taxi.
Test.assert_equals(min_num_taxis(two_reqs), 1)

three_reqs = [(1,4), (2, 9), (3, 6)] # Three requests, three taxis.
Test.assert_equals(min_num_taxis(three_reqs), 3)

four_reqs = [(1,4), (2, 9), (3, 6), (5, 8)] # Four requests, three taxis.
Test.assert_equals(min_num_taxis(four_reqs), 3)


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
'''

requests = [(1,4), (2, 9), (3, 6), (5, 8)]
print(max(requests,key=lambda x:x[1]))
print(min(requests,key=lambda x:x[0]))

def min_num_taxis(requests):
    ans = []
    for s in requests:
        num = [int(slot[0]<s[0]<slot[1]) for slot in requests]
        ans.append(num)
    return ans
print(min_num_taxis(requests))


def min_num_taxis(requests):
    taxiMax = []
    start,end = min(requests,key=lambda x:x[0])[0],max(requests,key=lambda x:x[1])[1]
    for i in range(start,end):
        taxi = [int(slot[0] <=i<= slot[1]) for slot in requests]
        #print(taxi)
        taxiMax.append(taxi)
    return sum(max(taxiMax))
'''
Execution Timed Out
 STDERR
Execution Timed Out (12000 ms)
'''
