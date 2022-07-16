

'''

def race_podium(blocks):
    match divmod(blocks, 3):
        case 2, 1:
            return 2, 4, 1
        case t, 0:
            return t, t + 1, t - 1
        case t, 1:
            return t + 1, t + 2, t - 2
        case t, 2:
            return t + 1, t + 2, t - 1
'''