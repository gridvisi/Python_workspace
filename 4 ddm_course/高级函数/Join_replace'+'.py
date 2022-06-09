
strs = ['Life', 'is', 'short,', 'I', 'use', 'Python']
def join_strs(strs):
    result = ''
    for s in strs:
        result += ' ' + s
    return result
print(join_strs(strs))

print(join_strs(strs))