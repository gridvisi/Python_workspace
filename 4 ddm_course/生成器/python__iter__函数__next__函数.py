
class test():
    def __init__(self,data=1):
        self.data = data

    def __iter__(self):
        return self
    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data+=1
            return self.data

for item in test(3):
    print(item)

class test():
    def __init__(self,data=1):
        self.data = data

    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data+=1
            return self.data

t = test(3)
for i in range(3):
    print(t.__next__())

def fib(end = 1000):
    prev,curr=0,1
    while curr < end:
        yield curr
        prev,curr=curr,curr+prev

print(list(fib()))