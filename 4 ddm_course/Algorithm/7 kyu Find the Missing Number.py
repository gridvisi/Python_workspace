'''
https://www.codewars.com/kata/57f5e7bd60d0a0cfd900032d/train/python

@test.describe("Example Tests")
def exampleTests():
    @test.it("Basic tests")
    def examples():
        #Numbers from 0 to 100, but missing 5
        nums = list(range(0,101))
        nums.remove(5)
        test.assert_equals(missing_no(nums), 5)

        nums = list(reversed(range(0,101)))
        nums.remove(10)
        test.assert_equals(missing_no(nums), 10)
'''

def missing_no(nums):
    #left,right = range(min(nums),max(nums)//2+1),range(min(nums),max(nums)//2+1)
    print(range(nums))
    for n in range(min(nums),101): #max(nums)+1:
        if n not in nums:
            return n
nums = [1,3,2,5,6]
print(range(nums))
print(missing_no(nums))

#1st solution
hundred = set(range(101))

def missing_no(nums):
    return (hundred - set(nums)).pop()

def missing_no(lst):
    return 5050 - sum(lst)

def missing_no(nums):
    return 100*101//2 - sum(nums)