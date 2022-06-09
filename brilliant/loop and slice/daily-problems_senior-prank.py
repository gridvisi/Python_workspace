
'''
https://brilliant.org/daily-problems/senior-prank/


'''

block = ["y"] * 50
#print(block)

def change_clor(n):
    step = 2
    block = ["y"]*n
    while step <= 50:
        for i in range(1,n,step):
            if block[i] == "b":
                block[i] = "y"
            elif block[i] == "y":
                block[i] = "b"
        step += 1
    return [i for i,e in enumerate(block) if e == "y"]
n = 50
print(change_clor(n))


#
# False := Yellow
# True := Blue

paintings = [False for _ in range(50)]

for n in range(49):
    for t in range(0, 51, n+2):
        paintings[t-1] = not paintings[t-1]

print(paintings[35], paintings[37], paintings[39], paintings[41])

 