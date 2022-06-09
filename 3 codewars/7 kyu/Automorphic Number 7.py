def automorphic(n):
    if n == (n * n) % (10 ** len(str(n))): return "Automorphic"
    else: return "Not!!"


print(automorphic(25))
