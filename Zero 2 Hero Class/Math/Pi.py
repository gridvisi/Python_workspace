'''
John Wallis 在 1656 年发表了他的 π 乘积：偶数平方除以两个相邻奇数的无限乘积。
令人惊讶的是，科学家们在氢原子能态的量子力学公式中发现了它
'''

def JohnWallis(n):
    s = 1
    for i in range(1,n):
        s *= ((2*i)**2)/((2*i-1)*(2*i+1))
    return s*2
n = 1000000
print(JohnWallis(n))