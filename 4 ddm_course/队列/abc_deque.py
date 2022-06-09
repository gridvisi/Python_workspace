'''
二.模块 collections 中的一个类—— deque。
deque类里有方法：
例子：d.append('x') 添加x到d的右端,不返回
d.appendleft('xx) 添加xx到d的左侧，不返回
d.clear() 清空
d.count(x) 统计x的个数
d.extend（可迭代的类型）  会把每个元素添加到d
d.index(x)返回x的索引，不存在的话报错
d.pop()删除右边的一个，没有就报错
d.remove(x) 去除x，不存在就报错
d.reverse()倒叙
rotate(n) 向右循环移动n，如果n是负数，就向左循环
例子：
d.rotate(1)
d
deque([1, 'a', 'd', 'f', 'g', 'h'])
d.rotate(1)
d
deque(['h', 1, 'a', 'd', 'f', 'g'])

 from collections import deque
 d=deque('abc')
 for i in d:
     print(i)


'''


class Queue:

    # create the constructor
    def __init__(self):

        # create an empty list as the items attribute
        self.items = []

    def enqueue(self, item):
        """
        Add item to the left of the list, returns Nothing
        Runs in linear time O(n) as we change all indices
        as we add to the left of the list
        """
        # use the insert method to insert at index 0
        self.items.insert(0, item)

    def dequeue(self):
        """
        Removes the first item from the queue and removes it
        Runs in constant time O(1) because we are index to
        the end of the list.
        """
        # check to see whether there are any items in the queue
        # if so then we can pop the final item
        if self.items:

            return self.items.pop()
        # else then we return None
        else:
            return None

    def peek(self):
        """
        Returns the final item in the Queue without removal

        Runs in constant time O(1) as we are only using the index
        """
        # if there are items in the Queue
        if self.items:
            # then return the first item
            return self.items

        # else then return none
        else:
            return None

    def is_empty(self):
        """
        Returns boolean whether Queue is empty or not
        Runs in constant time O(1) as does not depend on size
        """
        return not self.items

    def size(self):
        """
        Returns the size of the stack
        Runs in constant time O(1) as only checks size
        """
        # len will return 0 if empty
        # so don't need to worry about empty condition
        return len(self.items)

    def __str__(self):
        """Return a string representation of the Stack"""
        return str(self.items)