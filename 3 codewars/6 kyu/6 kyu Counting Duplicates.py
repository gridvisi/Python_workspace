'''
https://www.codewars.com/kata/counting-duplicates/train/python
'''
from collections import Counter
text = "indivisibilityS"
def duplicate_count(text):
    ls,re = [e.lower() for e in text],[]
    for e in ls:
        if ls.count(e) > 1:
            if e not in re:
                re.append(e)
    return len(re)

def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

def duplicate_count(text):
    text = text.lower()
    return(sum([text.count(c) > 1 for c in set(text)]))
print(duplicate_count(text))