def eliminate_set_bits(number):
    number = list(number)
    for i in range(0,number.count('0')):
        number.remove('0')
    if not number:
        return 0
    return int(''.join(number),2)
print(eliminate_set_bits("000"))