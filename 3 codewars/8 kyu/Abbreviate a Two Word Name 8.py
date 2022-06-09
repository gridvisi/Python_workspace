def abbrevName(name):
    name = name.upper()
    name = list(name)
    out = name[0]
    for i in range(len(name)-1):
        if name[i] == ' ':
            out += '.'+name[i+1]
    return ''.join(out)
print(abbrevName("P hahahha"))
