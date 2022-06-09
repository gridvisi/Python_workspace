'''
https://www.codewars.com/kata/52dffa05467ee54b93000712/train/python

test.assert_equals(pseudo_sort("I, habitan of the Alleghanies, treating of him as he is in himself in his own rights"), "as habitan he him himself his in in is of of own rights the treating I Alleghanies")
    test.assert_equals(pseudo_sort("take up the task eternal, and the burden and the lesson"), "and and burden eternal lesson take task the the the up")
    test.assert_equals(pseudo_sort("Land of the Old Thirteen! Massachusetts land! land of Vermont and Connecticut!"), "and land land of of the Vermont Thirteen Old Massachusetts Land Connecticut","sentence may end with a punctuation")
    test.assert_equals(pseudo_sort("Pioneers, O Pioneers!"), "Pioneers Pioneers O","sentence may end with a punctuation")
'''

st = "Pioneers, O Pioneers!"
#st = "Land of the Old Thirteen! Massachusetts land! land of Vermont and Connecticut!"
# "and land land of of the Vermont Thirteen Old Massachusetts Land Connecticut",
# "sentence may end with a punctuation"
st = "take up the task eternal, and the burden and the lesson"


def pseudo_sort(st):
    if not st.isalpha():return st
    re = sorted(list(st.split(' ')),reverse = True)
    punc = [i[:-1] if not i[-1].isalpha() else i for i in re]
    lowc = [i for i in punc if i[0].islower()]
    upperc = [i for i in punc if i[0].isupper()]
    print(lowc, upperc)

    if len(lowc) != 0 and len(upperc) != 0:
        return ' '.join(lowc[::-1]) + ' '.join(upperc)
    else:
        if len(lowc) == 0: return ' '.join(upperc)
        if len(upperc) == 0: return ' '.join(lowc[::-1])

print(pseudo_sort(st))


from string import punctuation
t = str.maketrans("", "", punctuation)

def pseudo_sort(s):
    a = s.translate(t).split()
    b = sorted(x for x in a if x[0].islower())
    c = sorted((x for x in a if x[0].isupper()), reverse=True)
    return " ".join(b + c)

def pseudo_sort(s):
    s = ''.join(i for i in s if i.isalpha() or i is ' ')
    a = sorted(i for i in s.split() if i[0].islower())
    b = sorted((i for i in s.split() if i[0].isupper()),key=lambda x: x.lower(),reverse=True)
    return ' '.join(a+b)

'''
    if len(lowc) != 0 and len(upperc) != 0:

       
        return ' '.join(lowc[::-1]) + ' '.join([i for i in punc if i[1].islower()])
    else:
        if len(lowc) == 0:' '.join([i for i in punc if i[1].islower()])
        if len(upperc) == 0:' '.join(lowc[::-1])


def pseudo_sort(st):
    re = sorted(list(st.split(' ')),reverse = True)
    punc = [i[:-1] if not i[-1].isalpha() else i for i in re]
    lowc = [i for i in punc if i[0].islower()]
    return ' '.join(lowc[::-1]) + ' '.join([i for i in punc if i[1].islower()])
'''