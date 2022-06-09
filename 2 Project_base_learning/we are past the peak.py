
'''
Germany: "we are past the peak"
France: "we are past the peak"
Italy: "we are past the peak"
USA: "wE aRe PaSt ThE pEaK"
'''

country = ['Germany','France','Italy','USA']
word = 'we are past the peak'

for c in country:
    if c != 'USA':
        print(f"{c}"+':'+ word)
    else:
        print('USA:'+ ''.join([e if i%2==0 else e.upper() for i,e in enumerate(word)]))