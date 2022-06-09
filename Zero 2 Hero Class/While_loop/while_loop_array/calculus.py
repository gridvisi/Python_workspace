__author__ = 'Administrator'
import numpy as np

# initialize
n=2
A= 0.0
x = 1/n
j=0
# Begin Numerical Integration
while j <= n-1:
	delta_A = x**2 * 1/n
	x = x + 1/n
	A = A + delta_A
	j = j+1
print('Approximate Area Under the Curve =', A)