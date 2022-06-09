'''
https://www.codewars.com/kata/58356a94f8358058f30004b5/train/python

@test.describe("Example tests")
def test_group():
    @test.it("example tests")
    def test_case():
        test.assert_equals(fly_by('xxxxxx', '====T'), 'ooooox')
        test.assert_equals(fly_by('xxxxxxxxx', '==T'), 'oooxxxxxx')
        test.assert_equals(fly_by('xxxxxxxxxxxxxxx', '=========T'), 'ooooooooooxxxxx')
'''

def fly_by(lamps, drone):
    return ''.join(['o' for i in lamps[:len(drone)]]) + lamps[len(drone):]
lamps, drone = 'xxxxxxxxx', '==T'

def fly_by(lamps, drone):
    return lamps.replace('x', 'o', drone.count('=') + 1)

def fly_by(lamps, drone):
    on = drone.find("T") + 1
    return lamps.replace("x", "o", on)
print(fly_by(lamps, drone))