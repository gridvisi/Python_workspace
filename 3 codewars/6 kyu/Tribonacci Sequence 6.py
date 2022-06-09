def tribonacci(signature, n):
    num1 = signature[0]
    num2 = signature[1]
    num3 = signature[2]
    output = []
    num4 = 0
    for i in range(n-3):
        num4 = num1 + num2 + num3
        signature.append(num4)
        num1 = num2
        num2 = num3
        num3 = num4
    for i in range(n):
        output.append(signature[i])
    return output
def tribonacci2(signature,n):
    return signature[:n] if n<=len(signature) else tribonacci(signature + [sum(signature[-3:])],n)
print(tribonacci2([1,1,1],10))