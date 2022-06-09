import phonenumbers
#pypi.org/project/phonenumbers/
from test import test_abstract_numbers
import phonenumbers
#from test import number
from phonenumbers import geocoder
x = phonenumbers.parse("+442083661177", None)
print(x)
#Country Code: 44 National Number: 2083661177 Leading Zero: False
type(x) #<class 'phonenumbers.phonenumber.PhoneNumber'>
y = phonenumbers.parse("020 8366 1177", "GB")
print(y)
#Country Code: 44 National Number: 2083661177 Leading Zero: False
print(x == y) #True
z = phonenumbers.parse("00 1 650 253 2222", "GB")  # as dialled from GB, not a GB number
print(z)
#Country Code: 1 National Number: 6502532222 Leading Zero(s): False

from phonenumbers import carrier
ro_number = phonenumbers.parse("+40721234567", "RO")
cname = carrier.name_for_number(ro_number, "en")
ro_number = phonenumbers.parse("+8613701183019", "hk")
cname = carrier.name_for_number(ro_number,'hk')
print(cname) #'Vodafone'