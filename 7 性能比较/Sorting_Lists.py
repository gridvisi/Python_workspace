'''

There are at least two common ways to sort lists in Python:
With sorted function that returns a new list
With list.sort method that modifies list in place
Which one is faster? Let’s find out!
sorted() vs list.sort()
I will start with a list of 1 000 000 randomly shuffled integers.
Later on, I will also check if the order matters.
'''

# sorting.py
from random import sample

# List of 1 000 000 integers randomly shuffled
MILLION_RANDOM_NUMBERS = sample(range(1_000_000), 1_000_000)

def test_sort():
    return MILLION_RANDOM_NUMBERS.sort()

def test_sorted():
    return sorted(MILLION_RANDOM_NUMBERS)
'''
$ python -m timeit -s "from sorting import test_sort" "test_sort()"
1 loop, best of 5: 6 msec per loop

$ python -m timeit -s "from sorting import test_sorted" "test_sorted()"
1 loop, best of 5: 373 msec per loop
'''

'''
Update: As pointed out by a vigilant reader in the comments section, I’ve made a terrible blunder in my benchmarks! timeit runs the code multiple times, which means that:
The first time it runs, it sorts the random list in place.
The second and next time, it runs on the same list (that is now sorted)! And sorting an already sorted list is much faster, as I show you in the next paragraph.
We get completely wrong results because we compare calling list.sort() on an ordered list with calling sorted() on a random list.
Let’s fix my test functions and rerun benchmarks.

更新：正如一位机警的读者在评论区指出的那样，我在基准测试中犯了一个可怕的错误！timeit多次运行代码，这意味着。
第一次运行时，它将随机列表排序在原地。
第二次和下一次，它运行在同一个列表上（现在已经排序了）！而对一个已经排序的列表进行排序，则是一个很复杂的过程。而对已经排序的列表进行排序的速度要快得多，我在下一段向你展示。
我们得到了完全错误的结果，因为我们比较了在一个有序列表上调用list.sort()和在一个随机列表上调用 sorted()。
让我们修正我的测试函数，重新运行基准。
'''
# sorting.py
from random import sample

# List of 1 000 000 integers randomly shuffled
MILLION_RANDOM_NUMBERS = sample(range(1_000_000), 1_000_000)

def test_sort():
    random_list = MILLION_RANDOM_NUMBERS[:]
    return random_list.sort()

def test_sorted():
    random_list = MILLION_RANDOM_NUMBERS[:]
    return sorted(random_list)

'''
his time, I’m explicitly making a copy of the initial shuffled list and then sort that copy (new_list = old_list[:] is a great little snippet to copy a list in Python). Copying a list adds a small overhead to our test functions, but as long as we call the same code in both functions, that’s acceptable.
Let’s see the results:
$ python -m timeit -s "from sorting import test_sort" "test_sort()"
1 loop, best of 5: 352 msec per loop

$ python -m timeit -s "from sorting import test_sorted" "test_sorted()"
1 loop, best of 5: 385 msec per loop
Now, sorted is less than 10% slower (385/352≈1.094). Since we only run one loop, the exact numbers are not very reliable. I have rerun the same tests a couple more times, and the results were slightly different each time. sort took around 345-355 msec and sorted took around 379-394 msec (but it was always slower than sort). This difference comes mostly from the fact that sorted creates a new list (again, as kindly pointed out by a guest reader in the comments).
Initial order matters
What happens when our initial list is already sorted?

'''