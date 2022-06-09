from zoneinfo import ZoneInfo
from datetime import datetime, timezone
print(datetime.now(tz=timezone.cn))

from zoneinfo import ZoneInfo
ZoneInfo("America/Vancouver")

'''
请注意，所产生的时间戳是时区识别的，它有一个由tzinfo指定的附加时区。它有一个由tzinfo指定的附加时区。没有任何时区信息的时间戳被称为 naive。
Paul Ganssle是dateutil的维护者，已经有多年的经验。他在2019年加入了Python核心开发人员，并帮助添加了一个新的zoneinfo标准库，使时区工作更加方便。
zoneinfo提供了对互联网编号分配机构（IANA）时区数据库的访问。IANA每年都会对其数据库进行多次更新，它是最权威的时区信息来源。
使用zoneinfo，您可以得到一个描述数据库中任何时区的对象。
'''
