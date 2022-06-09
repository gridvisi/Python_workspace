'''
https://www.codewars.com/kata/5af823451839f1768f00009d/train/

我们给你一个文档（字符串）数组、一个术语（字符串）和两个booleans来微调你的索引操作。
返回一个包含文档ID的数组（数组中基于1的文档索引），其中出现了术语，按升序排序。

Booleans:

CaseSensitive: test匹配test，但不匹配Test。
不区分大小写：test同时匹配test和Test。

完全匹配：测试与test和.test！相匹配，但不匹配attest或test42。
不完全匹配：测试与证明同时匹配。

Booleans:

CaseSensitive: test matches test, but not Test
Not CaseSensitive: test matches both test and Test

Exact Match: test matches test and .test!, but not attest or test42
Not Exact Match: test matches both test and attest
'''

def build_inverted_index(collection, term, case_sensitive, exact_match):
    flag = f"{int(case_sensitive)}{int(exact_match)}"
    if flag == '11':
        pass
    return

#1st solution
import re
def build_inverted_index(coll, term, cS, eM):
    return [i + 1 for i, x in enumerate(coll) if re.search(r"{0}{1}{0}".format('\\b' if eM else '', term), x, flags = not cS and re.I)]

#2nd soluion
import re

def build_inverted_index(expressions, term, case, exact):
    flag = "" if case else "(?i)"
    bound = r"\b" if exact else ""
    pattern = re.compile(f"{flag}{bound}{term}{bound}")
    return [i for i, exp in enumerate(expressions, 1) if pattern.search(exp)]
collection, term, case_sensitive, exact_match = ["Sign", "sign", "Signature", "Sign-ature"], "Sign", True, True