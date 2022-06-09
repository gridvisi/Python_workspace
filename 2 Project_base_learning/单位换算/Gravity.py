
def grav_force(a, b):
    units = {
        'kg': 1,
        'g': 1/10**3,
        'mg': 1/10**6,
        'μg': 1/10**9,
        'lb': 0.453592,
        'm': 1,
        'kkm': 1000,
        'cm': 1/10**2,
        'mm': 1/10**3,
        'μm': 1/10**6,
        'ft': 0.3048
        }

    g = 6.67 * 10 ** -11
    m1, m2, r = (value * units[unit] for value, unit in zip(a, b))
    return g * m1 * m2 / r ** 2