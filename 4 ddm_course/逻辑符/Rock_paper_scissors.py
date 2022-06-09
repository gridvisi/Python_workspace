#Rock, paper, scissors.

'''

rock——石头

paper——纸（布）

scissors——剪刀（要用复数，因为剪刀有两片刀刃）
'''

import random
def Rock_Paper_Scissors():
    choice_RPS = ["Rock", "Paper", "Scissors"]
    you = random.choice(choice_RPS)
    me = random.choice(choice_RPS)

    result = f"{you} vs {me}"

    rules = {'win':['Rock vs Scissors',
                    'Scissors vs Paper',
                    'Paper vs Rock'],

            'lose':['Scissors vs Rock',
                 'Paper vs Scissors',
                 'Rock vs Paper']
             }

    for k,v in rules.items():
        if result in v:
            return f"{you} vs {me} : " + f"you {k} me"
        #else:
        #    return 'draw'
    return f"{you} vs {me} : " + f"you draw me"

print(Rock_Paper_Scissors())