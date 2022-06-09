def generate_hashtag(s):
    s = s.lower()
    s = list(s)
    if len(s) > 140 or not s:
        return False
    if ord(s[0]) > 96 and ord(s[0]) < 123:
        s[0] = chr(ord(s[0])-32)
    for i in range(len(s)-1):
        if s[i] == ' ':
            if ord(s[i+1]) > 96 and ord(s[i+1]) < 123:
                s[i+1] = chr(ord(s[i+1])-32)
    for i in range(s.count(' ')):
        s.remove(' ')
    s.insert(0,'#')
    return ''.join(s)

print(generate_hashtag('CodeWars is nice'))