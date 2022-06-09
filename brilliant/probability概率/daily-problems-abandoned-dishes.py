'''
https://brilliant.org/daily-problems/abandoned-dishes/

For each of the four dishes i=1, 2, 3, 4,i=1,2,3,4, we define an indicator variable X_iX
i
​
  to be equal to 11 if the i^{\text{th}}i
th
  dish isn't chosen by anyone and equal to 00 otherwise.

For a dish to be completely left out, all six customers must choose one of the other three dishes, so the probability of a dish not being chosen by anyone is \left(\frac{3}{4}\right)^6=\frac{729}{4096}.(
4
3
​
 )
6
 =
4096
729
​
 . Then the expected value of each X_iX
i
​
  is

1 \times \frac{729}{4096}+0 \times \left(1-\frac{729}{4096}\right)=\frac{729}{4096}.
1×
4096
729
​
 +0×(1−
4096
729
​
 )=
4096
729
​
 .

Because we have four possible dishes, by linearity of expectation the expected number of dishes not chosen by anyone is
4\times \frac{729}{4096}=\frac{729}{1024} \approx 0.71.
4×
4096
729
​
 =
1024
729
​
 ≈0.71.
'''

print(pow(3/4,6))

#not right:
print(pow(1/4,6) + pow(2/4,6) + pow(3/4,6) + pow(4/4,6))

#right answer:
print(4 * pow(3/4,6)) #0.7 !!

