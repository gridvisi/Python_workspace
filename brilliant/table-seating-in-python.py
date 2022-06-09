#https://brilliant.org/problems/table-seating-in-python/
'''
Table seating in python
Computer Science Level 4
You may have encountered a problem on Brilliant about seating people around a long table made out of n-sided tables of equal side lengths. This one goes a little bit further.
You are preparing a big feast. You need to create one long table from small regular shaped n-lateral tables. We illustrate this in the picture bellow. You may seat one and only one person at each side of the small table.
What is the sum of all posible side numbers (triangle = 3, square = 4 etc.) you can use to seat 112 people?
Although this can be done on paper, try to use python and let the computer do the job!

def full_table(person):
    res = []
    for side in range(3,person+1):
        if (person-2*(side-1)) % (side-2) == 0:
            table = (person-2*(side-1))//(side-2)
            res.append((side,table+2))
    return res
person = 30
print(full_table(person))
'''
def table_seat(n,person):  # good solution
    table,seat = 1,n
    if person <= n:
        return table,person,seat,seat-person

    while person > n:
        table += 1
        seat += n-2
        person -= n-2
    if person <= n:
        #if person - 1 == n - 1:
        #    return table, person - 1, seat, (n - 1) - (person - 1)
        return table,person-1,seat,(n-1)-(person-1)

n, person = 17, 47
#n, person = 4, 8
#n, person = 4, 9
n, person = 5, 11
print(table_seat(n, person))





def table_seat(n,person):  # wrong solution
    seat,table = 0,1
    person = person - table*(n)
    seat = table*n
    if person <= 0:return table,person+table*(n),seat
    elif person > 0:
        person += 1
        seat -= 1
        #print(table,person,seat)
        if person < n-2:
            return table+1,person,seat+n-1
        while person >= n-2:
            person -= n-2
            table += 1
            seat += n-2
        #table += 1
        #seat += n-2
        return n,table,person+n-2,seat+1
n,person = 17,33
print(table_seat(n,person))


# Final Result
result = 0
for number_of_sides in range(3, 113):
    number_of_shapes = 112 - 2 * ( number_of_sides - 1 )
    number_of_shapes /= ( number_of_sides - 2 )
    # Since the end shapes are not taken into account
    number_of_shapes += 2
    # Only add result, if number of shapes is a whole number
    if number_of_shapes == number_of_shapes // 1 :
        result += number_of_sides
print('Result = ', result)

count = 0
for n in range(3, 113):
    if 110 % (n - 2) == 0:
        count += n
print(count)