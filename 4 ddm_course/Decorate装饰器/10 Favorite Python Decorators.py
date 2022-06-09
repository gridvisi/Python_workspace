'''
https://github.com/emmettgb/Emmetts-DS-NoteBooks/blob/master/Python3/10%20Python%20Decorators.ipynb
'''

from multipledispatch import dispatch
class Pasta:
    def __init__(self, width, height, classification):
        self.width, self.height = width, height
        self.classification = classification
    def classify(self):
        if self.width == 2 and self.height == 2:
            self.classification = "Linguine"
        elif self.width == self.height and self.width < 3:
            self.classification = "Spaghetti"
        elif self.width == 4 and self.height == 1:
            self.classification = "Fettuccine"
        else:
            self.classification = "Dough"

class Bread:
    def __init__(self, width, height, classification):
        self.width, self.height = width, height
        self.classification = classification
    def bake(self):
        if self.width == 3 and self.height == 2:
            self.classification = "Pizza Crust"
        elif self.width == self.height and self.width < 3:
            self.classification = "White bread"
        elif self.width > 2 and self.height == 1:
            self.classification = "Flatbread"
        else:
            self.classification = "Dough"

class Roller:
    def __init__(self):
        pass
    @dispatch (Pasta)
    def roll_thinner(self, x : Pasta):
        x.height -= 1
        x.width += 1
        x.classify()
    @dispatch (Pasta)
    def cut(self, x : Pasta):
        x.width -= 1
        x.classify()
    @dispatch (Pasta)
    def fold(self, x : Pasta):
        x.width += 1
        x.classify()
    @dispatch (Bread)
    def roll_thinner(self, x : Bread):
        x.height -= 1
        x.width += 1
        x.bake()
    @dispatch (Bread)
    def cut(self, x : Bread):
        x.width -= 1
        x.bake()
    @dispatch (Bread)
    def fold(self, x : Bread):
        x.width += 1
        x.bake()

def make_dough(pasta = False):
    if pasta:
        return(Pasta(10, 10, "Dough"))
    else:
        return(Bread(10, 10, "Dough"))

dough = make_dough()
print(dough.classification)

pasta_dough = make_dough(pasta = True)
rollingpin = Roller()
while pasta_dough.height >= 3:
    rollingpin.roll_thinner(pasta_dough)
print(pasta_dough.height)
print(pasta_dough.width)

while pasta_dough.width > 2:
    rollingpin.cut(pasta_dough)
print(pasta_dough.classification)


rollingpin.roll_thinner(dough)


import click

@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()

#deprecated


from deprecated import deprecated
@deprecated ("This function is deprecated, please do not make dough here")
def make_dough(pasta = False):
    if pasta:
        return(Pasta(10, 10, "Dough"))
    else:
        return(Bread(10, 10, "Dough"))

z = make_dough()


from deco import concurrent, synchronized
@concurrent
def roll_linguine(count : int):
    rollingpin = Roller()
    pastas = []
    for i in range(0, count):
        dough = make_dough(pasta = True)
        while dough.height >= 3:
            rollingpin.roll_thinner(dough)
        while dough.width > 2:
            rollingpin.cut(dough)
        pastas.append(dough)
    return(pastas)
%timeit roll_linguine(100000)

@concurrent
def roll_pizzas(count : int):
    rollingpin = Roller()
    pizzas = []
    for i in range(0, count):
        dough = make_dough()
        while dough.height > 3:
            rollingpin.roll_thinner(dough)
        while dough.width > 2:
            rollingpin.cut(dough)
%timeit roll_pizzas(500)