from itertools import takewhile

def take_while(arr, pred_fun):
    return list(takewhile(pred_fun, arr))


def take_while(arr, pred_fun):
    res = []
    for x in arr:
        if pred_fun(x): res.append(x)
        else: break
    return res

#match  python 9?
'''
def take_while(arr, pred):
    match arr:
        case [head, *tail] if pred(head):
            return [head, *take_while(tail, pred)]
        case _:
            return []

'''

take_while = lambda a, p: [*__import__("itertools").takewhile(p, a)]