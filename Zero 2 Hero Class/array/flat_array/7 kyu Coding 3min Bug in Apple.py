'''
https://www.codewars.com/kata/56fe97b3cc08ca00e4000dc9/train/python

@test.describe("Basic tests")
def basic():
    @test.it('')
    def f():
        apple=[
        ["B","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"]
        ]
        answer=[0,0]
        test.assert_equals(sc(apple), answer, "good luck!")

        apple=[
        ["A","A","A","A","A"],
        ["A","B","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"]
        ]
        answer=[1,1]
        test.assert_equals(sc(apple), answer, "good luck!")

        apple=[
        ["A","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","A","A","A","A"],
        ["A","B","A","A","A"]
        ]
        answer=[4,1]
        test.assert_equals(sc(apple), answer, "good luck!")
'''

def sc(apple):
    for i in range(len(apple)):
        for j in range(len(apple[i])):
            if apple[i][j] == 'B':
                return [i,j]


#1st
def sc(apple):
    return [[x,y.index("B")] for x,y in enumerate(apple) if "B" in y][0]


