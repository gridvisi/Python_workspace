# Resource case from fluent python

class Bus:
    def __init__(self,passager=None):
        if passager == None:
            self.passager = []
        else:
            self.passager = list(passager)

    def pick(self,name):
        self.passager.append(name)

    def drop(self,name):
        try:
            self.passager.remove(name)
        except: #ValueError == "x not in list":
            print(f"Please double check if {name} on bus")


import copy
T1 = Bus(['ada','bruce','cathy'])
T2 = copy.copy(T1)
T3 = copy.deepcopy(T1)
T1.pick('doris')
T1.drop('enya')
T1.drop('ada')
print(T1.passager,T2.passager,T3.passager)


# nest list deepcopy
import copy
def make_checkered_board(n):
    line=['X' for _ in range(n)]
    #lines = copy.deepcopy(line)
    board = [line[:] for _ in range(n)]  # why use line[:
    for row in range(0,n):
        for col in range(0,n):
            if (row+col)%2:
                board[row][col]="O"
    return board
n = 6
print(make_checkered_board(n))