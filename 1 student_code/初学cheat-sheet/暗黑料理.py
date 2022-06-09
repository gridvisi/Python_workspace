
print(20 * 'a' == "aaaaaaaaaaaaaaaaaaaa")
#print(20 * 'a' is "aaaaaaaaaaaaaaaaaaaa")

print(21 * 'a' == "aaaaaaaaaaaaaaaaaaaaa")
#print(21 * 'a' is "aaaaaaaaaaaaaaaaaaaaa")

#2
def fun():
    try:
        return "try this"
    finally:
        return "try final"
print(fun())


#3
for i in range(10):
    print(i)
    i = 11

#4

row = [''] * 3
board = [row] * 3
print(board)

board[0][0] = 'X'
print(board)