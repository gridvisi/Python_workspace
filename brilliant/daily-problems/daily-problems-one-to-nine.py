'''
https://brilliant.org/daily-problems/one-to-nine/
'''

from itertools import product

min_changes = 100
operations = (' + ', ' - ', ' * ', ' / ', '')
for op in product(operations, repeat=8):
    expr = '1' + op[0] + '2' + op[1] + '3' + op[2] + '4' + op[3] + '5' + op[4] + '6' + op[5] + '7' + op[6] + '8' + op[7] + '9'
    result = eval(expr)
    if result == 100:
        eqn = expr + ' = ' + str(result)
        changes = 0
        for i in expr:
            if i in ['+', '-', '*', '/']:
                changes += 1
        if changes < min_changes:
            min_changes = changes
            min_eqn = eqn
print(eqn)
print("changes:", changes)


#2 solution
from collections import Counter

operators = ["+", "-", ""] # "" represents concatenation-operator

# permutation of operators by use of recursion
def calc(n, op, solutions):
    if n == 8: # number of operations that need to be chosen before evaluation
        result = "{}".join(str(n) for n in range(1, 10)).format(*op)
        # build string with current operator permutation
        if eval(result) == 100:
            # powerful function to evaluate arithmetic operations in strings
            m = sum([v for k, v, in Counter(result).items() if k in operators])
            # count number of arithmetic operators
            solutions.add(tuple((m, result)))
            # save no of operators together with the associated arithmetic expression
        return
    else:
        for operator in operators:
            op[n] = operator
            calc(n+1, op, solutions)
    return solutions

# check for minimum operators in all possible arithmetic expressions
sol = calc(0, [""]*10, set())
print(f"min: {min(sol)}")
print(f"max: {max(sol)}")


#3rd solution
import copy, itertools
numbers = list("123456789")
operators = list("+-")

for i in range(1, 9):
    for j in operators:
        temp = copy.deepcopy(numbers)
        temp.insert(i, j)
        if eval(''.join(temp)) == 100:
            print (''.join(temp) + "=100")

for i in range(1, 9):
    for j in range(i+2, 10):
        for k, l in itertools.product(operators, operators):
            temp = copy.deepcopy(numbers)
            temp.insert(i, k)
            temp.insert(j, l)
            if eval(''.join(temp)) == 100:
                print(''.join(temp) + "=100")

for i in range(1, 9):
    for j in range(i+2, 10):
        for k in range(j+2, 11):
            for l, m, n in itertools.product(operators, operators, operators):
                temp = copy.deepcopy(numbers)
                temp.insert(i, l)
                temp.insert(j, m)
                temp.insert(k, n)
                if eval(''.join(temp)) == 100:
                    print(''.join(temp) + "=100")

#4th solution
p=['' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,''] # operator between numbers
# Change the minimum value of the number of operators, assign a large number at the beginning
def f(x): # x represents the x-th operator currently filled in, and the f function returns the minimum value that changes the number of operators
    if x==8: # If all operators are filled in
        t='' # expression
        k=0 # change the number of operators
        for i in range(9):
            t=t+n[i]+p[i] # Turn the array into an expression
            if p[i]!='':
                k=k+1 # Count the number of change operators
        if eval(t)==100: # If the value of the expression is 100
            print(t,'= 100') # output expression
            return k
        return 99999 # No matching answer
    else: # Not all operators are filled in
        m=99999 # minimum

        m=min(m,f(x+1)) # Fill in'||' (that is, do not change)
        p[x]='+' # Fill in'+'
        m=min(m,f(x+1)) # Fill in the next operator
        p[x]='-' # Fill in'-'
        m=min(m,f(x+1)) # Fill in the next operator
        p[x]='' # Remember to change the operator back

        return m

print('Smallest number of operators:',f(0)) # Fill in the operators from the 0th bit


#4th solution
import time

# Function that takes in an op_string and a list of nums, and returns an evaluable
# string.
def get_num_string(nums, op_string):
    final_string = "" + nums[0]
    for i in range(0, len(op_string)):
        if op_string[i] == 'C':
            final_string += nums[i + 1]
        else:
            final_string += op_string[i]
            final_string += nums[i + 1]

    return final_string


# Returns the number you get after evaluating the string
def eval_nums(nums, op_string):
    return eval(get_num_string(nums, op_string))


# Changes the concats to additions; does a parity check before
# moving to change any of the additions to subtractions. The parity
# check works because changing any addition to subtraction is the same
# as subtracting 2* a number, which maintains parity. So to get the desired
# answer, a necessary condition is that the sum of all of the numbers has the
# same parity as the answer.
def change_concats(nums, op_string, min_changes, current_index, num_changes):
    # if the num_changes is == the current known min_changes, we can't make any more changes; check it here
    if current_index == len(op_string) and num_changes <= min_changes[0]:
        if eval_nums(nums, op_string) % 2 == 100 % 2:
            # find the first index which something other than a C appears in op_string
            for i in range(0, len(op_string)):
                if op_string[i] != 'C':
                    change_addition_signs(nums, op_string, num_changes, min_changes, i)
                    return
            # Only gets to this point if the string is all C's
            change_addition_signs(nums, op_string, num_changes, min_changes, len(op_string))

    elif current_index < len(op_string):
        # recurse, keeping op_string[current_index] a C
        change_concats(nums, op_string, min_changes, current_index + 1, num_changes)

        # change it to a +
        op_string[current_index] = '+'
        num_changes += 1
        change_concats(nums, op_string, min_changes, current_index + 1, num_changes)
        op_string[current_index] = 'C'


def change_addition_signs(nums, op_string, num_changes, min_changes, current_index):
    if current_index == len(op_string):
        if eval_nums(nums, op_string) == 100:
            print(get_num_string(nums, op_string), ": Num changes ==", num_changes)
            min_changes[0] = num_changes  # it only gets to this point if num_changes <= min_changes

    elif current_index < len(op_string):
        # find the next occurrence of a + in op_string
        for i in range(current_index + 1, len(op_string)):
            if op_string[i] != 'C':
                change_addition_signs(nums, op_string, num_changes, min_changes, i)

                # change op_string[current_index] to a -, then recurse again
                op_string[current_index] = '-'
                change_addition_signs(nums, op_string, num_changes, min_changes, i)

                op_string[current_index] = '+'
                return

        # there is no next occurrence of a + in op_string; recurse to base case
        change_addition_signs(nums, op_string, num_changes, min_changes, len(op_string))

        op_string[current_index] = '-'
        change_addition_signs(nums, op_string, num_changes, min_changes, len(op_string))
        op_string[current_index] = '+'


def change_operators(nums, op_string, min_changes):
    change_concats(nums, op_string, min_changes, 0, 0)


if __name__ == "__main__":
    t0 = time.time()

    op_string = ['C'] * 8 # list instead of string because changing individual elements is more convenient
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    min_changes = [1000]  # large number, larger than the number of possible changes;
                          # similar to what you would do to find the min element of a
                          # list

    change_operators(nums, op_string, min_changes)
    print("Minimum number of changes:", min_changes[0])
    t1 = time.time()
    print("Time taken:", t1 - t0, "seconds")