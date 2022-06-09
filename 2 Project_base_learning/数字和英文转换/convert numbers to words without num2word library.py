
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

def test_say_number(data, expected_output):
    """Test cases for say_number(i)."""
    output = say_number(data)
    assert output == expected_output, \
        "\n    for:      {}\n    expected: {}\n    got:      {}".format(
            data, expected_output, output)


test_say_number(0, 'zero')
test_say_number(1, 'one')
test_say_number(-1, 'negative one')
test_say_number(10, 'ten')
test_say_number(11, 'eleven')
test_say_number(99, 'ninety nine')
test_say_number(100, 'one hundred')
test_say_number(111, 'one hundred eleven')
test_say_number(999, 'nine hundred ninety nine')
test_say_number(1119, 'one thousand one hundred nineteen')
test_say_number(999999,
                'nine hundred ninety nine thousand nine hundred ninety nine')
test_say_number(9876543210,
                'nine billion eight hundred seventy six million '
                'five hundred forty three thousand two hundred ten')
test_say_number(1000**1, 'one thousand')
test_say_number(1000**2, 'one million')
test_say_number(1000**3, 'one billion')
test_say_number(1000**4, 'one trillion')
test_say_number(1000**5, 'one quadrillion')
test_say_number(1000**6, 'one quintillion')
test_say_number(1000**7, 'one sextillion')
test_say_number(1000**8, 'one septillion')
test_say_number(1000**9, 'one octillion')
test_say_number(1000**10, 'one nonillion')
test_say_number(1000**11, 'one decillion')
test_say_number(1000**12, 'one thousand decillion')
test_say_number(
    1-1000**12,
    'negative nine hundred ninety nine decillion nine hundred ninety nine '
    'nonillion nine hundred ninety nine octillion nine hundred ninety nine '
    'septillion nine hundred ninety nine sextillion nine hundred ninety nine '
    'quintillion nine hundred ninety nine quadrillion nine hundred ninety '
    'nine trillion nine hundred ninety nine billion nine hundred ninety nine'
    ' million nine hundred ninety nine thousand nine hundred ninety nine')

print('say number:',say_number(1999))
#-----------------------------------------------#
def _join(*args):
    return ' '.join(filter(bool, args))



num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def number(Number):

    if (Number > 1) or (Number < 19):
        return (num2words1[Number])
    elif (Number > 20) or (Number < 99):
        return (num2words2[Number])
    else:
        print("Number Out Of Range")
        main()

def main():
    num = eval(input("Please enter a number between 0 and 99: "))
    number(num)
main()


import math

number = int(input("Enter number to print: "))

number_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
teen_list = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
decades_list =["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


if number <= 9:
    print(number_list[number].capitalize())
elif number >= 10 and number <= 19:
    tens = number % 10
    print(teen_list[tens].capitalize())
elif number > 19 and number <= 99:
    ones = math.floor(number/10)
    twos = ones - 2
    tens = number % 10
    if tens == 0:
        print(decades_list[twos].capitalize())
    elif tens != 0:
        print(decades_list[twos].capitalize() + " " + number_list[tens])


# recursively
num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
def spell(num):
    if num == 0:
        return ""
    if num < 20:
        return (num2words[num])
    elif num < 100:
        ray = divmod(num,10)
        return (num2words2[ray[0]-2]+" "+spell(ray[1]))
    elif num <1000:
        ray = divmod(num,100)
        if ray[1] == 0:
            mid = " hundred"
        else:
            mid =" hundred and "
        return(num2words[ray[0]]+mid+spell(ray[1]))


# s

def convert(num):
    units = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens =("", "", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    if num < 0:
        return "minus "+convert(-num)

    if num<20:
        return  units[num]

    if num<100:

        return  tens[num // 10]  +units[int(num % 10)]

    if num<1000:
        return units[num // 100]  +"hundred " +convert(int(num % 100))

    if num<1000000:
        return  convert(num // 1000) + "thousand " + convert(int(num % 1000))

    if num < 1000000000:
        return convert(num // 1000000) + "million " + convert(int(num % 1000000))

    return convert(num // 1000000000)+ "billion "+ convert(int(num % 1000000000))
print(convert(100001333))
