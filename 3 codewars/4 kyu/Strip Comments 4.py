def solution(string,markers):
    string = list(string)
    output = []
    remove_mode = False
    for i in range(len(string)):
        if string[i] in markers and string[i] != chr(92):
            remove_mode = True
            continue
        elif string[i] == ' ' and string[i+1] in markers and i+1 != len(string):
            continue
        elif string[i] == '\n':
            remove_mode = False
            output.append('\n')
        elif not remove_mode:
            output.append(string[i])
    output = ''.join(output)
    return output
print(solution('oranges pears , cherries watermelons pears\nwatermelons pears ^\navocados bananas watermelons strawberries lemons cherries\navocados avocados oranges', ["'", '?', '-', '^', '#', '!', '@', '.', '=']))
#def solution(string,markers):
#    parts = string.split('\n')
#    for s in markers:
#        parts = [v.split(s)[0].rstrip() for v in parts]
#    return '\n'.join(parts)