# https://brilliant.org/daily-problems/comparing-heights/

'''

Kim, Leo, Mia, and Nil are comparing their heights in centimeters. They learn these:

Nil is \SI{3}{\cm}3 cm taller than Kim.
Mia is \SI{6}{\cm}6 cm taller than Leo.
Mia's height is the arithmetic average of Leo's and Nil's heights.
If we order the children from the shortest to the tallest, where does Kim rank?
'''

# What does mean that "from the shortest to the tallest?"

rank = []
for leo in range(1,100):
    #rank['leo'] = leo
    mia = leo + 6
    nil = mia * 2 - leo  #mia*2 = leo + nil
    kim = nil - 3        #nil = kim + 3
    rank.append([leo,mia,nil,kim])
print([sorted(person).index(person[3]) for person in rank])


print(sorted([2,3,4,5,6],reverse=True))