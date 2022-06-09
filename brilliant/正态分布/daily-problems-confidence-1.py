'''
https://brilliant.org/daily-problems/confidence-1/


'''

import math
def normal_distribute(range,confidence=1.96):
    '''
    # se = math.sqrt(p * (1-p)/n)
    # p - confidence * se = range[0]
    # p + confidence * se = range[1]

    :param p:
    :param rate:
    :param range:
    :param confidence:
    :return:
    '''
    #p - confidence * se + p + confidence * se = range[0] + range[1]
    p = (range[0] + range[1])/2
    se = (p - range[0])/confidence
    return p*(1-p) / se**2

range = (0.31,0.37)

print(normal_distribute(range,confidence=1.96))