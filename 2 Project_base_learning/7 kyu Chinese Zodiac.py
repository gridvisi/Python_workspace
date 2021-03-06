'''
https://www.codewars.com/kata/57a73e697cb1f31dd70000d2/train/python

中国的十二生肖是一个12年的重复周期，每一年由一种动物和它的名誉属性代表。农历以60年为一个周期，
每一年都有一个动物和一个元素的组合。动物有12种，元素有5种，动物每年更换，元素每两年更换一次。
目前的周期是在1984年开始的，这一年是木鼠年。

由于目前的历法是格里高利历，所以我只用1924年这个纪元的年份。为了简单起见，我是以整年来计算，
而不是从1月/2月到年底。

##＃＃任务

给定一个年份，返回该年份所代表的元素和动物（"元素动物"）。例如，我出生于1998年，所以我是 "地虎"。
animals (或Ruby中的$animals)是一个预加载的数组，包含了按顺序排列的动物。
['鼠'、'牛'、'虎'、'兔'、'龙'、'蛇'、'马'、'羊'、'猴'、'鸡'、'狗'、'猪'] 。
elements (或Ruby中的$elements)是一个预加载的数组，按顺序包含元素。
['木'，'火'，'土'，'金属'，'水']
在评论中告诉我你的星座和元素。编码快乐:)
通过www.DeepL.com/Translator（免费版）翻译

['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']

elements (or $elements in Ruby) is a preloaded array containing the elements in order:

['Wood', 'Fire', 'Earth', 'Metal', 'Water']
Test.describe("Example Test Cases")

Test.assert_equals(chinese_zodiac(1965), "Wood Snake")
Test.assert_equals(chinese_zodiac(1938), "Earth Tiger")
Test.assert_equals(chinese_zodiac(1998), "Earth Tiger")
Test.assert_equals(chinese_zodiac(2016), "Fire Monkey")
Test.assert_equals(chinese_zodiac(1924), "Wood Rat")
Test.assert_equals(chinese_zodiac(1968), "Earth Monkey")
Test.assert_equals(chinese_zodiac(2162), "Water Dog")
'''

'''
干支数相加，超过5者减去5以差论之，1为木、2为金、3为水、4为火、5为土

甲 丙 戊 庚 壬   子丑  寅卯  辰巳
乙 丁 己 辛 癸   午未  申酉  戌亥
1  2  3 4  5    1     2    3

3、举例
①丙子：丙天干数为2，子地支数为1，和为3，纳音为水。
②庚申：庚天干数为4，申地支数为2，6减5余1，纳音为木。
例如 壬子年生桑柘木命（1972  ）   癸丑年生桑柘木命（1973）
壬天干数为5，子地支数为1，和为6，6减5余1，纳音为木。

项目 甲 乙 丙 丁 戊 己 庚 辛 壬 癸
性质 阳 阴 阳 阴 阳 阴 阳 阴 阳 阴
五行 木 木 火 火 土 土 金 金 水 水

项目 子 丑 寅 卯 辰 巳 午 未 申 酉 戌 亥
性质 阳 阴 阳 阴 阳 阴 阳 阴 阳 阴 阳 阴
五行 水 土 木 木 土 火 火 土 金 金 土 水

2021年100岁属猴，1922年是庚申年，庚五行属金，申为猴，所以1922年是金猴之命。
2021年100岁属鸡，1923年是辛酉年，辛五行属金，酉为鸡，所以1923年是金鸡之命。
2021年100岁属狗，1924年是壬戌年，壬五行属水，戌为狗，所以1924年是水狗之命。
'''
#1984年开始的，这一年是木鼠年 甲子金

def chinese_zodiac(year):
    # Define rules
    # 干支数相加，超过5者减去5以差论之，1为木、2为金、3为水、4为火、5为土
    Branch = {1: ['Rat', 'Ox', 'Horse', 'Goat'],
              2: ['Tiger', 'Rabbit', 'Monkey', 'Rooster'],
              3: ['Dragon', 'Snake', 'Dog', 'Pig']}

    # Define keys
    wuxing = ['Wood', 'Metal', 'Water','Fire', 'Earth']
    zodiac = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
              'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    S = ['甲','乙','丙','丁','戊','己','庚','辛','壬','庚']
    Z = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']

    # Define keys and Values
    Stem = {1:('甲','乙'),2:('丙','丁'),3:('戊','己'),4:('庚','辛'),5:('壬','庚')}
    Wuxing = dict(zip([i for i in range(1,6)],wuxing))
    # Find stem,print(S[(year - 1984)%10])
    # find animal print(zodiac[(year-1984)%12])

    stem = [(k,v) for k,v in Stem.items() if S[(year-1984)%10] in v][0]
    branch = [(k,v) for k,v in Branch.items() if zodiac[(year-1984)%12] in v]
    # stem dict and branch dict

    total = stem[0] + branch[0][0]
    # stem plus branch to get wuxing

    wx = Wuxing[total if total <= 5 else total - 5]
    #bazi = {f"{year}": [S[(year - 1984) % 10], Z[(year - 1984) % 12], wx]}

    return wx + ' ' +zodiac[(year-1984)%12]

