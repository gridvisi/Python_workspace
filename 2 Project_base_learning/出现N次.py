'''
7 kyu
Find the nth occurrence of a word in a string

You are required to implement a function find_nth_occurrence that returns the index of the nth occurrence of a substring within a string (considering that those substring could overlap each others). If there are less than n occurrences of the substring, return -1.

Example
string = "This is an example. Return the nth occurrence of example in this example string."
find_nth_occurrence("example", string, 1) == 11
find_nth_occurrence("example", string, 2) == 49
find_nth_occurrence("example", string, 3) == 65
find_nth_occurrence("example", string, 4) == -1

@test.describe('Example Tests')
def example_tests():
    @test.it('Example Test Case')
    def example_test_case():
        string = "This is an example. Return the nth occurrence of example in this example string."
        test.assert_equals(find_nth_occurrence("example", string, 1), 11)
        test.assert_equals(find_nth_occurrence("example", string, 2), 49)
        test.assert_equals(find_nth_occurrence("example", string, 3), 65)
        test.assert_equals(find_nth_occurrence("example", string, 4), -1)
'''



def find_nth_occurrence(substring, string, occurrence):
    s = 0
    for i in range(occurrence):
        #print(string[s:], s)
        index = string[s:].find(substring)
        if index == -1:return -1
        else:
            s += index + len(substring)
            #string = string[s:]
    return s - len(substring)

substring, string, occurrence = "example","This is an example. Return the nth occurrence of example in this example string.",4
print(find_nth_occurrence(substring, string, occurrence))