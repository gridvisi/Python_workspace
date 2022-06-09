'''
@test.describe("say me operations")
def test_group():
    @test.it("basic")
    def basic():
        test.assert_equals(sayMeOperations("1 2 3 5 8"), "addition, addition, addition")
        test.assert_equals(sayMeOperations("9 4 5 20 25"), "subtraction, multiplication, addition")
        test.assert_equals(sayMeOperations("10 2 5 -3 -15 12"), "division, subtraction, multiplication, subtraction")
        test.assert_equals(sayMeOperations("2 2 4"), "addition")
'''
def sayMeOperations(stringNumbers):
    pass