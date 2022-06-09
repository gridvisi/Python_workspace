'''
https://brilliant.org/problems/air-tickets-reservation-program/

Air tickets reservation program
Computer Science Level 2
The following pseudo-code is used to find the next available seat in airplanes.

for \ row \ = \ A \ to \ F \ \ do \\ \ \ \ for \ column \ = \ 1 \ to \ 13 \ \ do \\ \ \ \ \ \ \ if \ a \ seat \ (row, \ column) \ is \ available \\ \ \ \ \ \ \ \ \ \ then \ book \ the \ seat \ and \ mark \ it \ occupied \\ \ \ \ next \ \ column \\ next \ \ rowfor row = A to F  do
   for column = 1 to 13  do
      if a seat (row, column) is available
         then book the seat and mark it occupied
   next  column
next  row

The given \text{AIRPLANE SEATING DIAGRAM }AIRPLANE SEATING DIAGRAM  shows the occupied and available seats.

After booking 5151 seats what will be the actual seat number for the next available seat?

https://zhuanlan.zhihu.com/p/88197389
'''

A_04 = [1,1,1,0,1]
first_s = 'emma'
A_04[0] = first_s
print('a04',A_04)

A_05 = []
A = [A_04,A_05]


seats = [[1]*6]*13
print(seats)
seats[0][1] = 0
print(seats)

seat = [[0,0],[0,0],[0,0]]
seat[1][1] = 1
print(seat)

seats = [[1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]]
seats[2][2] = 0

print('taken',seats[2][2],seats[2])



seats[0][1], seats[0][3]= 0,0
seats[1][2] = 0
seats[3][4] = 0
seats[4][2], seats[4][3],seats[4][4], seats[4][5]= 0,0,0,0
seats[5][3], seats[5][5] = 0,0
seats[7][1] = 0
seats[8][3] = 0
seats[11][2] = 0
seats[12][2], seats[12][4],seats[12][5]= 0,0,0

print(seats)
print(seats[2])
print(len(seats))


# firstly 1-13,then A-F
def seatsPos(arr,seq):
    for s in range(len(seats)):
    #print(seats[s])
        for j in range(len(seats[s])):
            #print(j)
            seq -= 1
            if seq == 0:
                arr = seats[s][j]
                return arr

# 8 5


#矩阵转置
seq = 54
arr = seats

seatsTrans = [[1]*13]*6
def trans(arr):
    seatsTrans = list(map(list, zip(*arr)))
    return seatsTrans
print('arr:',seatsPos(arr,seq),trans(arr))


#Transform array
'''
seatsTrans = [[1]*13]*6
#print('initial:',seatsTrans)

[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], 
[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1], 
[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0], 
[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0]]

Process finished with exit code 0
'''

seatsTrans = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
              [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
              [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0]]

seatsTrans = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
              [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
              [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
              [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0]]

print('windows:',seatsTrans[0],seatsTrans[5],seatsTrans[-1])

print('by aisle:',seatsTrans[2],seatsTrans[3])

print(trans(arr) == seatsTrans)
# firstly A-F,then 1-13

def books(booked,seatsTrans):
    row = ['A', 'B', 'C', 'D', 'E', 'F']
    rowDict = dict(zip(range(len(row) + 1), row))
    colKey = [i for i in range(13)]
    colsDict = dict(zip(colKey, [i + 2 if i >= 12 else i for i in range(2, 16)]))

    for row in range(len(row)):
        # alphaZip[row]=A->F
        for col in colKey:
            if seatsTrans[row][col] != 0:
                booked -= 1
                if booked == 0:
                    return rowDict[row],colsDict[col]
booked = 51
print('seatsTarget:',books(booked,seatsTrans))


# 4 1

 #= [[1]*6]*13
def trans(arr,together):
    seatsTransed = list(map(list, zip(*arr)))

    row = ['A', 'B', 'C', 'D', 'E', 'F']
    rowDict = dict(zip(range(len(row) + 1), row))
    colKey = [i for i in range(13)]
    colsDict = dict(zip(colKey, [i + 2 if i >= 12 else i for i in range(2, 16)]))

    for i,col in enumerate(seatsTransed):
        for row in range(len(col)):
            if sum(col[row:row+together])==together:
                print(col,row)

                return colsDict[i],','.join([rowDict[i] for i in range(row,row+3)])
    return f"There's not {together} seats together"
together = 6
arr = seatsTrans
print('arr:',trans(arr,together))






'''
def trans(m):
    for i in range(len(m)):
        for j in range(i):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    return m
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(trans(m))
'''