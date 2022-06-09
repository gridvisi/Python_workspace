'''
https://www.codewars.com/kata/594b8e182fa0a0d7fc000875/train/python


'''

#ericlee solve
def find_e(s):
    try:
        if 'e' in s.lower():
            return str(s.lower().count('e'))
        elif isinstance(s ,str) and len(s ) >0:return "There is no 'E'"
        elif len(s) ==0:return ""
    except:
        return s


def find_e(s):
    return str(s.lower().count('e') or "There is no 'E'") if s else s