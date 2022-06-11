
circle = ['ada','alex','bruce','cathy','eric','fosi','sam','gaga','helen','jerry']
gender = ['G','B','B','G','B','G','B','G','G','B']
print(dict(zip(circle,gender)))
print(gender.count('B') == gender.count('G'))
#
def swap(circle,gender):
    new = [''] * len(circle)
    print(new)
    gen = [1 if i == 'B' else 0 for i in gender]
    even,odd = 0,1
    print(gen)
    for i,person in enumerate(circle):
        print(new)
        if gen[i]:
            new[even] = person
            even += 2
        elif not gen[i]:
            new[odd] = person
            odd += 2
    return [new[i:i+2] for i in range(0,len(new),2)]
print('odd_even:',swap(circle,gender))


def swap(circle,gender):
    gen = [1 if i == 'B' else 0 for i in gender]
    flag,prev = gen[0],0,
    ans = ['']*len(circle)
    print(ans)
    for i,s in enumerate(gen):
        print(circle,flag)
        if s == flag:
            ans.append(circle[i])
            flag = not flag
            if prev:
                ans[i],ans[prev] = ans[prev],ans[i]
            #continue

        elif s == flag:
            prev = i
            flag = not flag

    return circle,ans
#print(swap(circle,gender))


