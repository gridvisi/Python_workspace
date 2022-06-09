'''
https://www.codewars.com/kata/5f47e79e18330d001a195b55/train/python
'''
seq = ['1', '2', '3', '4', '5', '6', '10', '11', '12', '13']
#seq = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
seq = ['1', '2', '3', '4', '6', '10', '11', '12']

def base_finder(seq):
    res,i = [],0
    #for i,e in enumerate(seq):
    while i < len(seq)-1:
        if int(seq[i+1]) - int(seq[i]) == 1:
            #res.append(i+1)
            i += 1
        else:
            return i+1
    return len(seq)
print(base_finder(seq))

'''
def base_finder(seq):
    res,i = [],0
    #for i,e in enumerate(seq):
    while i < len(seq)-1:
        if int(seq[i+1]) - int(seq[i]) == 1:
            #res.append(i+1)
            i += 1
        else:
            return int(seq[i])+1
    return int(seq[-1])
print(base_finder(seq))
'''