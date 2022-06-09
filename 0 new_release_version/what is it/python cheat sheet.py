
arr = [1,2,3]
tup = (1,2,3)
print(id(arr),id(tup))
arr.append(4)
tup = (1,2,3,4)
print(id(arr),id(tup))

print(set(dir(set)) - set(dir(frozenset)))

_input = ['TS', 'FD','RD' , 'TS', 'FD','TJ', 'FD']
def ordered_count(_input):
    res = []
    for i in _input:
        if i not in res:
            res.append(i)
    it = iter(res)
    return [(next(it), _input.count(i)) for i in res]
print(ordered_count(_input))

for i in _input:
    print(':',_input.count('TS'))


for i in tup:
    print(i)

ls = [1,3,5,7]
it = iter(ls) #让l提供一个能访问自己的迭代器
print(next(it)) #1  从迭代器中取值,让迭代器去获取l中的一个元素
print(next(it)) #3
print(next(it)) #5
print(next(it)) #7
print(next(it)) # StopIterable 异常


class IteratorObjc:
    def __iter__(self):
        self._count = 0
        return self

    def __next__(self):
        while self._count < 3:
            self._count += 1
            return self._count

class IteratorObjc:
    """
    在这种情况下，每次调用__iter__方法时，
    会返回实例对象自身，不会创建具备新id的迭代器对象。
    """
    def __iter__(self):
        # 重置_count，便可反复进行迭代
        self._count = 0
        # 调用时返回实例自身
        return self

    def __next__(self):
        while self._count < 3:
            self._count += 1
            return self._count

a_iterator = IterableObjc()
for i in a_iterator:
    print(i, end=',')
print()
for i in a_iterator:
    print(i, end=',')