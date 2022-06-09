def solution(s):
    sub = s[0:len(set(s))]
    return (s.count(sub))

print(solution('abcabcabcabc'))
print(solution('abccbaabccba'))


def solution(s):
    if (len(s) % 2 != 0):
        print('Odd')
    else:
        print('Even')
solution('abcabcN') #>> ODD
solution('abcabc')  #>> EVEN

def solution(s):
    print('INPUT:' + s)
    i = (s+s).find(s,1, -1)
    sub = s[:i]
    print('Substring:', sub)
solution('abccbaabccba') #>> INPUT:abccbaabccba >> Substring: abccba
solution('xyztxyztxyzt') #>> INPUT:xyztxyztxyzt >> Substring: xyzt

def solution(s):
    print('INPUT:' + s)
    i = (s+s).find(s,1, -1)
    sub = s[:i]
    print("i:", i)
    print('Substring_1:', sub)
    s2 = s
    s2 = s2[:-1]
    sub2 = s2[0:len(set(s2))]
    print('Substring_2:' +  sub2)
solution('wewewe')

def solution(s):
    print('-------')
    print('INPUT:' + s)
    i = (s+s).find(s, 1, -1)
    print (i)
    if (len(s) % 2 != 0):
        print('ODD')
        if(len(set(s)) == 1):
            print("CASE: ODD SINGLE CHARACTER")
            print('pattern:' +  (s[0]))
            print('Divisions:' + str(len(s)))
            return
        else:
            s = s[:-1]
            if len(set(s)) == 1:
                print('pattern:' +  (s[0]))
                print("CASE: ODD SINGLE CHARACTER EXTRA CHARACTER")
                print('Divisions:' + str(len(s)))
                return
            elif i == -1:
                sub = s[0:len(set(s))]
                print('pattern:' +  sub)
                print('Divisions:' + str(s.count(sub)))
                print("CASE: MULTI CHARACTER EXTRA CHARACTER")
                return
            else:
                sub = s[:i]
                print('pattern:' +  sub)
                print('Divisions:' + str(s.count(sub)))
                print("CASE: ODD MULTI CHARACTER")
                return
    else:
        print('EVEN')
        if len(set(s)) == 1:
            print('pattern:' +  (s[0]))
            print('Divisions:' + str(len(s)))
            print("CASE: EVEN SINGLE CHARACTER")
            return
        else:
            sub = s[:i]
            print('pattern:' +  sub)
            print('Divisions:' + str(s.count(sub)))
            print("CASE: EVEN MULTI CHARACTER")
            return

solution('a')
solution('aa')
solution('abcabc')
solution('abcabcabc')
solution('aaT')
solution('ababT')