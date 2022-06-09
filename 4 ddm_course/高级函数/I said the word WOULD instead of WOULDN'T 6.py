def speech_correction(words, speech):
    speech = speech.split(' ')
    for i in range(len(speech)-1):
        for j in range(len(words)-1):
            if (words[j] in speech[i]):
                speech[i] = speech[i]+"n't"
            elif (words[j].upper() in speech[i].upper()):
                speech[i] = speech[i]+"N'T"
            elif (words[j]+"'t" in speech[i]) or (words[j].upper() + "'T" in speech[i]) or (words[j]+"n't" in speech[i]) or (words[j].upper() + "N'T" in speech[i]):
                temp = list(speech[i])
                speech[-1] =speech[-2]=speech[-3] = ''
                temp = ''.join(temp)
                speech[i] = temp
                continue
        speech[i] += ' '
    return ''.join(speech)
print(speech_correction(["can","do","have","was","would"],"You DO?"))