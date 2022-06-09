import this


import difflib

text_a = "Antartica was once a rainforest.".split('.') #Google’s DeepMind built artificial intelligences that can defeat human beings at all of the standard Atari (arcade) games.The risk of death and disability after a stroke fell substantially between 2000 and 2015.The U.S. Space Force announced that the Space Fence has been completed."
text_b = "Antartica was once  rainforest.".split('.')

d = difflib.Differ()
diff = d.compare(text_a,text_b)
print(diff)
print('\n'.join(diff))



zen = "The Zen of Python, by Tim Peters," \
         "Beautiful is better than ugly." \
      "Explicit is better than implicit." \
         "Simple is better than complex." \
         "Complex is better than complicated." \
      "Flat is better than nested." \
         "Sparse is better than dense.Readability counts." \
         "Special cases aren't special enough to break the rules." \
         "Although practicality beats purity." \
         "Errors should never pass silently." \
         "Unless explicitly silenced." \
         "In the face of ambiguity, refuse the temptation to guess." \
         "There should be one-- and preferably only one --obvious way to do it." \
         "Although that way may not be obvious at first unless you're Dutch." \
         "Now is better than never." \
         "Although never is often better than *right* now." \
         "If the implementation is hard to explain, it's a bad idea." \
         "If the implementation is easy to explain, it may be a good idea." \
         "Namespaces are one honking great idea -- let's do more of those!".split('.')


text = "The Zen of Python, by Tim Peters," \
         "Beautiful is better than ugly." \
       "Explicit is better than implicit." \
         "Simple is better than complex." \
         "Complex is better than complicated." \
       "Flat is better than nested." \
         "Sparse is better than dense.Readability counts." \
         "Special cases aren't special enough to break the rules." \
         "Although practicality beats purity." \
         "Errors should never pass silently." \
         "Unless explicitly silenced." \
         "In the face of ambiguity, refuse the temptation to guess." \
         "There should be one-- and preferably only one --obvious way to do it." \
         "Although that way may not be obvious at first unless you're Dutch." \
         "Now is better than ever." \
         "Although never is often better than *right* now." \
         "If the implementation is hard to explain, it's a bad idea." \
         "If the implementation is easy to explain, it may be a good idea." \
         "Namespaces are one honking great idea -- let's do more of those!".split('.')

print(zen,text)
d = difflib.Differ()
print(len(zen),len(text))
#print(zen.split(),text.split())
#print(len(zen.split()),len(text.split()))

zen = 'i love python'.split('.')
text = 'i like python'.split('.')
diff = d.compare(zen,text)
#diff = [list(d.compare(z,t)) for z in zen.split() for t in text.split()]
print(diff)
print('\n'.join(diff))

import difflib
s = difflib.SequenceMatcher(None, "love", "like")
print(s.ratio())
#结果为0.75