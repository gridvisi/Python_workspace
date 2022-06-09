def first_non_repeating_letter(string):
    backup = string
    string = string.lower()
    backup = list(backup)
    string = list(string)
    if not string:
        return ''
    for i in range(len(string)):
        if string.count(string[i]) == 1:
            return str(backup[i])
    return ''
print(first_non_repeating_letter('abba'))