import binascii
class Converter():
    @staticmethod
    def to_ascii(h):
        string = str(bytes.fromhex(h))
        string = list(string)
        string[0] = string[1] = string[-1] = ''
        return ''.join(string)
    @staticmethod
    def to_hex(s):
        string = str(binascii.b2a_hex(s.encode("utf8")))
        string = list(string)
        string[0] = string[1] = string[-1] = ''
        return ''.join(string)
print(Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473"))