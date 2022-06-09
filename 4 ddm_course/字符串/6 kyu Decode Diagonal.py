'''
https://www.codewars.com/kata/55af0d33f9b829d0a800008d/train/python

 H Z R R Q
  D I F C A E A !
  G H T E L A E
  L M N H P R F
  X Z R P E
'''

grid = "B p E D y o q F q n C H v x K K D\n" + \
       "C r I y o w A n y F t B B q J C u B t z I A F I\n" + \
       "F H u s s y H I D n B\n" + \
       "L o J u F D F J A I s G s u o x E v\n" + \
       "L r x G J K y x o I E n w G H J M M z w F M r G\n" + \
       "K"
    #"BruuJ", "nothing on the bottom line, so parsing should end")

grid = "H X Z 8 Q E\n" + \
       "Q N F C A E A !\n" + \
       "G H T E L A E\n" + \
       "L M N P P\n" + \
       "X Z R P *"

grid = "H\n" + \
       "D I F C A E A !\n" + \
       "G H T E L A E\n" + \
       "L M N H P R F\n" + \
       "X Z R P E"

grid = "q z J H M z D v H B H A E D G x s C C t H K w y s G K I q L t K D E J w L\n" + \
       "K p v r v z C y K M o p D y o y r n\n" + \
       "M E w B C p F n M s M J E s u A r J G F L v t r F B H E E D y E x A z F L q s r"
    # "qpwrMzFyHMMpEyuysnG"


#Top 1st
def get_diagonale_code(grid):
    grid = [line.split() for line in grid.split("\n")]
    i, j, d, word = 0, 0, 1, ""
    while 0 <= i < len(grid) and j < len(grid[i]):
        if 0 <= j < len(grid[i]):
            word += grid[i][j]
            i, j = i + d, j + 1
        else: i += d
        if i == 0 or i == len(grid) - 1: d = -d
    return word

def get_diagonale_code(grid: str) -> str:
    i, j, res, move, M = 0, 0, [], 1, [line.split() for line in grid.split('\n')]
    while i < len(M) and j < len(M[i]):
        res.append(M[i][j])
        move = 1 if i==0 else -1 if i==len(M)-1 else move
        i, j = i+move, j+1
    return ''.join(res)


def get_diagonale_code(grid: str) -> str:
    if not grid:
        return ""
    lines = [l.split() for l in grid.split('\n')]
    row, col, word = (0, 0, "")
    while col < len(lines[row]):
        word += lines[row][col]
        if row == 0:
            down = True
        if row+1 == len(lines):
            down = False
        row = row+1 if down else row-1
        col += 1
    return word


def get_diagonale_code(grid: str) -> str:
    if not grid:
        return ''
    s=[]
    for line in grid.split('\n'):
        s.append(line.split(' '))
    if len(s)==1:
        return s[0][0]
    x,y=0,0
    m=-1
    r=''
    while(y<len(s[x])):
        r+=s[x][y]
        if x==0 or x==len(s)-1:
            m*=-1
        x+=m
        y+=1
    return r


def get_diagonale_code(grid: str) -> str:
    if not grid:
        return ""
    lines = [l.split() for l in grid.split('\n')]
    row, col, word = (0, 0, "")
    while col < len(lines[row]):
        word += lines[row][col]
        if row == 0:
            down = True
        if row+1 == len(lines):
            down = False
        row = row+1 if down else row-1
        col += 1
    return word


def get_diagonale_code(grid): #-> str:
    if len(grid) == 0:return ""
    elif len(grid) == 1:return f"{grid}"
    elif len(grid) > 1:
        s = grid.split("\n")

        left = ''.join([e[i*2] for i,e in enumerate(s) if i*2 < len(e)])
        print(left)
        if len(left) < len(s):
            return left  #"nothing on the bottom line, so parsing should end"
        else:
            st = s[-1].index(left[-1])
            i,j = 0,0

            while st < len(s[i]):
                s = s[::-1]
                left += s[1]
            return left


print(get_diagonale_code(grid))


'''

           re,i,j = [],0,0
            for i,w in enumerate(s):
                re.append(''.join([w[j+i] for j in range(i,len(w),2**(len(s)-i)) if j+i < len(w)]))
            
            
            
       st = s[-1].index(left[-1])
        if st + 2 <= len(s[-2]):
            for i, e in enumerate(s[::-1][1:]):
                print(i,st + i * 2,e,len(e))
                if st + i * 2 < len(e):
                    left += e[st+(i+1)*2]

            return left
        else:
            return left
            
    #right = ''.join([s[st+i*2] if st+i*2 < len(e)-3 else '' for i,e in enumerate(s[::-1][1:])])
    #print(st,s[::-1][1:],left)
    #+ right
'''