year = 1994
print(chinese_zodiac(year))

# eric = {1972:'wood','branch':'rat','stem':'壬'}  #壬子年生桑柘木命 1972 
# ada = {1984:'Metal','branch':'rat','stem':'甲'}  #甲子年生海中金命（1984）
# 1924年是农历甲子年,是鼠年。(出生于1924年或者1984年)五行属海中金命,屋上之鼠
# 1924 should be Metal Rat, while test case show the Wooden Rat?
'''
The 2 issue during testing Case,which result does match with Chinese saying:

year = 1965 output should be Fire Snake instead of wood Snake
'Fire Snake' should equal 'Wood Snake'

year = 1924  output should be Metal Rat instead of Wooden Rat
'Metal Rat' should equal 'Wood Rat'

so that testing Case result is not suit to Chinese saying
'''



'''
天干五行

甲-木、乙-木、丙-火、丁-火、
戊-土、己-土、庚-金、辛-金、
壬-水、癸-水

地支五行

子-水、丑-土、寅-木、卯-木、
辰-土、巳-火、午-火、未-土、
申-金、酉-金、戌-土、亥-水


甲子年生海中金命（1984）  乙丑年生海水金命（1985）       
丙寅年生炉中火命（1986）  丁卯年生炉中火命（1987）  
     
戊辰年生大林木命（1988）  己已年生大林木命（1989）       
庚午年生路旁土命（1990）  辛未年生路旁土命（1991）       
壬申年生剑锋金命（1992）  癸酉年生剑锋金命（1993）    
甲戊年生山头火命（1994）  乙亥年生山头火命（1995）       
丙子年生涧下水命（1996）  丁丑年生涧下水命（1997）   
    
戊寅年生城头土命（1998）  已卯年生城头土命（1999）       
庚辰年生白蜡金命（2000）  辛已年生白蜡金命（2001）       
壬午年生杨柳木命（2002）  癸未年生杨柳木命（2003）       
甲申年生泉中水命（2004）  乙酉年生泉中水命（2005）       
丙戊年生屋上土命（2006）  丁亥年生屋上土命（2007）       
戊子年生霹雳火命（2008）  己丑年生霹雳火命（2009）       
庚寅年生松柏木命（2010）  辛卯年生松柏木命（2011）       
壬辰年生长流水命（2012）  癸已年生长流水命（2013）       
甲午年生砂石金命（2014）  乙未年生砂石金命（2015）       
丙申年生山下火命（2016）  丁酉年生山下火命（2017）       
戊戊年生平地木命（2018）  已亥年生平地木命（2019）       
庚子年生壁上土命（1960  2020）   辛丑年生壁上土命（1961  2021）       
壬寅年生金薄金命（1962  2022）   癸卯年生金薄金命（1963  2023）       
甲辰年生覆灯火命（1964  2024）   乙已年生覆灯火命（1965  2025）       
丙午年生天河水命（1966  2026）   丁未年生天河水命（1967  2027）       
戊申年生大驿土命（1968  2028）   已酉年生大驿土命（1969  2029） 

庚戊年生钗环金命（1970  ）   辛亥年生钗环金命（1971）       
壬子年生桑柘木命（1972  ）   癸丑年生桑柘木命（1973）       
甲寅年生大溪水命（1974  ）   己卯年生大溪水命（1975）       
丙辰年生沙中土命（1976  )    丁已年生沙中土命（1977）      
戊午年生天上火命（1978  ）   己未年生天上火命（1979）  
     
庚申年生石榴木命（1980  ）   辛酉年生石榴木命（1981）       
壬戊年生大海水命（1982  ）   癸亥年生大海水命（1983）  

http://www.xuexila.com/wuhang/zhishi/2095408.html


for k, v in enumerate(zodiac):
    print(k, v)
    Branch[k % 6 + 1].append(v)

相生相克编辑
木生火者，木性温暖，火伏其中，钻灼而出，故木生火；火生土者，火热故能焚木，木焚而成灰，灰即土也，故火生土；土生金者，金居石依山，津润而生，聚土成山，山必长石，故土生金；金生水者，少阴之气，润燥流津，销金亦为水，所以山石而从润，故金生水；水生木者，因水润而能生，故水生木也。
木生火， 是因为木性温暖， 火隐伏其中， 钻木而生火， 所以木生火。
火生土， 是因为火灼热， 所以能够焚烧木，木被焚烧后就变成灰烬，灰即土，所以火生土。
土生金， 因为金需要隐藏在石里， 依附着山，津润而生， 聚土成山, 有山必生石， 所以土生金。
金生水，因为少阴之气(金气)温润流泽， 金靠水生，销锻金也可变为水， 所以金生水。
水生木，因为水温润而使树木生长出来， 所以水生木。
天地之性，众胜寡，故水胜火。精胜坚， 故火胜金。刚胜柔，故金胜木。专胜散，故木胜土。实胜虚， 故土胜水。 [2] 
金克木，因为金属铸造的割切工具可锯毁树木。（有矿的土地不长草）
木克土，因为树根吸收土中的营养，以补己用，树木强壮了，土壤如果得不到补充，自然削弱。
土克水，因为土能防水。（兵来将挡水来土掩）
水克火，因为火遇水便熄灭。
火克金，因为烈火能融化金属。 [2]

金蛇人的财运(辛已年：1941、2001、2013年出生)

金蛇人的财运平平稳稳。金蛇人独立意识很强，不喜欢与人合作。内心情感丰富，有强烈的审美意识，
金钱大都花费在自己的着装上。若命中有财运吉星相助，金蛇人多是心平气和，能进能退，自力更生的人，
会因人成事获得赚钱的机会，若命中没有财运吉星相助，金蛇人会终生奔波忙碌，但收入足以维持家计。

土狗年是哪些年份

从干支组合当中看，出生在戊戌年的属狗人就称为土狗。土狗年主要是1958、2018年，属于戊戌年生平地木命。古人称“土爰稼穑”，就是说土有种植和收获庄稼的用处，所以也可以说一切具有生化、承载、受纳作用的事物，都可以归属于土。故自古就有“土载四行”和“土为万物之母”的说法。

土狗年出生人的性格
土狗年出生的人，做任何事情都会善始善终，性格执着，能够贯彻到底，绝不半途而废。明辨是非，
认为只要脚踏实地的走好自己的路就可以了。土狗人也不会见异思迁，经常会以身怀一技，贯彻一职为原则，
也以此为乐。偶尔表现出顽固的个性，心情不好的时候别人不管怎么劝导安慰都无动于衷。懂得尊重他人，
不喜欢干涉他人也不喜欢别人干涉自己。

土狗年出生人的命运
土狗人具有艺术气质，不太适合在竞争激烈的环境中发展。在这个讲究八面玲珑的社会中，并非他们的能力
和斗志比别人差，而是因为他们的性格无法一一迎合别人。个人精神也无法承受瞬息万变的生活。
工作总是认真负责，一丝不苟，所以成功的几率相当大。

土狗人财运方面比较理想，但是也要多加小心，谨防因为金钱问题和别人发生争执。所幸这些都是小问题，
对整体影响不大。赚钱的数目会慢慢增加，经济比较宽裕。如果自己有计划的话不妨着手进行，会有意想不到的效果。

木鼠之人
独立自尊，不趋炎附势，是一类受人尊敬的人，这也造成了两个方面的结果：
一是在官场不易攀升，二是大众缘好，在物质方面不愁，家庭融洽。
生肖为木鼠之人，通晓制度法规，遵守传统观念，群体观念强，尽管他们有时显得自私，但也显得随和，
也会关心别人，因为他们十分看重自己的人格和形象。在遵守原则的同时，为达到目的也十分灵活。
他们喜欢生活中有安全感，并且常有忧虑感，这也是他们为什么努力工作的原因之一。

水虎人的性格
水虎人充满自信，对自己的实力相当有信心，喜欢接受挑战，喜欢刺激的生活。能够全力以赴的面对困难，
不会因为一些小事或者小情绪的影响而乱了分寸。头脑冷静，心思细腻，而且勇于创新和接受新事物、
新创想和新事物。判断明确，很少出错。眼光敏锐，能够把握住机会。性格比较稳重，但是有时候会优柔寡断，
让机会白白错失。

水虎人的命运，水虎人喜欢新事物，特别是手工艺以及艺术方面。自尊心很强，容易自视清高，恃才傲物，
不容易接纳别人的意见，比较自我中心，我行我素，也容易引起别人的嫉妒。一生的事业好坏参半，若能
够得到朋友或者伴侣的帮助，能有崭新的发展前途。已婚人士，夫妻之间比较容易发生口角，争执，闹意
见的情况，应该尽量协调解决。经济困难的时候一般能顺利获得银行的借贷批准，让财务问题顺利解决。
还可能有意向不到的收获，建议可以试着做一些小投资。
'''