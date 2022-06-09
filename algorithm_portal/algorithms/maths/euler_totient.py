"""
在数论中，对正整数n，欧拉函数φ(n)是小于或等于n的正整数中与n互质的数的数目。
此函数以其首名研究者欧拉命名，它又称为φ函数（由高斯所命名）或是欧拉总计函数
（totient function，由西尔维斯特所命名）。

例如φ(8) = 4，因为1,3,5,7均和8互质。

也可以从简化剩余系的角度来解释，简化剩余系(reduced residue system)
也称既约剩余系或缩系，是m的完全剩余系中与m互素的数构成的子集，如果模m
的一个剩余类里所有数都与m互素，就把它叫做与模m互素的剩余类。在与模m互
素的全体剩余类中，从每一个类中各任取一个数作为代表组成的集合，叫做模m的一个简化剩余系。

（1，3，5，7）就构成了8的一个简化剩余系。

Euler's totient function, also known as phi-function ϕ(n),
counts the number of integers between 1 and n inclusive,
which are coprime to n.
(Two numbers are coprime if their greatest common divisor (GCD) equals 1).
"""
def euler_totient(n):
    """Euler's totient function or Phi function.
    Time Complexity: O(sqrt(n))."""
    result = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result
