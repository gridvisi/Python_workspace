'''
同学 "丁猫编贺38神快，我你锅"
主持人   "丁程祝女节乐请吃火"
'''
str, part1, part2 =  "丁丁编程祝猫38女神节快乐，我贺请你吃火锅","丁猫编贺38神快，我你锅","丁程祝女节乐请吃火"


def is_merge(str, part1, part2):
    if not part1:
      return str == part2
    if not part2:
      return str == part1
    if not str:
      return part1 + part2 == ''
    if str[0] == part1[0] and is_merge(str[1:], part1[1:], part2):
      return True
    if str[0] == part2[0] and is_merge(str[1:], part1, part2[1:]):
      return True  # 完美一对
    return False
print(is_merge(str, part1, part2))