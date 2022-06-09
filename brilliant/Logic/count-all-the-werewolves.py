# https://brilliant.org/daily-problems/count-all-the-werewolves/

from itertools import product

result = {"Nayeli": "", "Bashir": "", "Zoe": ""}

for beings in product(["human", "werewolf"], repeat=3):
    result["Nayeli"] = "human" if beings[1] == "werewolf" else "werewolf"
    result["Bashir"] = "human" if beings[2] == "human" else "werewolf"
    result["Zoe"]    = "human" if beings.count("human") == 3 else "werewolf"
    if beings == tuple(result.values()):
        print(result)

#2nd solution
from itertools import compress,product

for is_wolf in product((True,False),repeat=3):
    if is_wolf[0] != is_wolf[1] and is_wolf[1] == is_wolf[2] and is_wolf[2] == any(is_wolf):
        print(f"{is_wolf.count(True)} werewolves:", *compress(('Nayeli', 'Bashir', 'Zoe'), is_wolf))
        break
else:
    print("No solution")


#3rd solution
possibles = [[True, True, True], [True, True, False], [True, False, True], [False, True, True], [True, False, False], [False, True, False], [False, False, True], [False, False, False]]; counter = 0
for i in possibles:
    NayeliStatement = i[0]
    BashirStatement = i[1]
    ZoeStatement = i[2]
    Nayeli = []
    Bashir = []
    Zoe = []
    werewolfCount = 0
    werewolves = "None"
    if NayeliStatement == True:
        Bashir.append("Werewolf")
        Nayeli.append("Human")
    else:
        Bashir.append("Human")
        Nayeli.append("Werewolf")

    if BashirStatement == True:
        Zoe.append("Human")
        Bashir.append("Human")
    else:
        Zoe.append("Werewolf")
        Bashir.append("Werewolf")

    if ZoeStatement == True:
        werewolves = [0]
        Zoe.append("Human")
    else:
        werewolves = [1, 2, 3]
        Zoe.append("Werewolf")

    for i in (set(Nayeli), set(Bashir), set(Zoe)):
        for j in i:
            if j == "Werewolf":
                werewolfCount += 1
    if len(set(Nayeli)) == 1 and len(set(Bashir)) == 1 and len(set(Zoe)) == 1 and werewolfCount in werewolves:
        print("Nayeli is a ", ''.join(set(Nayeli)), "\n", "Bashir is a ", ''.join(set(Bashir)), "\n", "Zoe is a ", ''.join(set(Zoe)), "\n", sep='')
    else:
        counter += 1

    if counter == len(possibles):
        print("There are no solutions.")

