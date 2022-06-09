def divisible_by(numbers, divisor):
    output = []
    for i in range(len(numbers)):
        if numbers[i] % divisor == 0:
            output.append(numbers[i])
    return output
print(divisible_by([0,1,2,3,4,5,6], 2))