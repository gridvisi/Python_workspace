def longest_consec(strarr, k):
    cam2 = 0
    backup = strarr.copy()
    pk = "a"
    cam = 99999999
    output = []
    if k > len(strarr) or k<=0 or len(strarr) == 0:
        return ""
    for j in range(k):
        for i in range(len(strarr)):

            if len(strarr[i]) > len(pk) or len(strarr[i]) == cam2:
                pk = strarr[i]
                cam2 = len(strarr[i])
        output.append(pk)
        strarr.remove(pk)
        pk = "a"
    new = []
    for i in range(len(output)):
        if backup.index(output[i]) < cam:
            new.insert(0,output[i])
        else:
            new.append(output[i])
        cam = backup.index(output[i])
    new = ''.join(new)
    return new

print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))