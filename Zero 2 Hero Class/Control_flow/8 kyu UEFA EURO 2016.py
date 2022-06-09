'''
uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."

'''


def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"

    if scores[0] == scores[1]:
        return f"At match {teams[0]} - {teams[1]}, teams played draw."

    if scores[0] < scores[1]:
        return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"

def uefa_euro_2016(teams, scores):
    s1, s2 = scores
    result = "teams played draw." if s1 == s2 else f"{teams[s1 < s2]} won!"
    return f"At match {teams[0]} - {teams[1]}, {result}"


def uefa_euro_2016(teams, scores):
    return f"At match {teams[0]} - {teams[1]}, {'teams played draw.' if scores[0] == scores[1] else teams[scores.index(max(scores))] + ' won!'}"