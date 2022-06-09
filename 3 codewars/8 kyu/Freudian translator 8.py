def to_freud(sentence):
    sentence = list(sentence)
    output = []
    count = 0
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            count+= 1
    for i in range(count+1):
        output.append("sex")
    output = ' '.join(output)
    return output

print(to_freud("You're becoming a true freudian expert"))