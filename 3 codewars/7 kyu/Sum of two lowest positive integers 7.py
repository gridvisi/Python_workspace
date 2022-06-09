def sum_two_smallest_numbers(numbers):
    num1 = min(numbers)
    numbers.remove(num1)
    num2 = min(numbers)
    return num1+num2
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))