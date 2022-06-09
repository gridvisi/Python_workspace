
# 整数各位数求和直至位个位数
# class
def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        res = 0
        for i in s:
            res += int(i)
        while res > 9:
            s = str(res)
            res = 0
            for i in s:
                res += int(i)
        return res

print(addDigits(0,234345))