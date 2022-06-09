'''
https://www.codewars.com/kata/52ab60b122e82a6375000bad/train/python
Test.describe("Basic tests")
Test.assert_equals(sort_reindeer(['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada']),['Kenjiro Mori', 'Juzo Okita', 'Akira Sanada', 'Susumu Tokugawa'])
Test.assert_equals(sort_reindeer([]),[])
Test.assert_equals(sort_reindeer(['Yasuo Kodai', 'Kenjiro Sado', 'Daisuke Aihara', 'Susumu Shima', 'Akira Sanada', 'Yoshikazu Okita', 'Shiro Yabu', 'Sukeharu Nanbu', 'Sakezo Yamamoto', 'Hikozaemon Ohta', 'Juzo Mori', 'Saburo Tokugawa']),['Daisuke Aihara', 'Yasuo Kodai', 'Juzo Mori', 'Sukeharu Nanbu', 'Hikozaemon Ohta', 'Yoshikazu Okita', 'Kenjiro Sado', 'Akira Sanada', 'Susumu Shima', 'Saburo Tokugawa', 'Shiro Yabu', 'Sakezo Yamamoto'])
Test.assert_equals(sort_reindeer(['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto']),['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'])
Test.assert_equals(sort_reindeer(["Sukeharu Yamamoto", "Juzo Yabu", "Saburo Shima", "Shiro Sanada", "Daisuke Mori"]),['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'])
'''
reindeer_names =['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada']

def sort_reindeer(reindeer_names):
    re = sorted([n.split(' ') for n in reindeer_names],key=lambda x:x[1])
    res = [n.split(' ') for n in reindeer_names]
    return [' '.join(n) for n in re]
print(sort_reindeer(reindeer_names))

#TOP SOLUTION
def sort_reindeer(reindeer_names):
    return sorted(reindeer_names, key=lambda s:s.split()[1])