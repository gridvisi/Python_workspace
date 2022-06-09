'''
https://www.codewars.com/kata/5ff6060ed14f4100106d8e6f/train/python

@test.describe('Ce*s*r*d Strings')
def examples():

    @test.it("Example Tests")
    def example_fixed():
        data = [
            ('*h*s *s v*ry *tr*ng*', 'Tiiesae', 'This is very strange'),
            ('A**Z*N*', 'MAIG', 'AMAZING'),
            ('xyz', '', 'xyz'),
            ('', '', ''),
            ('***', 'abc', 'abc')
        ]

        for infected, discovered, result in data:
            test.assert_equals(uncensor(infected, discovered), result)
'''
infected, discovered = '*h*s *s v*ry *tr*ng*', 'Tiiesae'

#8th solve by ericlee
def uncensor(infected, discovered):
    it = iter(discovered)
    return ''.join([next(it) if i == "*" else i for i in infected])
print(uncensor(infected,discovered))

#1st
def uncensor(infected, discovered):
    return infected.replace('*', '{}').format(*discovered)

