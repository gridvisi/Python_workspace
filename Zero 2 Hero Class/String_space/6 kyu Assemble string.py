# https://www.codewars.com/kata/6210fb7aabf047000f3a3ad6/train/python
'''
import codewars_test as test
from solution import assemble

@test.describe('Example')
def test_group():
    @test.it('Should pass')
    def test_case():
        test.assert_equals(assemble(['H*llo, W*rld!', 'Hel*o, *or*d!', '*ello* World*']), 'Hello, World!');
        test.assert_equals(assemble(['.** . ." ."" ! ! .', '. . . ." **" ! * .', '* . .*.* ."" * ! .', '. . .*." .**** ! .', '**. * .* .*" ! ! .']), '. . . ." ."" ! ! .');
        test.assert_equals(assemble(['. . . .', '. . . .', '. . . .', '. . . .', '. . . .']), '. . . .');
        test.assert_equals(assemble(['12***6789', '**3456789', '12345**8*', '***456**9', '1*3*5*7*9', '*2*456789']), '123456789');
        test.assert_equals(assemble(['******', '******', '******', '******']), '######');
        test.assert_equals(assemble(['*#*#*#*#*#*#*#*', '*#*#*#*#*#*#*#*', '*#*#*#*#*#*#*#*', '*#*#*#*#*#*#*#*']), '###############');
        test.assert_equals(assemble([]), '');


'''
def assemble(input):
    if not input:return ''
    c = ''
    for i in range(len(input[0])):
        s = ''.join(set([w[i] for w in input if w[i]!="*"]))
        c += s if len(s) else "#"
    return c
input = ['H*llo, W*rld!', 'Hel*o, *or*d!', '*ello* World*']
print(assemble(input))


def assemble(input):
    result = list(input[0]) if input else []

    for i in input:
        for j, k in enumerate(i):
            result[j] = k if result[j] == '*' else result[j]

    return ''.join(result).replace('*', '#')


def assemble(data: list) -> str:
    return ''.join(next(filter('*'.__ne__, c), '#') for c in zip(*data))


def assemble(inp):
    return "".join(min({*letters} - {"*"}, default="#") for letters in zip(*inp))

def assemble(input):
    return ''.join(next((y for y in x if y != '*'), '#') for x in zip(*input))


input = [
  "a*cde",
  "*bcde",
  "abc*e"
]
result = "abcde"
print(list(zip(*input)))
print(min({*('a', '*', 'a')}))
print(min({*('a', '*', 'a')} - {"*"},default="#"))
print(min({*('*', '*', '*')} - {"*"},default="#"))

input = [
  "a*c**",
  "**cd*",
  "a*cd*"
]