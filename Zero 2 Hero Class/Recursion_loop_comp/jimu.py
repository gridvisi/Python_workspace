__author__ = 'Administrator'
def consume(layer):

    if layer == 1:
        return 1
    return consume(layer - 1) + 0.5*(layer**2+layer)

x=1
total=int(input('please enter the cube numeber:'))
while consume(x) < total:
    x=x+1
    if consume(x)== total:  print(x,(total-int(consume(x))))
    if consume(x)>total: print(x-1,(total-consume(x-1)))