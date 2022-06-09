

class Point:
    """ Point class represents and manipulates x,y coords. """
    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point(4, 3)
q = Point(5, 12)
r = Point() # r代表原点(0, 0)
print(p.x, q.y, r.x)
print(p.distance_from_origin(),q.distance_from_origin())

#将一个实例转换为一个字符串

class Point:
    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):  # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


# 很好地解决了
print(str(p))  # Python now uses the __str__ method that we wrote.
#(3, 4)
print(p)
(3, 4)

def to_string(self):
    return "({0}, {1})".format(self.x, self.y)

p = Point(3, 4)
#print(p.to_string())


def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x) / 2
    my = (p1.y + p2.y) / 2
    return Point(mx, my)
#函数可以返回值为类:
p = Point(3, 4)
q = Point(5, 12)
r = midpoint(p, q)
print(r)


#这个方法与函数完全相同，除了一些重命名之外。它的用法可能是这样的。

p = Point(3, 4)
q = Point(5, 12)
r = p.halfway(q)
print(r)

print(Point(3, 4).halfway(Point(5, 12)))

# 很好地解决了
print(str(p))  # Python now uses the __str__ method that we wrote.
(3, 4)
print(p)
(3, 4)