import re
from collections import defaultdict
solutions = defaultdict(list)
word = 'hero and zero for you'
category = re.sub("[aeiou]", "*", word)
print(re.sub("[aeiou]", "*", word))
solutions[category].append(word)
#print(solutions,solutions.itervalues() )

# solution
word = ['blackcaps', 'blackguard', 'blacks', 'blague', 'blancmange',
     'blander', 'blastular', 'blawort', 'blender', 'blimbing',
     'blinder', 'blistered', 'blocks', 'blonde', 'blonder',
     'blotchier', 'blowlamp', 'blue', 'bluejays', 'blunder']

w = 'blonde'
VOWELS = 'aeiou'
PATTERN = re.compile(r'[' + VOWELS + ']')
print(PATTERN)
transDct = defaultdict(set)
transDct[PATTERN.sub('_', w)].add(w)
print(transDct)


# abc startup
line = "this hdr-biz 123 model server 456"
line = "123 345 this hdr-biz 123 model server 456"
pattern = r"123"
pattern = r"hdr"
matchObj = re.match(pattern, line)
print(matchObj)

pattern=r"hdr-biz"
pattern=r"hdr"
m = re.search(pattern, line)
print(m)


patt=r'hdr'
pattern = re.compile(r'\d+')
name = re.sub(patt, "hdrhdr", line)
print(name)

pattern = re.compile(r'\d+')
name = re.sub(pattern, "abc", line)
print(name,pattern )

line="this hdr-biz model server args= server"
patt=r'server'
pattern = re.compile(patt)
result = pattern.findall(line)
print(result)

it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
  print (match.group())

re_str = r'(\d{3})abc'
print([re.fullmatch(re_str, x) for x in ['773abc','773abcer']])
print(re.findall(re_str, 'euhasdhf873abcssjsja235abcu-03s834432abcjjsks'))


#print(result.string)
result = re.match(r'\d([a-zA-Z]+)123', '2hjdh123ABC')
print('match:',result)