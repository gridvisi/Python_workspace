
import zulu

#print(zulu.now())
# <Zulu [2016-07-25T19:33:18.137493+00:00]>

dt = zulu.parse('2016-07-25T19:33:18.137493+00:00')
# <Zulu [2016-07-25T19:33:18.137493+00:00]>
#print(dt)
dt = zulu.create(2016, 7, 25, 19, 33, 18, 137493)
# <Zulu [2016-07-25T19:33:18.137493+00:00]>

dt.isoformat()
# '2016-07-25T19:33:18.137493+00:00'

dt.timestamp()
# 1469475198.137493

dt.naive
# datetime.datetime(2016, 7, 25, 19, 33, 18, 137493)

dt.datetime
# datetime.datetime(2016, 7, 25, 19, 33, 18, 137493, tzinfo=<UTC>)

dt.format('%Y-%m-%d')
# 2016-07-25

dt.format('YYYY-MM-dd')
# 2016-07-25

dt.format("E, MMM d, ''YY")
# "Mon, Jul 25, '16"

dt.format("E, MMM d, ''YY", locale='de')
# "Mo., Juli 25, '16"

dt.format("E, MMM d, ''YY", locale='fr')
# "lun., juil. 25, '16"

dt.shift(hours=-5, minutes=10)
# <Zulu [2016-07-25T14:43:18.137493+00:00]>

dt.replace(hour=14, minute=43)
# <Zulu [2016-07-25T14:43:18.137493+00:00]>

dt.start_of('day')
# <Zulu [2016-07-25T00:00:00+00:00]>

dt.end_of('day')
# <Zulu [2016-07-25T23:59:59.999999+00:00]>

dt.span('hour')
# (<Zulu [2016-07-25T19:00:00+00:00]>, <Zulu [2016-07-25T19:59:59.999999+00:00]>)

dt.time_from(dt.end_of('day'))
# '4 hours ago'

dt.time_to(dt.end_of('day'))
# 'in 4 hours'

list(zulu.range('hour', dt, dt.shift(hours=4)))
# [Zulu [2016-07-25T19:33:18.137493+00:00]>,
#  Zulu [2016-07-25T20:33:18.137493+00:00]>,
#  Zulu [2016-07-25T21:33:18.137493+00:00]>,
#  Zulu [2016-07-25T22:33:18.137493+00:00]>]

list(zulu.span_range('minute', dt, dt.shift(minutes=4)))
# [(Zulu [2016-07-25T19:33:00+00:00]>, Zulu [2016-07-25T19:33:59.999999+00:00]>),
#  (Zulu [2016-07-25T19:34:00+00:00]>, Zulu [2016-07-25T19:34:59.999999+00:00]>),
#  (Zulu [2016-07-25T19:35:00+00:00]>, Zulu [2016-07-25T19:35:59.999999+00:00]>),
#  (Zulu [2016-07-25T19:36:00+00:00]>, Zulu [2016-07-25T19:36:59.999999+00:00]>)]

zulu.parse_delta('1w 3d 2h 32m')
# <Delta [10 days, 2:32:00]>

zulu.parse_delta('2:04:13:02.266')
# <Delta [2 days, 4:13:02.266000]>

zulu.parse_delta('2 days, 5 hours, 34 minutes, 56 seconds')
# <Delta [2 days, 5:34:56]>