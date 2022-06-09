def frame(text, char):
    start = ''
    se = ''
    for i in range(0,4+len(text[0])):
        start = char+start
    se = start
    for i in range(len(text)):
        start = start+'\n'+char+' '+text[i]+' '+char
    start += '\n'+se
    return start

print(frame(['Create','this','kata'], '+'))