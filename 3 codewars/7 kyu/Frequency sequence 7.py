def freq_seq(s, sep):
    s = list(s)
    output = []
    for i in range(len(s)):
        output.append(sep)
        output.append(str(s.count(s[i])))
    output.remove(output[0])
    output = ''.join(output)
    return output
print(freq_seq('hello world','-'))