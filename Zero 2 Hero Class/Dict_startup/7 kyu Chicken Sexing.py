'''
https://www.codewars.com/kata/57ed40e3bd793e9c92000fcb/train/python

import codewars_test as test
from solution import correctness

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(correctness(('M', 'F', '?'), ('M', 'F', '?')), 3)
        test.assert_equals(correctness(('M', '?', 'M'), ('M', 'F', '?')), 2)
        test.assert_equals(correctness(('F', 'M', 'F'), ('M', 'F', 'M')), 0)
'''
bobs_decisions, expert_decisions = ('M', '?', 'M'), ('M', 'F', '?')

bobs_decisions, expert_decisions = expert_decisions, bobs_decisions
print(bobs_decisions,expert_decisions)

print([x==y for x,y in zip(bobs_decisions,expert_decisions)])
print([(x,y) for x,y in zip(bobs_decisions,expert_decisions)])


def correctness(bobs_decisions, expert_decisions):
    return sum([1 if x==y else 0.5 if '?' in (x+y) else 0 for x,y in zip(bobs_decisions,expert_decisions)])

bobs_decisions, expert_decisions = ('M', '?', 'M'), ('M', 'F', '?')
print(correctness(bobs_decisions, expert_decisions))