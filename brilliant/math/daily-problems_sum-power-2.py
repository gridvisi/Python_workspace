# https://brilliant.org/daily-problems/sum-power-2/
def conversion(n, base, result):
    if n < base:
        result.append(n)
    else:
        conversion(n//base, base, result)
        result.append(n % base)
    return result

for i in [11, 26, 65, 127]:
    print(f"{i:3} : {' '.join([str(c) for c in conversion(i, 2, [])])}")

# Consecutive Sum
def consecutive(n):
    bin_n = str(bin(n))[2:]
    if len(bin_n) == bin_n.count('1'):
        return f"{n}" + " is Consecutive Sum"
    else:
        return f"{n}" + " is Not Consecutive Sum"
print(consecutive(127))