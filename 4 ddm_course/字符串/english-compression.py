#How to convert numbers to words without using num2word library?

single_digit = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine'}

teen = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninety'}

def spell_single_digit(digit):
    if 0 <= digit < 10:
        return single_digit[digit]

def spell_two_digits(number):
    if 10 <= number < 20:
        return teen[number]

    if 20 <= number < 100:
        div = (number // 10) * 10
        mod = number % 10
        if mod != 0:
            return tens[div] + "-" + spell_single_digit(mod)
        else:
            return tens[number]

def spell_three_digits(number):
    if 100 <= number < 1000:
        div = number // 100
        mod = number % 100
        if mod != 0:
            if mod < 10:
                return spell_single_digit(div) + " hundred " +  \
                   spell_single_digit(mod)
            elif mod < 100:
                return spell_single_digit(div) + " hundred " + \
                   spell_two_digits(mod)
        else:
            return spell_single_digit(div) + " hundred"

def spell(number):
    if -1000000000 < number < 1000000000:
        if number == 0:
            return spell_single_digit(number)
        a = ""
        neg = False
        if number < 0:
            neg = True
            number *= -1
        loop = 0
        while number:
            mod = number % 1000
            if mod != 0:
                c = spell_three_digits(mod) or spell_two_digits(mod) \
                    or spell_single_digit(mod)
                if loop == 0:
                    a = c + " " + a
                elif loop == 1:
                    a = c + " thousand " + a
                elif loop == 2:
                    a = c + " million " + a
            number = number // 1000
            loop += 1
        if neg:
            return "negative " + a
        return a  #f"{a},{number} should be {a}"
number = 33
print(spell(number))

# 2nd solution
ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
illions = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
    10: 'nonillion', 11: 'decillion'}



def say_number(i):
    """
    Convert an integer in to it's word representation.

    say_number(i: integer) -> string
    """
    if i < 0:
        return _join('negative', _say_number_pos(-i))
    if i == 0:
        return 'zero'
    return _say_number_pos(i)


def _say_number_pos(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return _join(tens[i // 10], ones[i % 10])
    if i < 1000:
        return _divide(i, 100, 'hundred')
    for illions_number, illions_name in illions.items():
        if i < 1000**(illions_number + 1):
            break
    return _divide(i, 1000**illions_number, illions_name)


def _divide(dividend, divisor, magnitude):
    return _join(
        _say_number_pos(dividend // divisor),
        magnitude,
        _say_number_pos(dividend % divisor),
    )


def _join(*args):
    return ' '.join(filter(bool, args))



n = 26
s = 1
for i in range(1,n+1):
    s *= i
print(s)