from collections import deque

def dead_live(person,nth):
    circle_1 = [i for i in range(nth,person)]
    circle_2 = [i for i in range(nth)]
    circle = circle_1 + circle_2
    d, result = deque(circle), []
    while d:
        result.append(d.popleft())
        d.rotate(-(nth-1))
    return result

person,nth = 41,3

print(dead_live(person,nth))