'''
https://www.codewars.com/kata/5e5acfe31b1c240012717a78/train/python

test.describe('Basic Tests')
test.assert_equals(make_model_year([1998, 'ford', ('mustang', 'gt'), False]), {'make': 'ford', 'model': 'mustang gt', 'year': 1998, 'new': False})
test.assert_equals(make_model_year(['benz', ('motorwagen', 'basic'), False, 1886]), {'make': 'benz', 'model': 'motorwagen basic', 'year': 1886, 'new': False})
test.assert_equals(make_model_year([('camry', 'basic'), True, 2020, 'toyo']), {'make': 'toyo', 'model': 'camry basic', 'year': 2020, 'new': True})
'''

def make_model_year(lst):
    dict_car = {'make': '', 'model': (), 'year': 0, 'new': True}
    for i in lst:
        if isinstance(i,str):
            dict_car['make'] = i

        if isinstance(i,tuple):
            dict_car['model'] = ' '.join(i)

        if isinstance(i,int) and i > 1:
            dict_car['year'] = i

        if isinstance(i,bool):
            dict_car['new'] = i

    return dict_car
lst = [1998, 'ford', ('mustang', 'gt'), False]
print(make_model_year(lst))

print(isinstance(1996,bool))
print(isinstance(False,int))


#1
id_=lambda k: lambda v: (k,v)

CONFIG = {
    bool:  id_('new'),
    int:   id_('year'),
    tuple: lambda t:('model',' '.join(t)),
    str:   id_('make'),
}

def make_model_year(lst):
    return dict( CONFIG[type(data)](data) for data in lst)

#2
D = {int:   (lambda x: ('year', x)),
     str:   (lambda x: ('make', x)),
     tuple: (lambda x: ('model', ' '.join(x))),
     bool:  (lambda x: ('new', x))}

def make_model_year(lst):
    return dict(D[type(x)](x) for x in lst)

#3rd
def make_model_year(lst):
    new, year, make, model = sorted(lst, key=lambda i: str(type(i)))
    return {'make':make, 'model':' '.join(model), 'year':year, 'new':new}

