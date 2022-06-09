class Queue:
    def __init__(self, arr=[]):
        self.arr = arr
        self.wait_time = sum(i for i in arr)

    def enqueue(self, num):
        self.arr.append(num)
        self.wait_time += num

    def dequeue(self):
        return self.arr.pop(0)


def queue_time(customers, n):
    # TODO
    customer_queue = Queue(customers)
    if n == 1:
        return customer_queue.wait_time

    queues = [Queue([]) for i in range(n)]
    while len(customer_queue.arr) >= 1:
        wait = [k.wait_time for k in queues]
        for i in queues:
            if i.wait_time == min(wait) or i.wait_time == 0:
                i.enqueue(customer_queue.dequeue())
                break

    return max([i.wait_time for i in queues])

print(queue_time([2,2,3,3,4,4], 2))

print(queue_time([8,2,3,5,4,4], 3))

print(queue_time([1,2,3,4,5,6], 3))