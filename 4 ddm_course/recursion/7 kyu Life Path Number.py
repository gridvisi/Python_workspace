'''

https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0/train/python

A person's Life Path Number is calculated by adding each individual number in that person's date of birth, untill it is reduced to a single digit number.

For example, Albert Einstein's birthday is March 14, 1879. The calculation of his Life Path Number would look like this:

year: 1 + 8 + 7 + 9 = 25; 2 + 5 = 7
month: 0 + 3 = 3
day: 1 + 4 = 5
final result: 7 + 3 + 5 = 15; 1 + 5 = 6
Einstein's Life Path Number is therefore: 6

Write the function lifePathNumber(dateOfBirth) that accepts a date of birth (as a string)
on the following format: "yyyy-mm-dd". Where "y" is year, "m" is month and "d" is day.
The function shall return a one digit integer between 1 and 9 which represents the
Life Path Number of the given date of birth.

You do not need to check that the input to the lifePathNumber()-function is correct
format. You can assume that the input to the function will always be a valid date
(as a string) with the format: "yyyy-mm-dd".

Note: If the month or day is a single digit number, then it shall be preceeded by
a 0 (zero). For example, in Einstein's case the month of March is 3; which is a
single digit number. The function shall in this case be called with the following
parameter: lifePathNumber("1879-03-14").

FUNDAMENTALSRECURSIONALGORITHMSCOMPUTABILITY THEORYTHEORETICAL
COMPUTER SCIENCENUMBERSREGULAR EXPRESSIONSDECLARATIVE PROGRAMMINGADVANCED
LANGUAGE FEATURESSTRINGS

import codewars_test as test

from solution import life_path_number

@test.describe("Example")
def test_group():
    @test.it("Life Path Number - Bill Gates")
    def billy():
        test.assert_equals(life_path_number("1955-10-28"), 4)

    @test.it("Life Path Number - Elon Musk")
    def elly():
        test.assert_equals(life_path_number("1971-06-28"), 7)

'''
birthdate = "1879-3-14"
def life_path_number(birthdate):
    num = [sum([int((n)) for n in i]) for i in birthdate.split('-')]
    print(num)
    if all(len(str(n))==1 for n in num):
        print('2', sum(num),type(num))
        if len(str(sum(num))) == 1:
            print('final')
            return sum(num)
        return life_path_number(str(sum(num)))
    else:
        for i in num:
            x = '-'.join([str(i) for i in num])
            print('1',x)
            return life_path_number(x)

#1st solution
def life_path_number(s):
    return int(s.replace("-", "")) % 9 or 9
print(life_path_number(birthdate))

#2nd solution
def life_path_number(birthdate):
    n = "".join(i for i in birthdate if i.isdigit())
    while len(str(n)) > 1:
        n = sum(i for i in map(int, str(n)))
    return n

def life_path_number(birthdate):
    num = [sum([int((n)) for n in i]) for i in birthdate.split('-')]
    print(num)
    if all([len(str(i)) == 1 for i in num]):
        print('2', num,all([len(str(i)) == 1 for i in num]))
        return sum([int(i) for i in str(sum(num))])
    elif any([len(str(i)) == 2 for i in num]):
        for i in num:
            x = '-'.join([str(i) for i in num])
            print('1',x)
            return life_path_number(x)