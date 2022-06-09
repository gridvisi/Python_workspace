'''
https://brilliant.org/daily-problems/circular-nim/
There are several empty spots arranged in a circle.
Taking turns, each player places one token on an empty spot. A player is not allowed to place their token in a spot that is adjacent to one of their opponent's tokens.
The player who is unable to place a token loses the game.

有几个空位排列成一个圆圈。
轮流，每个玩家将一个代币放在一个空位上。棋手不允许将自己的牌子放置在与对手牌子相邻的位置上。
无法放置令牌的玩家将输掉比赛。
'''

def is_winning_position(current_board, player_to_play):
    # Look through all the moves the player could make
    for i in range(0, len(current_board)):
        if current_board[i-1] != (-1*player_to_play) and \
                current_board[(i+1) % len(current_board)] != (-1*player_to_play) and \
                current_board[i] == 0:  # Multiplying the player by -1 switches the player
            current_board[i] = player_to_play

            # If a single move creates a losing position for the other player,
            # then this position is a winning position for the current player
            if not is_winning_position(current_board, -1*player_to_play):
                current_board[i] = 0
                return True
            current_board[i] = 0

    # If no moves are available to be made, or no moves create a winning position, this position is a losing position
    return False


if __name__ == "__main__":
    board = [1, 0, 0, 0, 0, 0, 0, 0, 0]  # WLOG, we can have player 1 move in the first slot
    if not is_winning_position(board, -1):
        print("Yves wins")
    else:
        print("Jean wins")