'''
https://www.codewars.com/kata/572cc218aedd20cc83000679/train/python
'''

def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        """
            Your code here 
        """
    return result

#1st
def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if v == {}:
                result["/".join((path + (k,)))] = "";
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result


#3rd 易懂的写法
def flatten(d):
    result = {}
    for key, value in d.items():
        if value and isinstance(value, dict):
            for k, v in flatten(value).items():
                result[key + '/' + k] = v
        else:
            result[key] = value or ''
    return result