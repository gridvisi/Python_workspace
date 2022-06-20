
ttt = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in ttt:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(ttt)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if ttt[move] == ' ':
            ttt[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if ttt['7'] == ttt['8'] == ttt['9'] != ' ':
                printBoard(ttt)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif ttt['4'] == ttt['5'] == ttt['6'] != ' ':
                printBoard(ttt)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif ttt['1'] == ttt['2'] == ttt['3'] != ' ':
                printBoard(ttt)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif ttt['1'] == ttt['4'] == ttt['7'] != ' ':
                printBoard(ttt)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif ttt['2'] == ttt['5'] == ttt['8'] != ' ':
                printBoard(ttt)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif ttt['3'] == ttt['6'] == ttt['9'] != ' ':
                printBoard(ttt)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif ttt['7'] == ttt['5'] == ttt['3'] != ' ':
                printBoard(ttt)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif ttt['1'] == ttt['5'] == ttt['9'] != ' ':
                printBoard(ttt)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            ttt[key] = " "

        game()

if __name__ == "__main__":
    game()