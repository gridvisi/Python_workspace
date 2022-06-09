
#1st solution
arrs = ['a','b',['c','d',['e',['a','b',['c','d',['e']]]]]]
def flatarrs(arrs):
    ans = []
    for arr in arrs:
        if type(arr) == str:
            ans.append(arr)
            yield arr
        else:
            yield from flatarrs(arr)
print(list(flatarrs(arrs)))

import collections

def flatten(iterable):
    iterator = iter(iterable)
    array, stack = collections.deque(), collections.deque()

    while True:
        try:
            value = next(iterator)

        except StopIteration:
            if not stack:
                return tuple(array)
            iterator = stack.pop()

        else:
            if not isinstance(value, str) and isinstance(value, collections.Iterable):
                stack.append(iterator)
                iterator = iter(value)

            else:
                array.append(value)



def main():
    data = [1, 2, [3, 4, [5], []], [6]]
    print(list(flatten(data)))


def flatten(iterable):
    iterator, sentinel, stack = iter(iterable), object(), []
    while True:
        value = next(iterator, sentinel)
        if value is sentinel:
            if not stack:
                break
            iterator = stack.pop()

        elif isinstance(value, str):
            yield value

        else:
            try:
                new_iterator = iter(value)

            except TypeError:
                yield value
            else:
                stack.append(iterator)
                iterator = new_iterator

if __name__ == '__main__':
    main()

