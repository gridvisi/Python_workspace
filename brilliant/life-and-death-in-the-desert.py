#https://brilliant.org/problems/life-and-death-in-the-desert/

Save = {} #Always save values when using recursive functions
          #it saves a lot of time and avoids recomputation
def Cap(Capacity,values):
    if Capacity in Save:
        return Save[Capacity]
    vs = []
    if Capacity in values:
        return Capacity
    if Capacity <= 0:
        return 0
    s = 0
    for value in values:
        s += 1
        if value > Capacity:
            vs.append(0)

        else:

            print(f'{s}'+' (',vs, value,Capacity,Save)
            vs.append(Cap(Capacity-value,values)+value)
            print(f'{s}'+' )',vs, value, Capacity, Save)

    Save[Capacity] = max(vs)
    print('Save:',Save,Save[Capacity])
    return max(vs)

#print(Cap(1500,[77,110,340,700])/100.0)
print(Cap(107,[5,10]))