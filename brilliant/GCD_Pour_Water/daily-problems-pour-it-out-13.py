# https://brilliant.org/daily-problems/pour-it-out-13/
'''
Today's Challenge
You have two empty containers — one that holds 99 liters
and the other that holds 11.2511.25 liters.



Using these moves:

completely fill a container from the tap
completely empty a container onto the ground
pour a container into the other until it's completely full or
the one pouring is completely empty,\\[-0.7em]
\\[-0.6em]
which one of the following amounts can you measure out exactly?

Hint: What's the smallest amount you can measure?
'''

class Container():
    def __init__(self, content, capacity):
        self.content = content
        self.capacity = capacity
    def empty(self):
        self.content = 0
    def fill(self):
        self.content = self.capacity
    def pour(self, other):
        water_moved = min(self.content, other.capacity - other.content)
        self.content -= water_moved
        other.content += water_moved

c1 = Container(0, 9)
c2 = Container(0, 11.25)
goals = (1.5, 3.25, 5, 6.75)

while not any(c.content in goals for c in (c1, c2)):
    if c1.content == 0:
        c1.fill()
    elif c2.content == c2.capacity:
        c2.empty()
    else:
        c1.pour(c2)
    print(c1.content, c2.content)