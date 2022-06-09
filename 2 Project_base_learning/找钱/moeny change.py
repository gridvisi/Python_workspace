__author__ = 'Administrator'
coin_v = [25,10,5,1]
coin_c = [0,0,0,0]
for i in range(1000):
    tsum=i
    csum=0
    for idx,coin in enumerate(coin_v):
        if tsum//coin>0:
            coin_c[idx]=tsum//coin
            csum+=coin_c[idx]
            tsum-=(tsum//coin)*coin
    if csum==20:
        print(i)
        print ( list( zip(coin_c,coin_v) ) )
        break

def min_change(n, denoms=[1,5,10,25]):
  change = 0

  # d1, d2 <- ((1,5), (5,10), (10,25))
  for d1, d2 in zip(denoms, denoms[1:]):
    coins = min(n, (d2-change-1)//d1)
    change += d1*coins
    n -= coins

    return change + n*denoms[-1]
print(20,denoms=[1,5,10,25])