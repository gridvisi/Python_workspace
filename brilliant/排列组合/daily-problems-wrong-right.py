'''
https://brilliant.org/daily-problems/wrong-right/

Today's Challenge
Different letters represent different digits, and leading digits cannot be 0.0.

If OO is 0,0, this puzzle has two solutions.

Which of the five letters in \green{R} \yellow{I} \pink{G} \blue{H} \purple{T}RIGHT has a different value in the two solutions?

WRONG + WRONG = RIGHT


\green{R}
R
\yellow{I}
I
\pink{G}
G
\blue{H}
H
\purple{T}
T

'''

# since WRONG + WRONG = RIGHT
# O = 0
#

s = [i for i in range(10)]
for n in range(10000,50000):
    #print(set(list(str(n))))
    if len(set(list(str(n)))) == 5 and len(set(list(str(n+n)))) == 5:
        if str(n)[2] == '0' and str(n)[1] == str(n+n)[0]:
            if str(n)[-1] == str(n+n)[2]:
                print(n)

'''
Since O=0,O=0, \pink{G}G cannot be 00 as well. Then we must have \pink{G}=1,G=1, carried over from the tens column. That means that \purple{T}=2T=2 from the sum in the ones column.

Therefore, in the tens column, there is no carry over from the ones column. So \blue{H}H must be an even number — the remaining evens are 4, 6,4,6, and 8.8. Noting that \orange{N}+\orange{N}\ge 10 \implies \orange{N}\ge 5N+N≥10⟹N≥5 since \pink{G}=1G=1 in the third column, we have the following cases:

If \blue{H} = 4,H=4, then \orange{N}=7.N=7.
If \blue{H}=6,H=6, then \orange{N}=8.N=8.
If \blue{H}=8,H=8, then \orange{N}=9.N=9.
Now, note that if \green{R}R is even, it must be true that \green{R} < 5R<5 because carrying a 11 to the leftmost column would mean that \green{R}R is odd, a contradiction. Then the only option for an even \green{R}R is 4.4. However, if \green{R}=4,R=4, then \red{W}=2,W=2, a repeat digit. So \green{R}R cannot be even.

If \green{R}R is odd, it must be true that \green{R} \geq 5R≥5 because, without carrying a 11 to the leftmost column, it would have to be even, a contradiction. This means that \red{W} \leq 4,W≤4, which makes its only options 33 or 4.4. So the options for \green{R}R are 77 and 9,9, respectively.

Suppose that \red{W}=4W=4 and \green{R}=9.R=9. Then we must have \yellow{I}=8,I=8, in which case none of the above three bullet points hold because of repeat digits:
\begin{aligned} 49071+{\red{4}}9071&=981{\red{4}}2\\ 49081+490{\red{8}}1&=9{\red{8}}162\\ 49091+4{\yellow{9}}0{\yellow{9}}1&=9{\red{8}}1{\red{8}}2. \end{aligned}
49071+49071
49081+49081
49091+49091
​
  
=98142
=98162
=98182.
​
 
So our solution must have \red{W}=3W=3 and \green{R}=7.R=7. That makes \yellow{I}=4.I=4. Then, along with \pink{G}=1G=1 already determined, four of the five digits in \green{R} \yellow{I} \pink{G} \blue{H} \purple{T}RIGHT are determined except for \blue{H}.H.

We can check that the second two of the three cases listed above both fit with the digits we have found:
\begin{aligned} &37081 \\ + \; &37081 \\ \hline &741{\blue{6}}2 \end{aligned}
+
​
  
37081
37081
74162
​
 
​
 
and
\begin{aligned} &37091 \\ + \; &37091 \\ \hline &741{\blue{8}}2. \end{aligned}
+
​
  
37091
37091
74182.
​
 
​
 
Only the \blue{H}H in \green{R} \yellow{I} \pink{G} \blue{H} \purple{T}RIGHT changes.
'''