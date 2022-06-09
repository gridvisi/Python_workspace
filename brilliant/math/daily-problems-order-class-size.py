'''
https://brilliant.org/daily-problems/order-class-size/

Daisy, Evie, Faye, Gwen, and Harry are comparing the numbers
of students in their classes. These statements are all true:

Daisy's and Gwen's classes together are twice as big as Evie's.
Evie's and Faye's classes together are twice as big as Harry's.
Faye's and Gwen's classes together have one student fewer than
twice the size of Daisy's class.
Each class has a different size and Gwen's class is the smallest.
Whose class is the largest?


d + g == e * 2
e + f == h * 2
f + g == d * 2 - 1
g is smallest

d - e == 2*e - g - 2*h + f             (1)
e - f == 2*h - 2*d + 1 - f + g         (2)
f - g == 2*d - 2*g - 1 == 2*(d-g) - 1  (3)

#1 only if d-g==1,then f-g==d-g but confict with none of them same
so that d-g>1, so f-g>d-g, f>d

#2 (1) + (2)
d - f == 2*e - 2*d + 1
so that 2*e - 2*d + 1 < 0, e - d < - 0.5
g < e < d < f

#3 since that e - h == h - f
so that  e<h<f


2*g + 2*f == e + d + 2*h - 1
2*(g + f) == 2*d*2 - 2
4*d == e + d + 2*h + 1
3*d == e + 2*h + 1
'''