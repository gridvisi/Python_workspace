#https://www.codewars.com/kata/5eb34624fec7d10016de426e/train/python
'''
您在赌场里玩轮盘，只下 "1-18 "的赌注，并急于打败赌场，所以您想测试一下马丁格尔策略有多有效。
您将得到一个起始现金余额和一个二进制数字阵列，代表赢（1）或输（0）。在玩完所有回合后返回您的余额。
马丁格尔策略
您开始时的赌注为100美元。如果您输了一局，您就会输掉这一局的赌注，下一局的赌注就会翻倍。当您赢了，
您将赢得100%的赌注，并在下一次下注时回到100美元的赌注。

'''
def martingale(bank, outcomes):
    #prices = [100,100]+[100*2**i for i in range(len(outcomes))]
    bet,res = 100,0
    for i, e in enumerate(outcomes):
        if e == 0:
            res -= bet
            bet *= 2
            #outcomes[i+1] = 2*outcomes[i]
        else:
            res += bet
            bet = 100
            #outcomes[i+1] = 100
    #rate = [2*outcomes[i+1] else i for i,e in enumerate(outcomes)]

    return bank + res

# Top solution 1st
def martingale(bank, outcomes):
    stake = 100
    for i in outcomes:
        if i == 0:
            bank -= stake
            stake *= 2
        else:
            bank += stake
            stake = 100
    return bank
bank, outcomes = 1000, [1, 1, 0, 0, 1]
bank, outcomes = 0, [0, 0, 0, 0, 1, 0, 0,]  # -200
#bank, outcomes = 5100, [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0] # 5600]
print(martingale(bank, outcomes))