
user_input = "This\nstring has\tsome whitespaces...\r\n"

character_map = {
    ord('\n') : ' ',
    ord('\t') : ' ',
    ord('\r') : None
}
print(user_input,character_map)

import itertools
s = itertools.islice(range(50), 10, 20)
# <itertools.islice object at 0x7f70fab88138>
for val in s:
    print(val)
string_from_file = """

// Author: ...

// License: ...

//

// Date: ...

Actual content...

"""

import itertools
for line in itertools.dropwhile(lambda line: line.startswith("//"), string_from_file.split("\n")):
    print(line)

#4 只带关键字参数的函数（kwargs）
#  创建只接受关键字参数以在使用此类函数时提供（强制）更清晰的函数可能会有帮助：
def test(*, a, b):
    pass
test("value for a", "value for b")  # not good!
# TypeError: test() takes 0 positional arguments...
test(a="value", b="value 2")  # Works...
#如您所见，将单个*参数放在关键字参数之前可以很容易地解决这个问题。如果将位置参数放在*参数之前，
# 显然会需要有位置参数。


class Connection:
    def __init__(self):

    def __enter__(self):
    # Initialize connection...

    def __exit__(self, type, value, traceback):
    # Close connection...

with Connection() as c:
    # __enter__() executes
    ...
​   # conn.__exit__() executes