'''
Test.it("Basic tests")
Test.assert_equals(missing("123567"),4)
Test.assert_equals(missing("899091939495"),92)
Test.assert_equals(missing("9899101102"),100)
Test.assert_equals(missing("599600601602"),-1)
Test.assert_equals(missing("8990919395"),-1)
Test.assert_equals(missing("998999100010011003"),1002)
Test.assert_equals(missing("99991000110002"),10000)
Test.assert_equals(missing("979899100101102"),-1)
Test.assert_equals(missing("900001900002900004900005900006"),900003)
'''
s = "899091939495"  #92
s = "900001900002900004900005900006"
print(len(s),list(s))
def missing(s):
    sl,re = 1,[]
    countone = 0
    for sl in range(1,len(s)//2):
        re = [int(s[i]) for i in range(sl,len(s),sl)]
        print(re)
        if len(set(re)) == 1:
            ix = [s.index(e) for e in s if e == str(re[0])]
    return countone,ix


def missing(seq):
    for digits in range(1, len(seq) // 2 + 1):
        my_seq = last = seq[:digits]
        n = int(my_seq)
        missing = None

        while len(my_seq) < len(seq):
            n += 1
            my_seq += str(n)

            if not seq.startswith(my_seq):
                if missing == None:
                    missing = n
                    my_seq = last
                else:
                    break
            else:
                last = my_seq

        if my_seq == seq and missing:
            return missing

    return -1
print(missing(s))


def missing(s):
    for k in range(1, 7):
        p, n, l, gaps = s, int(s[:k]), k, []
        while p:
            p = p[l:]
            if p.startswith(str(n+1)):
                l, n = len(str(n+1)), n + 1
            elif p.startswith(str(n+2)):
                gaps += [n + 1]
                l, n = len(str(n+2)), n + 2
            else:
                break
        if len(gaps) == 1 and p == '': return gaps.pop()
    return -1

def missing(s):
    i = 1
    while True:
        start, missing, j = int(s[:i]), [], i
        number = start + 1
        while j <= len(s) - len(str(number)):
            if int(s[j:j + len(str(number))]) != number : missing.append(number)
            else : j += len(str(number))
            number += 1
            if len(missing) > 1 : break
        else:
            if not missing : return -1
            return missing[0]
        i += 1
'''
def missing(s):
    i,j,gap = 0,1,1
    while i+gap <= len(s):
        if int(s[i:i+gap]) == int(s[i+1:i+1+gap]) - 1:
            i += 1
            print(s[i:i + gap])
        else:
            gap += 1
            i = 0

    return s[0:gap]
'''