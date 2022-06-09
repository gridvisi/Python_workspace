import time
print(time.time())
print(time.strftime('%Y%m%d %a %w %U %z %x',time.localtime(time.time())))
print(time.strftime('%Y%m%d',time.localtime(time.time())))
print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))

'''
详解：

取得时间相关的信息的话，要用到python time模块,python time模块里面有很多非常好用的功能，可去官方
文档了解下，要取的当前时间的话，要取得当前时间的时间戳，时间戳好像是1970年到现在时间相隔的时间。

你可以试下下面的方式来取得当前时间的时间戳：
import time
print time.time()
输出的结果是：
1555318821.489356

但是这样是一连串的数字不是我们想要的结果，我们可以利用time模块的格式化时间的方法来处理：
time.localtime(time.time())
用time.localtime()方法，作用是格式化时间戳为本地的时间。
输出的结果是：
time.struct_time(tm_year=2010, tm_mon=7, tm_mday=19, tm_hour=22, tm_min=33, tm_sec=39, tm_wday=0, tm_yday=200, tm_isdst=0)

现在看起来更有希望格式成我们想要的时间了。
time.strftime('%Y-%m-%d',time.localtime(time.time()))

最后用time.strftime()方法，把刚才的一大串信息格式化成我们想要的东西，现在的结果是：
2019-04-15

输出日期和时间：

time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

time.strftime里面有很多参数，可以让你能够更随意的输出自己想要的东西：
下面是time.strftime的参数：
strftime(format[, tuple]) -> string
将指定的struct_time(默认为当前时间)，根据指定的格式化字符串输出
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12） 
%M 分钟数（00=59）
%S 秒（00-59）

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身 

参考：

https://www.cnblogs.com/kerwinC/p/5760811.html

 
————————————————
版权声明：本文为CSDN博主「春风化作秋雨」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/jiahao1186/java/article/details/89315703
'''
