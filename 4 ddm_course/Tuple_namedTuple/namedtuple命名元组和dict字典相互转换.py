
from collections import namedtuple

dct = {
    "name": "Tom",
    "age": 24
}

Person = namedtuple("Person", ["name", "age"])

# 字典转为namedtuple
person = Person._make(dct)
print(person)
# Person(name='name', age='age')

# namedtuple转为字典
print(person._asdict())
# OrderedDict([('name', 'name'), ('age', 'age')])
