def solution(string, ending):
    if ending: return string[-len(ending):] == ending
    else: return True
print(solution('abcde', ''))