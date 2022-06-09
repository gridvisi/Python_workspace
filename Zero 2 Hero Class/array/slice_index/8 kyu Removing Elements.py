'''
https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/solutions/python
'''
def remove_every_other(my_list):
    # Your code here!
    return [my_list[i] for i in range(0,len(my_list),2)]

#1st
def remove_every_other(my_list):
    return my_list[::2]