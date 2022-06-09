


x= "😂😍🎉👍"
x="😂😍🎉👍"
print(len(x))
e = []
for emoj in x:
    e.append(ord(emoj))
print(e)


print(len(x))
e = []
for emoj in x:
    e.append((emoj,ord(emoj)))
print(e)

code = [chr(i) for i in range(12700,12899)]
print(code)

print(ord('♥'))

print(ord('I'),ord('!'),ord('👍'))
s = ' china  '
u = chr(73) + s + chr(33)
print(u)
print(s.isascii())
print(s.isnumeric())
print(s.islower())
s = '1F609'
print(chr(65))