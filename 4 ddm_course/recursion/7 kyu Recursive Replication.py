'''


@countcalls
def replicate(times, number):
    #your code here

Test.describe("Basic tests")
Test.assert_equals(replicate(3,5), [5, 5, 5])
Test.assert_equals(replicate(5,1), [1, 1, 1, 1, 1])
Test.assert_equals(replicate(0,12), [])
Test.assert_equals(replicate(-1,12), [])
Test.assert_equals(replicate(8,0), [0, 0, 0, 0, 0, 0, 0, 0])
'''
times, number = 3,5

#start = [0*times]
#start = [0]*times
#start = []
#number = start.append(number)
#number = [number].append(number)
#number = list(number).append(number)
print(number)

#print(start,number)

#@countcalls
def replicate(times, number):
    if times > 0:
        return [number] + replicate(times - 1, number)
    return []
print(replicate(times, number))

'''
def replicate(times, number):
    start = []
    #number = [number]
    start.extend([number])
    if times <= 0:
        return number, times

    else:
        # number = [number]
        # number += str(number)
        start.extend([number])
        print(times, number)
        replicate(times - 1, start)

print(replicate(times, number))
'''