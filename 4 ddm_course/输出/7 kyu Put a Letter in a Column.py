'''
https://www.codewars.com/kata/563d54a7329a7af8f4000059/train/python


'''

#10 solve by ericlee
def build_row_text(index, character):
    return '|'.join([' ' if i-1 != index else character for i in range(11)]).strip() #' '.join(['|' for i in range(10)])
index, character = 8, 'A'
print(build_row_text(index,character))


#1st
def build_row_text(index, character):
    a=list('|||||||||')
    a[index]="|"+character+"|"
    return " ".join(a)

