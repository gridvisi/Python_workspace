__author__ = 'Administrator'
#from brilliant import goldgrid
#coins = goldgrid.grid()
#height, width = goldgrid.height(coins), goldgrid.width(coins)

#Initializing the dictionary for the maximum coins up to a certain cell
#max_coins = {(0,0) : coins[(0,0)]}

#Computing the max_coins values for the first column and row
#The maximum coins is the maximum for the cell prior to it, plus the coins in that cell
for row in range(1,height):
    max_coins[(0,row)] = max_coins[(0,row-1)] + coins[(0,row)]

for column in range(1,width):
    max_coins[(column,0)] = max_coins[(column-1,0)] + coins[(column,0)]

#Using recursion / dynamic programming to find the remaining maximums
for row in range(1,height):
    for column in range(1,width):
        max_coins[(column,row)] = #FILL ME IN

#Print the maximum value for the top right cell
print(max_coins[(width-1,height-1)])