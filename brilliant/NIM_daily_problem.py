
def squregame(top):
        sqs=[a**2 for a in range(1,int(top**0.5)+1)]
        win=sqs.copy()
        lose=[]
        for n in range(top):
            if n in win:
                continue
            if set(map(lambda x: n-x, (s for s in sqs if s < n)))&set(win) == set(map(lambda x: n-x, (s for s in sqs if s < n))):
                lose.append(n)
            else:
                win.append(n)
        print("wins: ", win)
        print("loses: ", lose)
squregame(34)