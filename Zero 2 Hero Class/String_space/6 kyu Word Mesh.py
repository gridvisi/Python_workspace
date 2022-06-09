'''
https://www.codewars.com/kata/5c1ae703ba76f438530000a2/train/python

from solution import word_mesh
import codewars_test as test


@test.it("Basic tests")
def iloveyou():
    test.assert_equals(word_mesh(["beacon", "condominium", "umbilical", "california"]), "conumcal")
    test.assert_equals(word_mesh(["allow", "lowering", "ringmaster", "terror"]), "lowringter")
    test.assert_equals(word_mesh(["abandon", "donation", "onion", "ongoing"]), "dononon")
    test.assert_equals(word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]), "ownhippuscartpher")
'''
def common(x,y):
    share = ''.join(sorted(list(set(x) & set(y)),key=x.index))
    return share
x,y = "beacon", "condominium"
x,y = "condominium", "umbilical"
print(common(x,y))

def longest_common_substring(x: str, y: str):
    index_x = len(x) + 1  # columns
    index_y = len(y) + 1  # rows
    c = [[''] * index_y for _ in range(index_x)]
    current_lcs = ''

    for i in range(index_x):
        for j in range(index_y):
            if i == 0 or j == 0 or x[i-1] != y[j-1]:
                c[i][j] = ''
                continue
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + x[i-1]
                if len(c[i][j]) > len(current_lcs):
                    current_lcs = c[i][j]

    return current_lcs  #len(current_lcs),
x,y = "beacon", "condominium"
x,y = "condominium", "umbilical"
print(longest_common_substring(x, y))

def word_mesh(words):
    ans = ''
    for i in range(len(words)-1):
        ans += longest_common_substring(words[i],words[i+1])
    return ans

words = ["beacon", "condominium", "umbilical", "california"]
words = ["abandon", "donation", "onion", "ongoing"]
print(word_mesh(words))