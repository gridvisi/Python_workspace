
#首先以正则表达式为例，如果我们想抽取一句话文章中的手机号码，但并不知道这句话有没有手机号，那通常我们会这么写:
import re
string = 'my mobile number is 15951914109，重庆火锅'
match_result = re.search(r'\d{11}', string)
if match_result:
    mobile_num = match_result.group()
else:
    mobile_num = None

print(mobile_num)
'15951914109'