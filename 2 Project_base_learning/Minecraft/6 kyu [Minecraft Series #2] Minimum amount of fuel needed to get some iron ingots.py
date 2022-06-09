'''
https://www.codewars.com/kata/583a02740b0a9fdf5900007c/train/python

Test.describe("Test cases")
Test.it("should work for the following cases")
Test.assert_equals(calc_fuel(37), {"lava": 0, "blaze rod": 3, "coal": 0, "wood": 3, "stick": 2 })
Test.assert_equals(calc_fuel(21), {"lava": 0, "blaze rod": 1, "coal": 1, "wood": 2, "stick": 1 })
Test.assert_equals(calc_fuel(123), {"lava": 1, "blaze rod": 4, "coal": 0, "wood": 4, "stick": 13 })
'''

n = 21

def calc_fuel(n):
    re = {"lava": 0, "blaze rod": 0, "coal": 0, "wood": 0, "stick": 0}
    cost = {"lava": 800, "blaze rod": 120, "coal": 80, "wood": 15, "stick": 1}
    item = n * 11
    print(item)
    for k,v in cost.items():
        if item >= v:
            re[k] = item // v
            item = item % v
    return re
print(calc_fuel(n))


# top 1st
t = ((800, "lava"), (120, "blaze rod"), (80, "coal"), (15, "wood"), (1, "stick"))

def calc_fuel(n):
    s, r = n * 11, {}
    for d, e in t:
        r[e], s = divmod(s, d)
    return r


fuel = {
    "lava": 800,
    "blaze rod": 120,
    "coal": 80,
    "wood": 15,
    "stick": 1
}
result = {
    "lava": 0,
    "blaze rod": 0,
    "coal": 0,
    "wood": 0,
    "stick": 0
}


def calc_fuel(n):
    time = n * 11

    for x in fuel.keys():
        result[x] = time // fuel[x]
        time -= result[x] * fuel[x]

    return result