'''
https://www.codewars.com/kata/5d2d0d34bceae80027bffddb/train/python

import codewars_test as test
from solution import sort_strings_by_vowels

@test.describe("Example")
def test_group():
    @test.it("given SIMPLE strings")
    def test_case():
        test.assert_equals(sort_strings_by_vowels(["aa","eee","oo","iiii"]), ["iiii","eee","aa","oo"])
        test.assert_equals(sort_strings_by_vowels(["a","e","ii","ooo","u"]) ,["ooo","ii","a","e","u"])
        test.assert_equals(sort_strings_by_vowels(["ioue","ee","uoiea"]), ["uoiea", "ioue","ee"])
        test.assert_equals(sort_strings_by_vowels(["high","day","boot"]), ["boot","high","day"])
        test.assert_equals(sort_strings_by_vowels(["none","uuu","Yuuuge!!"]), ["uuu","Yuuuge!!","none"])
        test.assert_equals(sort_strings_by_vowels(["AIBRH","","YOUNG","GREEEN"]), ["GREEEN","AIBRH","YOUNG",""])
        test.assert_equals(sort_strings_by_vowels(["jyn","joan","jimmy","joey"]), ["joan","joey","jimmy","jyn"])
        test.assert_equals(sort_strings_by_vowels(["uijijeoj","lkjlkjww2","iiutrqy"]), ["iiutrqy","uijijeoj","lkjlkjww2"])
        test.assert_equals(sort_strings_by_vowels(["how about now","a beautiful trio of"]), ["a beautiful trio of","how about now"])
        test.as
sert_equals(sort_strings_by_vowels(["every","bataux","is","waaaay","loose"]), ["waaaay","bataux","loose","every","is"])
'''

class Vowlen:
    def __init__(self,s):
        self.s = s

    def vowl(self):
        maxl = [e if e.lower() in 'aeiou' else ' ' for e in self.s]
        print(''.join(maxl))
        return max(''.join(maxl).split(' '),key=len)

x = Vowlen("what a beautiful day today")
print(x.vowl())

#6TH SOLVE BY ERICLEE
def vowl_len(s):
    maxl = [e if e.lower() in 'aeiou' else ' ' for e in s]
    print(''.join(maxl))
    return len(max(''.join(maxl).split(' '), key=len))

def sort_strings_by_vowels(seq):
    # your code here
    return sorted(seq,key=lambda x:vowl_len(x),reverse=True)
seq = ["how about now","a beautiful trio of"]
seq = ["aa","eee","oo","iiii"]
#print(sorted([vowl_len(s) for s in seq],key=len,reverse=True))
print(sort_strings_by_vowels(seq))


#1ST
import re
def sort_strings_by_vowels(seq):
    return sorted(seq, reverse=True, key=lambda x: max((len(i) for i in re.findall(r'[aeiouAEIOU]+', x)), default=0))

#2ND
import re
def sort_strings_by_vowels(seq):
    return sorted(seq, reverse=True, key=lambda s: max(map(len, re.findall('[aeiou]*', s, re.I))))

#3RD
def contigvowels(s):
    count = 0;
    highest = 0
    for c in s:
        if c.lower() in "aeiou":
            count += 1; highest = max(count, highest)
        else:
            count = 0
    return highest
def sort_strings_by_vowels(seq): return sorted(seq, key=contigvowels, reverse=True)

#4TH
import re


def sort_strings_by_vowels(seq):
    def vowels(st):
        groups = re.findall("([aeiou]+)", st.lower())
        return max([len(x) for x in groups]) if groups else 0

    return sorted(seq, key=lambda x: vowels(x) if x else 0, reverse=True) if seq else None

#5TH
import re


def sort_strings_by_vowels(seq):
    return sorted(
        seq,
        key=lambda s: max(len(sub) for sub in re.split("(?i)[^aeiou]+", s)),
        reverse=True,
    )

#6TH

