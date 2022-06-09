'''
https://www.codewars.com/kata/54207f9677730acd490000d1/train/python

When you sign up for an account somewhere, some websites do not actually store your password
in their databases. Instead, they will transform your password into something else using a
cryptographic hashing algorithm.

After the password is transformed, it is then called a password hash. Whenever you try to
login, the website will transform the password you tried using the same hashing algorithm
and simply see if the password hashes are the same.

Create the function that converts a given string into an md5 hash. The return value should
be encoded in hexadecimal.

Code Examples
Test.describe("Basic tests")
Test.assert_equals(pass_hash('password'), '5f4dcc3b5aa765d61d8327deb882cf99');
Test.assert_equals(pass_hash('abc123'), 'e99a18c428cb38d5f260853678922e03');

md5的值是不能反解的，那怎么判断现在的输入和数据库中加密的内容一致呢，只能将现在的输入加密，
拿加密后的md5值和数据库中的md5值做判断，md5可以被黑客暴力破解

https://segmentfault.com/q/1010000006988189
python 用md5生成16位长度字符串，求解
import random
import string

def id_generator(size=16, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print(id_generator())
# 结果 nrICjdPKnxZdp4tI (每次都不同)

2. md5(这个应该是你要的结果)
# Python 2.x
import hashlib
print hashlib.md5("fuck gfw").hexdigest()[8:-8]

# Python 3.x
import hashlib
print(hashlib.md5("fuck gfw".encode('utf-8')).hexdigest())[8:-8]

'''
import hashlib

def pass_hash(str):
    hash = hashlib.md5(str.encode('utf-8')).hexdigest() #[8:-8]
    return hash #hash.update(str.encode('utf-8'))
str = 'password'
str = 'abc123'
print(pass_hash(str))

from hashlib import md5
def pass_hash(str):
    return md5(str.encode()).hexdigest()

#示例一
hash = hashlib.md5()
#将加密内容先用utf-8编码，防止“Unicode-objects must be encoding before hashing”错误
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

#示例二
data = 'admin'
hash = hashlib.md5(data.encode('utf-8'))
print(hash.hexdigest())