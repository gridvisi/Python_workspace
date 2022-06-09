
for x,y in zip([3,8],['cm',"m"]):
    print(x,y)

def grav_force(a, b, r):
    units = {

        'kg': 1,

        'g': 1/10**3,

        'mg': 1/10**6,

        'μg': 1/10**9,

        'lb': 0.453592,

        'm': 1,

        'km': 1000,

        'cm': 1/10**2,

        'mm': 1/10**3,

        'μm': 1/10**6,

        'ft': 0.3048

        }

    g = 6.67 * 10 ** -11
    v = [i[0] for i in [a,b,r]]
    u = [i[1] for i in [a,b,r]]
    print(v,u)
    M, m, r = (value * units[unit] for value, unit in zip(v, u))
    return 'N',g * M * m / r ** 2

a = (5.965 * 10**24,'kg')
b = (75,'kg')
r = (6371,'km')

print(grav_force(a, b, r))
