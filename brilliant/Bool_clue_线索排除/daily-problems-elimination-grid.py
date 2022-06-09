'''

https://brilliant.org/daily-problems/elimination-grid/

Annie does not live in the red house.
The fish lives in the orange house, which is not Annie's.
Becca owns the lizard and does not live in the yellow house.
Dante's house is red.
The hamster lives in the yellow house.
'''

name = ['Annie','Becca','Carlos','Dante']
house = ['red','orange','yellow','green']
animal = ['bird','lizard','hamster','fish']

comb = []
for n in name:
    for h in house:
        for a in animal:
            comb.append([n,h,a])


# Try first
for i in comb:
    if i.count('Annie') and 'red' not in i and 'orange' not in i:
        print('1',i)
        if i.count('fish') and 'orange' in i:
            print('2',i)
            if i.count('Becca') and 'lizard' in i and 'yellow' not in i:
                print('3',i)
                if 'Dante' in i and 'red' in i:
                    print('4',i)


# Try 2nd:

one,two,three,four = [],[],[],[] #list([] * 4)
print('s:',[[]]*4)

for i in comb:
    if i.count('Annie') and 'red' not in i and 'orange' not in i:
        print('1',i)
        one.append(i)

for i in comb:
    if i.count('fish') and 'orange' in i:
        print('2',i)
        two.append(i)

for i in comb:
    if i.count('Becca') and 'lizard' in i and 'yellow' not in i:
        print('3',i)
        three.append(i)

for i in comb:
    if 'Dante' in i and 'red' in i:
        print('4',i)
        four.append(i)


for o in one:
    for t in two:
        for r in three:
            for f in four:
                s = o+t+r+f
                #print(set(s))
                if len(set(s)) == 12:
                    print('res:',o,t,r,f)

#print(set(one) and set(two) and set(three) and set(four))

#['Annie', 'yellow', 'bird'] ['Carlos', 'orange', 'fish'] ['Becca', 'green', 'lizard'] ['Dante', 'red', 'hamster']
#['Annie', 'yellow', 'hamster'] ['Carlos', 'orange', 'fish'] ['Becca', 'green', 'lizard'] ['Dante', 'red', 'bird']


# Try 3rd:

one,two,three,four = [],[],[],[] #list([] * 4)
print('s:',[[]]*4)

for i in comb:
    if i.count('Annie') and 'red' not in i and 'orange' not in i:
        print('1',i)
        one.append(i)

#for i in comb:
    if i.count('fish') and 'orange' in i:
        print('2',i)
        two.append(i)

#for i in comb:
    if i.count('Becca') and 'lizard' in i and 'yellow' not in i:
        print('3',i)
        three.append(i)

#for i in comb:
    if 'Dante' in i and 'red' in i:
        print('4',i)
        four.append(i)


for o in one:
    for t in two:
        for r in three:
            for f in four:
                s = o+t+r+f
                #print(set(s))
                if len(set(s)) == 12:
                    print('3rd:',o,t,r,f)



# Try 4th:

one,two,three,four,five = [[]]*5
print('s:',[[]]*4)

for i in comb:
    if 'Annie' in i and 'red' not in i:
        #print('1',i)
        one.append(i)

for i in comb:
    if 'Annie' not in i and 'fish' in i and 'orange' in i:
        #print('2',i)
        two.append(i)

for i in comb:
    if 'Becca' in i and 'lizard' in i and 'yellow' not in i:
        #print('3',i)
        three.append(i)

for i in comb:
    if 'Dante' in i and 'red' in i:
        #print('4',i)
        four.append(i)

for i in comb:
    if 'hamster' in i and 'yellow' in i:
        #print('5',i)
        five.append(i)
'''

for o in one:
    for t in two:
        for r in three:
            for f in four:
                for v in five:
                    s = o+t+r+f+v
                    #print(set(s))
                    if len(set(s)) == 12:
                        #print('res:',o,t,r,f,v)

'''

'''

Annie does not live in the red house.
The fish lives in the orange house, which is not Annie's.
Becca owns the lizard and does not live in the yellow house.
Dante's house is red.
The hamster lives in the yellow house

name = ['Annie','Becca','Carlos','Dante']
house = ['red','orange','yellow','green']
animal = ['bird','lizard','hamster','fish']
'''
animal = ['bird','lizard','hamster','fish']

graph_name = {
         'Annie':['yellow','green'],
         'Becca':['orange','green'],
         'Carlos':['orange','yellow','green'], #因为annie和Becca组合后每一种可能
         'Dante':['red']
             }


graph_house = {
            'red': ['bird','lizard'],
            'orange': ['fish'],
            'yellow': ['hamster'],
            'green': ['bird','lizard']
            }

graph_animal = {
         'bird':['Annie','Carlos','Dante'],
         'lizard':['Becca'],
         'hamster':['Annie','Carlos'], #Dante's house is red.
         'fish':['Carlos','Dante']  #The fish lives in the orange house, which is not Annie's.
        }

clue = []
for k,v in graph_name.items():
    #clue.extend(k)
    for i in v:
        for j in graph_house[i]:
            for l in graph_animal[j]:
                if k == l:
                    clue.append([k,i,j])
print('clue:',clue)
