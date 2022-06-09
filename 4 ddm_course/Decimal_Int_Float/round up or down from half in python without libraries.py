'''
https://stackoverflow.com/questions/68429793/is-there-a-better-or-faster-solution-to-round-up-or-down-from-half-in-python-wit?r=SearchResults
'''

def rounding(number, levels = 3, up = True):
    n = number * (10 ** levels)
    nint = int(n)
    up = 1 if (up is True and number > 0) or (up is False and number < 0) else 0
    return (nint + round(n - nint + up) - up) / (10 ** levels)
print(rounding(3.1415))