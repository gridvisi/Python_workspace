'''
https://brilliant.org/daily-problems/5-solutions-cryptogram/

    A B
+   A B
----------
=   B C

This simple-looking cryptogram has five solutions, so the challenge is to find all of them.
Given that every letter corresponds to a different digit, what is the sum of all the possible
values of WHICH IS RIGHT OPTION:
24  25  26  27  28
'''

b_sum = 0
for ab in range(10, 100):
    # extract digits by using of mod- and floor-division-operators
    if ab % 10  == 2 * ab // 10 and ab // 10 != ab % 10 != 2 * ab % 10:
        b_sum += 2 * ab // 10
        print(f"ab: {ab}, bc: {2 * ab}")
print(b_sum)

digit_b = [i for i in range(10)]
digit_a = [i for i in range(1,10)]

ans = []
for a in digit_a:
    for b in digit_b:
        if b*10 <= 2*(a*10 + b) <= b*10+9:
            ans.append([a,b])
print(ans,'sum(all of option b) is',sum([x[1] for x in ans]))
