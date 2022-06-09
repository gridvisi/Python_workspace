
def alphabet_position(text):
    str = []
    ans = []
    text = text.lower()
    str = list(text)
    for i in range(len(str)):
        if int(str[i]) >= 61 and int(str[i]) <= 80:
            ans.append(int(str[i]))
    print(ans)
alphabet_position("The sunset sets at twelve o' clock.")