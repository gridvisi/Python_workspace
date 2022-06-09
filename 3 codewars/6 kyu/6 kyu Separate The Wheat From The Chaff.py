'''
https://www.codewars.com/kata/separate-the-wheat-from-the-chaff/train/python
Test.assert_equals(wheat_from_chaff([2,-4,6,-6]), [-6,-4,6,2])
Test.assert_equals(wheat_from_chaff([7,-3,-10]), [-10,-3,7])
Test.assert_equals(wheat_from_chaff([7,-8,1,-2]), [-2,-8,1,7])
Test.assert_equals(wheat_from_chaff([8,10,-6,-7,9]), [-7,-6,10,8,9])
Test.assert_equals(wheat_from_chaff([-3,4,-10,2,-6]), [-3,-6,-10,2,4])
Test.assert_equals(wheat_from_chaff([2,-6,-4,1,-8,-2]), [-2,-6,-4,-8,1,2])
Test.assert_equals(wheat_from_chaff([16,25,-48,-47,-37,41,-2]), [-2,-37,-48,-47,25,41,16])
Test.assert_equals(wheat_from_chaff([-30,-11,36,38,34,-5,-50]), [-30,-11,-50,-5,34,38,36])
Test.assert_equals(wheat_from_chaff([-31,-5,11,-42,-22,-46,-4,-28]), [-31,-5,-28,-42,-22,-46,-4,11])
Test.assert_equals(wheat_from_chaff([46,39,-45,-2,-5,-6,-17,-32,17]), [-32,-17,-45,-2,-5,-6,39,46,17])
Test.assert_equals(wheat_from_chaff([-9,-8,-6,-46,1,-19,44]), [-9,-8,-6,-46,-19,1,44])
Test.assert_equals(wheat_from_chaff([-37,-10,-42,19,-31,-40,-45,33]), [-37,-10,-42,-45,-31,-40,19,33])
Test.assert_equals(wheat_from_chaff([-25,-48,-29,-25,1,49,-32,-19,-46,1]), [-25,-48,-29,-25,-46,-19,-32,49,1,1])
Test.assert_equals(wheat_from_chaff([-7,-35,-46,-22,46,43,-44,-14,34,-5,-26]), [-7,-35,-46,-22,-26,-5,-44,-14,34,43,46])
Test.assert_equals(wheat_from_chaff([-46,-50,-28,-45,-27,-40,10,35,34,47,-46,-24]), [-46,-50,-28,-45,-27,-40,-24,-46,34,47,35,10])
Test.assert_equals(wheat_from_chaff([-33,-14,16,31,4,41,-10,-3,-21,-12,-45,41,-19]), [-33,-14,-19,-45,-12,-21,-10,-3,41,4,31,41,16])
Test.assert_equals(wheat_from_chaff([-17,7,-12,10,4,-8,-19,-24,40,31,-29,21,-45,1]), [-17,-45,-12,-29,-24,-8,-19,4,40,31,10,21,7,1])
Test.assert_equals(wheat_from_chaff([-16,44,-7,-31,9,-43,-44,-18,50,39,-46,-24,3,-34,-27]), [-16,-27,-7,-31,-34,-43,-44,-18,-24,-46,39,50,3,9,44])
'''

values = [-37,-10,-42,19,-31,-40,-45,33]
values = [-16,44,-7,-31,9,-43,-44,-18,50,39,-46,-24,3,-34,-27]

def wheat_from_chaff(values):
    i,j = 0,len(values)-1
    while i < len(values) and j > 0:
        if values[i] < 0:
            i += 1

        elif values[i] > 0 and values[j] < 0:
            values[i], values[j] = values[j], values[i]

        elif values[i] > 0 and values[j] > 0:
            j -= 1
        #print(i,j,values[i],values[j])
        if j < i:
            return values

def wheat_from_chaff(values):
    i, j = 0, len(values) - 1
    vals = values[:]
    while i < j:
        if vals[i] < 0:
            i += 1
        elif vals[j] > 0:
            j -= 1
        else:
            vals[i], vals[j] = vals[j], vals[i]
            i, j = i + 1, j - 1
    return vals

print(wheat_from_chaff(values))
'''
[-16,-27,-7,-31,-34,-43,-44,-18,-24,-46,39,50,3,9,44]

def wheat_from_chaff(values):
    i = 0
    while i < len(values)%2:
        if values[i] > 0:
            values[i], values[len(values)-i] = values[len(values)-i], values[i]
        i += 1
    return values

def wheat_from_chaff(values):
    i,j = 0,len(values)
    while i < len(values) and j > 0 :
        print(i,j)
        if values[i] > 0 and values[j] < 0:
            values[i],values[j] = values[j],values[i]

        i += 1
        j -= 1
    return values
'''






