'''
https://www.codewars.com/kata/5b65c47cbedf7b69ab00066e/train/python

>>> build_trie()
{}
>>> build_trie("")
{}
>>> build_trie("trie")
{'t': {'tr': {'tri': {'trie': None}}}}
>>> build_trie("tree")
{'t': {'tr': {'tre': {'tree': None}}}}
>>> build_trie("A","to", "tea", "ted", "ten", "i", "in", "inn")
{'A': None, 't': {'to': None, 'te': {'tea': None, 'ted': None, 'ten': None}}, 'i': {'in': {'inn': None}}}
>>> build_trie("true", "trust")
{'t': {'tr': {'tru': {'true': None, 'trus': {'trust': None}}}}}
'''
words = ("true", "trust")
print('true'.startswith('t'))
def build_trie(*words):
    d = {}
    for word in words:
        dd = d
        w, l = "", len(word)
        for c in word:
            w += c
            l -= 1
            if w not in dd: dd[w] = None
            if l and dd[w] is None: dd[w] = {}
            dd = dd[w]
    return d
#words = "trie"
#words = ("true", "trust")
print(build_trie("true", "trust"))

def build_trie(*words):
    root = {}
    for word in words:
        branch = root
        print('branch:',branch,root)
        length = len(word)
        for i in range(1, length+1):
            length -= 1
            key = word[:i]
            if key not in branch:
                branch[key] = None
            if length and not branch[key]:
                branch[key] = {}
                #print(branch,branch[key],root)
            branch = branch[key]
            #print(branch,  root)
    return root
words = "trie"
print(build_trie("true", "trust"))

c = {}
a = {'a':1}
b = {'b':1}
a = c
print(a,c)

'''
def build_trie(words):
    i,re = 1,{}
    tier = set([s[0] for s in words])
    while i < len(min(words,key=lambda x:len(x))):
        for s in tier:
            re[s] = [w for w in words if w.startswith(s)]
            print(re)
        i += 1
        tier = set([s[0:i] for s in words])
    return re

'''