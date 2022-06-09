'''
https://brilliant.org/daily-problems/cryptogram-lass/

If the same letter is used twice, it’s the same digit in both places, and if different letters are used, the digits are also different.

No number is written with a leading zero. For example, 5353 cannot be written as 053.053.

\Large \begin{array} { c c c c } & \color{#D61F06} L & \color{#69047E} E & \color{#3D99F6} T \\ + & \color{#3D99F6} T & \color{#20A900} H & \color{#69047E} E \\ \hline \color{#D61F06} L & \color{#333333} A & \color{#EC7300} S & \color{#EC7300} S \\ \end{array}
+
L
​

L
T
A
​

E
H
S
​

T
E
S
​

​

This puzzle has multiple solutions. Which letter represents the same digit in all solutions? Select all that apply.



Select one or more

\color{#333333} A
A
\color{#69047E} E
E
\color{#20A900} H
H
\color{#D61F06} L
L
\color{#EC7300} S
S
\color{#3D99F6} T
T
No digit is the same in every solution.
'''

let = [i for i in range(1000)]
res = []
for let in range(100,1000):
    for x in range(10):
        if str(let)[1] != str(let)[2]:
            the = str(let)[-1] + str(x) + str(let)[1]
            re = str(let + int(the))
            if len(re) == 4 and re[0] == str(let)[0] and re[-1] == re[-2]:
                if re[0] != re[1] and str(let)[-1] != the[-1] and str(let)[-1] != re[-1]:
                    res.append(re)
print(res)
t = [i[0] for i in res]
h = [i[1] for i in res]
y = [i[2] for i in res]
n = [i[3] for i in res]

lass = []
for i,e in enumerate([t,h,y,n]):
    if len(set(e)) == 1:
        lass.append((i,e))
print(lass,t,h,y,n)

"""
solution of:
    https://brilliant.org/daily-problems/cryptogram-lass/
"""
import itertools
def get_value(in_digit_list):
    """
    returns the number represented by the in_digit_list
    in_digit_list[0] represents the most significant digit
    """
    assert len(in_digit_list) <= 1 or in_digit_list[0] != 0
    res_val = 0
    cur_multip = 1
    for cur_digit in reversed(in_digit_list):
        res_val += cur_multip*cur_digit
        cur_multip *= 10
    return res_val

def check(in_data):
    """
    checks if in_data represents a solution of:
        https://brilliant.org/daily-problems/cryptogram-lass/
    """
    def get_value_of_str(in_str):
        return get_value([in_data[_] for _ in in_str])
    if 0 in [in_data['L'], in_data['T']]:
        res = False
    else:
        val_1 = get_value_of_str("LET")
        val_2 = get_value_of_str("THE")
        val_3 = get_value_of_str("LASS")
        res = val_1+val_2 == val_3
    return res

FREE_LETTER_LIST = sorted(list(set("LETTHELASS")))
SOL_LIST = []
print("Solutions:")
for cur_data in itertools.permutations(list(range(10)), r=len(FREE_LETTER_LIST)):
    cur_dict = dict(zip(FREE_LETTER_LIST, cur_data))
    if check(cur_dict):
        print(cur_dict)
        SOL_LIST.append(cur_dict)
print("Fixed letters:")
for cur_letter in FREE_LETTER_LIST:
    tmp_val_set = {tmp_dict[cur_letter] for tmp_dict in SOL_LIST}
    if len(tmp_val_set) == 1:
        print(cur_letter)