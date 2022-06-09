'''
https://brilliant.org/problems/life-and-death-in-the-desert/
This problem is a simpler version of the Knapsack problem.
It can be solved recursively.Let Cap(x)Cap(x) be the maximum amount of water that can be carried for a weight limit of xx. And let vv be the set of the values of the smaller bottles.We can define recursively as Cap(x)=max( \left\{ Cap(x-{v}_{0})+{v}_{0} , Cap(x-{v}_{1})+{v}_{1},Cap(x-{v}_{2})+{v}_{2} ...,Cap(x-{v}_{i})+{v}_{i} \right\} )Cap(x)=max({Cap(x−v
We are basically subtracting each value of the set of bottle(v)v)
values from the limit(15kg15kg) and seeing which difference
yields the maximum value..

This can be implemented easily in python..

print Cap(1500,[77,110,340,700])/100.0
Note:I multiplied each bottle value by 100100,since it is easier to deal with integers.
'''


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
    for value in values:
        if value > Capacity:
            vs.append(0)
        else:
            vs.append(Cap(Capacity-value,values)+value)
    Save[Capacity] = max(vs)
    print(Save)
    return max(vs)
print(Cap(1500,[77,110,340,700]))

