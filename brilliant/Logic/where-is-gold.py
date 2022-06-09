'''
https://brilliant.org/daily-problems/where-is-gold/
Four chests (A, B, C, and D) each have a statement pinned to them, and these four
bullet points are true statements:

Each chest contains either rocks or gold, but not both.

One chest is labeled with a false statement.

Three chests are labeled with true statements.

The "True" and "False" labels are accurate, given what each statement claims about
what's in each chest.



'''

from itertools import product
class Chest:
    def __init__(self, name, statement):
        self.name = name
        self.statement = statement

a = Chest("A", lambda: all(chest.content == "rocks" for chest in chests if chest.label == True))
b = Chest("B", lambda: c.content == "gold" and d.content == "gold")
c = Chest("C", lambda: b.label == False)
d = Chest("D", lambda: all(chest.label == True for chest in chests if chest.content == "rocks"))
chests = (a, b, c, d)

for contents in product(("rocks", "gold"), repeat=4):
    for labels in product((True, False), repeat=4):
    #for labels in product((True, False), repeat=4):
        if sum(labels) != 3:
            continue
        for i in range(4):
            chests[i].content = contents[i]
            chests[i].label = labels[i]
        if all(chest.statement() == chest.label for chest in chests):
            for chest in chests:
                #print("Chest {} is labeled with a {} statement and contains {}.".format(chest.name, str(chest.label).lower(), chest.content))
                print(f"{chest.name} tell {chest.label} and have {chest.content}")