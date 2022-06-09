'''
https://www.codewars.com/kata/the-supermarket-queue/train/python
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time:
'''
customers, n = [2,2,3,3,4,4], 2
#customers, n = [2,4,3,2,4,5], 2  #10
customers, n = [1,2,3,4,5],1
#customers, n = [2], 5
#customers, n = [], 1
#customers, n = [1,2,3,4,5], 100
#customers, n = [1,2,3,4,5,6,7], 4
customers,n = [44, 44, 32, 41, 30, 14, 50, 19, 46, 36, 23, 30, 47, 7, 49, 7, 48], 6  #114 should equal 122

def queue_time(customers, n):
    re,res,step = [],[[0]*n],0
    if len(customers) == 1:return customers[0],"wrong answer for a single person in the queue"
    elif len(customers) == 0:return 0,"wrong answer for case with an empty queue"
    elif n > len(customers): return max(customers),"wrong answer for a case with a large number of tills"

    customer = [0] * (1+len(customers)//n)*n
    customer[:len(customers)] = customers[:]
    #print(customer,len(customer))

    for i in range(0,len(customer),n):
        re.append(sorted(customer[i:i+n]))
    #print(re)
    for j in range(len(re)):
        re[j].sort(reverse=True)
        #print(res,re[j])
        res[0] = [res[0][i]+re[j][i] for i in range(n)]
        res[0].sort()
    return max(res[0]),res[0]#"wrong answer for a case with two tills",
print(queue_time(customers, n))  #[[2, 4], [3, 2], [4, 5]]

 #114 should equal 122
#customers, n = [2,4,3,2,4,5], 2  #10
customers, n = [1,2,3,4,5],1
customers, n = [2], 5
#customers, n = [], 1
#customers, n = [1,2,3,4,5], 100
#customers, n = [1,2,3,4,5,6,7], 4
customers,n = [44, 44, 32, 41, 30, 14, 50, 19, 46, 36, 23, 30, 47, 7, 49, 7, 48], 6
def queue_time(customers, n):
    re = customers[:n]
    if len(customers) == 1:return customers[0] #"wrong answer for a single person in the queue"
    elif len(customers) == 0:return 0  #wrong answer for case with an empty queue"
    elif n > len(customers): return max(customers) #"wrong answer for a case with a large number of tills"
    for i,e in enumerate(customers[n:]):
        d = re.index(min(re))
        re[d] += e #customers[n+i]
    return max(re)

def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
print(queue_time(customers, n))


class MarketQueue():

    def __init__(self, customers, n):
        self.customers = customers
        self.n = n
        self.timer = 0
        self.active_checkouts = []

    def calculate_total_time(self):
        while self.customers:
            self.process_queue()
        return self.timer

    def process_queue(self):
        if len(self.active_checkouts) < self.n:
            queue_index = self.n - len(self.active_checkouts)
            self.active_checkouts.extend(self.customers[:queue_index])
            self.customers[:queue_index] = []
        while self.active_checkouts and (len(self.active_checkouts) == self.n or not self.customers):
            self.timer += 1
            self.process_active_checkouts()

    def process_active_checkouts(self):
        finished_customers = []
        for index, customer in enumerate(self.active_checkouts):
            if customer > 1:
                self.active_checkouts[index] = int(customer - 1)
            else:
                finished_customers.append(customer)

        for finished in finished_customers:
            self.active_checkouts.remove(finished)


# implementing requirements
def queue_time(customers, n):
    return MarketQueue(customers, n).calculate_total_time()
'''
Wrong answer for customers = [44, 44, 32, 41, 30, 14, 50, 19, 46, 36, 23, 30, 47, 7, 49, 7, 48] and n = 6: 114 should equal 122
Wrong answer for customers = [13, 7, 41, 36, 16, 9, 28, 26, 14, 16, 49] and n = 6: 56 should equal 76
Wrong answer for customers = [8, 30, 21, 15, 9, 44, 22, 10, 13, 33, 41, 41, 41, 38] and n = 5: 81 should equal 90
Wrong answer for customers = [40, 35, 29, 31, 20, 19, 7, 27, 2, 47, 20, 15, 24, 23, 20, 34, 48] and n = 6: 90 should equal 97
Test Passed
Wrong answer for customers = [14, 9, 44, 44, 5, 21, 26, 4, 48, 23, 50, 23, 20, 41, 42, 10, 47, 7, 8, 26] and n = 4: 142 should equal 141
Wrong answer for customers = [9, 48, 8, 25, 13, 10, 48, 28, 27, 11, 39, 35, 30, 9, 48, 31, 2, 32, 31, 7] and n = 3: 177 should equal 173
Wrong answer for customers = [30, 14, 26, 21, 13, 38, 24, 44, 44, 34, 43, 42, 6, 36] and n = 5: 99 should equal 101
Wrong answer for customers = [40, 21, 41, 23, 15, 26, 23, 43, 18, 4, 39, 35, 2, 43, 3, 41, 7, 1] and n = 4: 122 should equal 127
Wrong answer for customers = [24, 42, 1, 41, 11, 43, 34, 6, 16, 26, 41, 46, 5, 12, 39, 49, 26, 50] and n = 3: 173 should equal 196
 Longer Random Tests
Wrong answer for customers = [7, 3, 24, 16, 29, 47, 31, 42, 18, 16, 31, 38, 39, 50, 37, 46, 44, 11, 26, 15, 1, 29, 28, 41, 5, 26, 11, 5, 11, 1, 2, 27, 27, 19, 48, 3, 44, 39, 18, 50, 29, 39, 20, 16, 23, 4, 26, 9, 49, 32, 34, 43, 3, 34, 41, 44, 48, 11, 26, 26, 31, 42, 44, 20, 45, 24, 14, 3, 8, 17, 3, 39, 26, 28, 48, 31, 14, 45, 27, 5, 8, 13] and n = 5: 424 should equal 433
Wrong answer for customers = [14, 7, 11, 38, 37, 38, 7, 6, 47, 13, 3, 42, 8, 43, 8, 39, 46, 26, 42, 13, 28, 33, 21, 27, 40, 3, 8, 37, 41, 23, 43, 8, 38, 33, 34, 37, 9, 7, 5, 21, 27, 15, 37, 45, 40, 44, 14, 47, 36, 20, 42, 26, 43, 19, 48, 6, 17, 45, 26, 38, 6, 16, 28, 17, 9, 50, 45, 20, 35, 1, 2, 39, 25, 42, 11, 45, 41, 8, 25, 44, 13, 32, 37, 27, 14, 43, 32, 8, 43, 14, 13, 30, 41, 41, 50, 12, 34, 5, 24, 17, 22, 1, 41, 32, 49, 21, 41, 12, 26, 39, 25, 47, 43, 49, 33, 1, 32, 13, 22, 9, 16, 12, 18, 20, 33, 39] and n = 7: 482 should equal 502
Wrong answer for customers = [31, 20, 18, 12, 36, 29, 45, 44, 25, 43, 16, 2, 48, 1, 13, 34, 17, 6, 21, 36, 8, 24, 8, 48, 35, 40, 47, 8, 10, 42, 8, 12, 18, 5, 28, 24, 32, 46, 28, 11, 12, 7, 44, 50, 47, 14, 24, 37, 36, 43, 9, 37, 10, 9, 49, 44, 14, 27, 2, 4, 15, 28, 46, 14, 1, 40, 1, 6, 49, 17, 21, 25, 23, 30, 16, 2, 17, 13, 29, 17, 38, 3, 8, 48, 46] and n = 13: 183 should equal 188
Wrong answer for customers = [23, 37, 43, 14, 25, 5, 40, 8, 4, 2, 29, 3, 15, 18, 44, 36, 11, 7, 10, 50, 3, 43, 14, 43, 7, 5, 12, 37, 14, 25, 34, 43, 44, 18, 31, 39, 21, 20, 41, 13, 2, 4, 4, 39, 38, 15, 14, 28, 15, 17, 40, 30, 27, 24, 16, 38, 48, 4, 15, 8, 49, 28, 13, 47, 38, 2, 33, 5, 18, 45, 38, 48, 32, 12, 34, 12, 18, 17, 11, 42, 8, 32, 28, 19, 31, 28, 44, 16, 16, 25, 36, 29, 2, 48, 14, 16, 24, 42, 26, 28, 15, 29, 9, 42, 42, 16, 40, 42, 3, 32, 24, 10, 28, 37, 6, 11, 3, 11, 25, 50, 21, 11, 7, 30, 37, 34, 4, 21, 17, 7, 18, 11, 7, 46, 41, 34, 2, 12, 33, 12, 2, 13, 17, 47, 49, 14, 17, 43, 40, 4, 28, 24, 38, 29, 15, 29, 21, 14, 48, 29, 32, 44, 33, 10, 32, 47, 7, 33, 36, 45, 20, 17, 33, 47, 15, 36, 12, 6, 20, 10, 25, 13, 17, 2, 16, 37, 28, 1, 38, 46, 18, 46] and n = 12: 403 should equal 411
Wrong answer for customers = [21, 3, 39, 16, 19, 27, 26, 41, 42, 25, 23, 8, 12, 11, 40, 44, 30, 4, 18, 35, 37, 46, 48, 46, 30, 9, 40, 41, 27, 25, 47, 12, 1, 37, 20, 25, 36, 20, 49, 14, 19, 36, 35, 46, 32, 49, 36, 41, 44, 36, 37, 50, 35, 32, 34, 30, 39, 25, 17, 45, 13] and n = 19: 119 should equal 123
Wrong answer for customers = [42, 46, 26, 7, 49, 42, 30, 41, 43, 48, 9, 44, 1, 47, 4, 18, 49, 47, 19, 39, 2, 27, 42, 13, 5, 29, 14, 3, 26, 47, 48, 39, 40, 32, 28, 47, 44, 3, 8, 46, 3, 19, 28, 38, 36, 24, 3, 6, 47, 31, 1, 50, 2, 43, 18, 21, 35, 43, 8, 32, 9, 45, 43, 41, 9, 36, 47, 4, 41, 19, 26, 44, 31, 4, 23, 42, 22, 9, 1, 34, 36, 27, 40, 44, 29, 2, 6, 37, 11, 26, 21, 43, 4, 11, 5, 25, 10, 46, 29, 11, 46, 16, 15, 32, 29, 27, 14, 15, 14, 47, 20, 20, 8, 13, 29] and n = 32: 115 should equal 124
Wrong answer for customers = [40, 35, 31, 5, 17, 46, 11, 3, 43, 12, 30, 11, 15, 11, 21, 45, 26, 20, 3, 29, 45, 22, 25, 23, 35, 24, 9, 4, 6, 13, 8, 39, 8, 39, 49, 47, 16, 24, 47, 6, 43, 2, 5, 41, 6, 42, 30, 39, 39, 46, 9, 10, 22, 6, 14, 23, 20, 5, 24, 16, 49, 16, 11, 36, 10, 9, 38, 21, 5, 48, 6, 21, 28, 39, 12, 3, 50, 49, 34, 18, 24, 38, 25, 3, 41, 46, 48, 10, 45, 24, 4, 34, 47, 29, 46, 22, 32, 26, 9, 28, 6, 15, 30, 6, 19, 40, 12, 35, 13, 5, 30, 32, 17, 3, 18, 9, 41, 19, 43, 17, 8, 22, 3, 38, 47, 43, 2, 47, 23, 1, 24, 25, 37, 6, 38, 36, 24, 21, 18, 26, 7, 8, 39, 38, 48, 10, 27, 11, 36, 33, 3, 31, 41, 7, 49, 46, 37, 2, 47, 12, 36, 7] and n = 25: 181 should equal 183
Wrong answer for customers = [45, 24, 33, 1, 38, 23, 32, 16, 26, 36, 50, 49, 21, 27, 9, 19, 8, 49, 43, 8, 28, 37, 18, 41, 37, 30, 44, 22, 4, 25, 35, 40, 4, 23, 4, 39, 41, 3, 31, 6, 17, 5, 12, 14, 34, 49, 44, 37, 41, 16, 31, 42, 29, 28, 23, 9, 12, 37, 11, 29, 17, 35, 49, 16, 38, 1, 18, 1, 43, 47] and n = 6: 326 should equal 329
Wrong answer for customers = [27, 30, 9, 11, 32, 7, 13, 38, 50, 47, 8, 18, 49, 48, 46, 42, 42, 32, 30, 14, 28, 32, 42, 3, 2, 22, 14, 27, 19, 50, 1, 11, 49, 11, 14, 34, 20, 1, 15, 33, 16, 32, 8, 32, 32, 47, 34, 20, 44, 41, 43, 26, 50, 4, 28, 25, 18, 10, 18, 50, 42, 1, 17, 33, 45, 37, 40, 48, 5, 7, 27, 27, 37, 41, 8, 14, 21, 20, 33, 46, 35, 45, 49, 36, 24, 3, 45, 21, 42, 11, 33, 46, 45, 9, 18, 6, 22, 35, 16, 42, 50, 31, 41, 9, 36, 18, 19, 28, 15, 45, 41, 27, 9, 18, 36, 2, 16, 10, 41, 3, 45, 30, 38, 28, 43, 2, 21, 35, 46, 49, 27, 3, 29, 20, 40, 5, 13, 40, 43, 47, 47, 43, 16, 1, 20, 21, 47, 3, 1, 17, 37, 23, 33, 24, 38, 45, 18, 7, 17, 25, 20, 28, 24, 4, 13, 10] and n = 27: 175 should equal 182
Wrong answer for customers = [22, 36, 5, 49, 12, 49, 1, 48, 38, 21, 42, 14, 37, 4, 14, 5, 47, 38, 42, 46, 46, 13, 27, 30, 10, 25, 35, 29, 46, 18, 46, 13, 37, 36, 23, 23, 21, 41, 26, 18, 29, 31, 6, 12, 40, 15, 50, 39, 5, 26, 16, 28, 3, 20, 22, 3, 47, 43, 27, 35, 46, 2, 49, 10, 15, 44, 47, 24, 11, 40, 48, 41, 21, 24, 31, 26, 7, 30, 31, 19, 29, 1, 4, 46, 8, 34, 25, 8, 43, 42, 44, 32, 2, 40, 49, 42, 18, 47, 8, 8, 45, 7, 11, 24, 6, 19, 16, 44, 12, 20, 14, 39] and n = 28: 117 should equal 132
 Big Number Random Tests
Test Passed
Wrong answer for customers = [20, 28, 90, 22, 11, 96, 132, 50, 112, 25, 116, 126, 88, 93, 106, 67, 97, 24, 24, 12, 139, 16, 44, 105, 78, 34, 75, 17, 85, 107] and n = 13: 228 should equal 223
Wrong answer for customers = [127, 109, 136, 10, 63, 67, 119, 43, 130, 45, 128, 29, 112] and n = 5: 284 should equal 277
Wrong answer for customers = [25, 74, 98, 76, 86, 94, 39, 100, 54, 91, 145, 50, 45, 47, 28, 113, 111, 78, 48, 113, 135, 131, 57, 135, 80, 38, 104, 12, 142, 84, 113, 66, 14, 107, 136, 132, 82, 83, 142, 73, 43, 131, 105] and n = 12: 341 should equal 360
Wrong answer for customers = [48, 111, 62, 147, 99, 30, 32, 120, 142, 142, 52, 65, 109, 52, 84, 45, 73, 80, 59, 110, 56, 56, 62, 66, 42, 117, 28, 76, 90, 103, 147, 49, 129, 64, 102, 52, 57, 20, 140, 60, 19, 52, 59, 103] and n = 5: 712 should equal 724
Test Passed
Wrong answer for customers = [62, 120, 123, 33, 88, 131, 104, 119, 41, 55, 126, 16, 129, 140, 79, 28, 148, 48, 96, 18, 38, 64, 101] and n = 8: 295 should equal 297
Wrong answer for customers = [66, 61, 92, 62, 140, 120, 30, 67, 112, 108, 52, 12, 13, 112, 90, 103, 140, 37, 109, 104, 94, 83, 140, 77, 69, 141, 30, 59, 150, 78, 84, 121, 58, 12] and n = 4: 721 should equal 752
Wrong answer for customers = [41, 34, 39, 123, 20, 17, 139, 104, 104, 77, 20, 58, 77, 133, 138, 88, 27, 44] and n = 3: 446 should equal 449
Wrong answer for customers = [56, 118, 42, 123, 28, 122, 120, 135, 87, 87, 57, 38, 147, 89, 115, 55, 145, 22, 139, 100, 74, 134, 113, 81, 121, 57, 75, 133, 36, 64, 128, 105, 31, 74, 73, 133, 86, 132, 27, 56, 148, 51, 129, 122, 92, 149, 11, 122] and n = 14: 378 should equal 397


a,b = [1,2,3],[4,5,6]
print([a[i]+b[i] for i in range(len(a))])
print(customers.sort()) #None
print(customers)
print(sorted(customers))
print(customers)

    for i in range(0,len(customers),n):
        if step % 2 == 0:
            re.append(sorted(customers[i:i+n]))
        elif step % 2 == 1:
            re.append(sorted(customers[i:i + n],reverse = True))
        step += 1
        print(step)
        
    for i in range(len(re)):
        if i%2 == 0:
            re[i] = sorted(re[i])
        elif i % 2 == 1:
            re[i] = sorted(re[i],reverse = True)
    
'''