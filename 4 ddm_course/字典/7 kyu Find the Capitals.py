'''
https://www.codewars.com/kata/53573877d5493b4d6e00050c/train/python

@test.describe('Example Tests')
def example_tests():
    state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
    test.assert_equals(capital(state_capitals), ["The capital of Maine is Augusta"]);

    country_capitals = [{'country' : 'Spain', 'capital' : 'Madrid'}]
    test.assert_equals(capital(country_capitals), ["The capital of Spain is Madrid"])

    mixed_capitals = [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}]
    test.assert_equals(capital(mixed_capitals), ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]
'''

capitals = [{'country' : 'Spain', 'capital' : 'Madrid'}]
capitals = [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}]
#--> ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]

def capital(capitals):
    re = []
    for s in capitals:
        key = [k for k,v in s.items()]
        re.append('The capital of '+ s[key[0]]) + ' is '+  s['capital']
    return re

# first fail try!
def capital(capitals):
    re = []
    for s in capitals:
        key = [k for k,v in s.items()]
        re.append('The capital of '+ s['capital'] + ' is '+ s[key[0]])
    return re

print(capital(capitals))


def capital(capitals):
    return [f"The capital of {c.get('state') or c['country']} is {c['capital']}" for c in capitals]

def capital(capitals):
    ans = []
    for each in capitals:
        a = each.get('state', '')
        b = each.get('country', '')
        c = each.get('capital')
        ans.append('The capital of {}{} is {}'.format(a,b,c))
    return ans