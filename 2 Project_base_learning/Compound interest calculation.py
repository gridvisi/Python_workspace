
capital = 10000
interest_rate = 100*10**-2
period = 30 # interest cal per day
print(365/period)
rate = float(period/365)
print(interest_rate * rate)


def cic(capital,interest_rate,period,round = 365/period):
    rate = float(period/365)
    while round > 0:
        interest = capital * interest_rate * rate
        capital,round = capital+interest,round - 1
        print(capital,round,interest,rate)
    return capital

print(cic(capital,interest_rate,period,round = 365//period))

'''
def cic(capital,interest_rate,period,round = 365//period):

    rate = float(period/365)

    interest = capital * interest_rate * rate
    capital += interest
    print(capital,round,interest,rate)
    round -= 1
    if round == 0:
        return capital
    else:return cic(capital,interest_rate,period,round)

print(cic(capital,interest_rate,period,round = 365//period))
'''
