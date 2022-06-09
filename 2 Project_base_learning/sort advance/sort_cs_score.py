

alex = {'Lua': 51, 'Swift': 83, 'CoffeeScript': 47, 'java': 60, 'PowerShell': 55, 'Linux': 47, 'C++': 71, 'Julia': 62,'Python':98}
brown = {'Lua': 89, 'Swift': 53, 'CoffeeScript': 64, 'java': 80, 'PowerShell': 75, 'Linux': 88, 'C++': 51, 'Julia': 72,'Python':87}
carl = {'Lua': 90, 'Swift': 78, 'CoffeeScript': 82, 'java': 59, 'PowerShell': 90, 'Linux': 68, 'C++': 61, 'Julia': 97,'Python':97}

print(sorted(alex))
class Report:
     def __init__(self, name, course, score):
         self.name = name
         self.course = course
         self.score = score
     def __repr__(self):
         return repr((self.name, self.course, self.score))

cs = ('C++','Python','java')
def filter_cs(dict,cs):
    re = sorted([ for k,v in dict.items() if k in cs])
    return re
print('re',filter_cs(alex,cs))

SCORES = {'Alex':filter_cs(alex,cs),
          'Brown':filter_cs(brown,cs),
          'Carl':filter_cs(carl,cs)
          }
print(SCORES)

names = [alex,brown,carl]
#report_objects =
report_objects = [Report(k,v) for k,v in SCORES.items()]
print(sorted(report_objects, key=lambda report:'C++'))   # sort by cs
