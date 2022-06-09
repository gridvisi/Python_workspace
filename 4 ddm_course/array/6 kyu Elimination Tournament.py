'''
https://www.codewars.com/kata/5f631ed489e0e101a70c70a0/train/python

@test.describe("tourney")
def tests():
    @test.describe("sample tests")
    def sample():
        @test.it("testing even list length")
        def even():
            input1 = [9, 5, 4, 7, 6, 3, 8, 2]
            output1 = [
              [9, 5, 4, 7, 6, 3, 8, 2],
              [9, 7, 6, 8],
              [9, 8],
              [9]
            ]
            test.assert_equals(tourney(input1), output1)
        @test.it("testing odd list length")
        def odd():
            input2 = [9, 5, 4, 7, 6, 3, 8]
            output2 = [
              [9, 5, 4, 7, 6, 3, 8],
              [8, 9, 7, 6],
              [9, 7],
              [9]
            ]
            test.assert_equals(tourney(input2), output2)
'''
inp = [9, 5, 4, 7, 6, 3, 8, 2]
import numpy as np
def tourney(inp):
    tour = [inp]
    arry = inp
    while len(arry) > 1:
        print(arry)
        #if len(arry)%2 == 0:
        if len(arry)%2 == 1:
            head = arry[-1]
            arrs = [max(arry[i], arry[i+1]) for i in range(0, len(arry)-2, 2)]
            arrs.insert(0, head)
            arry = arrs
            tour.append(arry)
            print('if:', head, arry)
        elif len(arry)%2 == 0:
            arry = [max(arry[i], arry[i+1]) for i in range(0, len(arry)-1, 2)]
            tour.append(arry)
    return tour
inp = [9, 5, 4, 7, 6, 3, 8]
print('tour:',tourney(inp))

#1st solution
def tourney(lst):
    out = [lst]
    while len(lst)>1:
        lst = [ lst[-1] ] * (len(lst)%2) + [ *map(max, lst[::2], lst[1::2])]
        out.append(lst)
    return out


# Not good solution
def tourney(inp):
    tour = []
    arry = inp
    while len(arry) >= 1:
        print(arry)
        tour.append(arry)
        arry = [max(arry[i],arry[i+1]) for i in range(0,len(arry)-1,2)]
    return tour


import numpy as np
def tourney(inp,ans=[]):

    #if len(inp) == 1:return ans
    arry = np.array(inp)

    arry = [max(i) for i in arry.reshape(4, 2)]
    ans.append(arry)
    return tourney(arry,ans)
'''
def tourney(inp,outp=[]):
    #ans = []
    if len(inp) == 1:
        outp.extend(inp)
        return outp
    else:
        outp.append(inp)
        inp = [max(inp[st],inp[st+1]) for st in range(0,len(inp),2)]
        return tourney(inp)

'''