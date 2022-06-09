

from itertools import permutations, product

class Person:
    """
    Attributes
    ----------
    name : str
        the person's name
    racket_owner : Person
        the owner of the racket which the person took home
    bottle_owner : Person
        the owner of the water bottle which the person took home
    """
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name} took {self.racket_owner.name}'s racket and {self.bottle_owner.name}'s water bottle."

e = Person("Elaine")
f = Person("Feldman")
g = Person("Gene")
k = Person("Kevin")
people = (e, f, g, k)

for racket_owners, bottle_owners in product(permutations(people), repeat=2):
    for i in range(len(people)):
        if people[i] == racket_owners[i] or people[i] == bottle_owners[i]:
            break
        people[i].racket_owner = racket_owners[i]
        people[i].bottle_owner = bottle_owners[i]
    else:
        # `for-else`: executed if the `for` is not broken
        if e.bottle_owner == f.racket_owner\
        and any(p.bottle_owner == f and p.racket_owner == e for p in people)\
        and g.racket_owner == k:
            print("\n".join([str(p) for p in people]), end="\n\n")