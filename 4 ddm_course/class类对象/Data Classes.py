'''
文档：Cool New Features in Python 3.7 .not...
链接：http://note.youdao.com/noteshare?id=6b46a4ad2567f3b1097919c0a7011424&sub=895ad54ad27b4b3c86e693b790caf4a3
'''

from dataclasses import dataclass, field
@dataclass(order=True)
class Country:
    name: str
    population: int
    area: float = field(repr=False, compare=False)
    coastline: float = 0

    def beach_per_person(self):
        """Meters of coastline per person"""
        return (self.coastline * 1000) / self.population

norway = Country("Norway", 5320045, 323802, 58133)

print(norway)
#Country(name='Norway', population=5320045, coastline=58133)

print(norway.area)
#323802

usa = Country("United States", 326625791, 9833517, 19924)
nepal = Country("Nepal", 29384297, 147181)
print(nepal)
#Country(name='Nepal', population=29384297, coastline=0)

print(usa.beach_per_person())
#0.06099946957342386
print(norway.beach_per_person())
#10.927163210085629

print(sorted((norway, usa, nepal)))
'''
norway, usa, nepal 
[Country(name='Nepal', population=29384297, coastline=0),
 Country(name='Norway', population=5320045, coastline=58133),
 Country(name='United States', population=326625791, coastline=19924)]
'''
