'''
https://github.com/emmettgb/Emmetts-DS-NoteBooks/blob/master/Python3/Python%20DataClasses.ipynb
'''

import dataclasses
from dataclasses import dataclass


@dataclass
class Food:
    name: str
    unit_price: float
    stock: int = 0

    def stock_value(self) -> float:
        return (self.stock * self.unit_price)


carrot = Food("Carrot", .45, 25)


class Food:
    name: str
    unit_price: float
    stock: int = 0

    def __init__(self, name: str, unit_price: float, stock: int):
        self.name, self.unit_price, self.stock = name, stock, unit_price

    def stock_value(self) -> float:
        return (self.stock * self.unit_price)


carrot = Food("Carrot", .45, 25)


@dataclass
class Point:
    x: int
    y: int


p = Point(10, 20)
assert dataclasses.asdict(p) == {'x': 10, 'y': 20}