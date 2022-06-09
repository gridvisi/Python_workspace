#https://brilliant.org/weekly-problems/2017-09-25/intermediate/

#from brilliant import goldgrid
coins = goldgrid.grid()
height, width = goldgrid.height(coins), goldgrid.width(coins)
#Initializing the dictionary for the maximum coins up to a certain cell
max_coins = {(0,0): coins[0,0]}
def get_max_coins(coord):
    if coord[0] >= 0 and coord[1] >= 0:
        return max_coins[coord]
    else:
        return 0

for row in range(height):
    for column in range(width):
        if not (column, row) == (0,0):
            left_coin = get_max_coins((column - 1, row))
            down_coin = get_max_coins((column, row - 1))
            max_coins[(column,row)] = max(left_coin, down_coin) + coins[column,row]  #递归


def trace_path(coord, accumulator):
    accumulator.append(coord)

    left_coord = (coord[0] - 1, coord[1])
    down_coord = (coord[0], coord[1] - 1)

    max_coord = (left_coord, down_coord)[get_max_coins(down_coord) > get_max_coins(left_coord)]

    if coord != (0,0):
        return trace_path(max_coord, accumulator)
    else:
        return accumulator

#Print path and maximum value
print(trace_path((width - 1, height - 1), []))
print(get_max_coins((width - 1, height - 1)))