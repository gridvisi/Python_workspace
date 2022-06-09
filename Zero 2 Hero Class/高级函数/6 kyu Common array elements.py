'''
6 kyu Common array elements
https://www.codewars.com/kata/5a6225e5d8e145b540000127/train/python

Test.it("Basic tests")
Test.assert_equals(common([1,2,3],[5,3,2],[7,3,2]),5)
Test.assert_equals(common([1,2,2,3],[5,3,2,2],[7,3,2,2]),7)
'''

from collections import Counter
def common(a,b,c):
    return sum((Counter(a) & Counter(b) & Counter(c)).elements())

# extend case study
# 学校统计竞赛队报名情况，你的任务是找出
'''
1、苹果apple英 ['æp(ə)l]  美bai ['æpl] 

2、梨子pear英 [peə]  美 [pɛr] 

3、桃子peach英 [piːtʃ]  美 [pitʃ] 

4、葡萄grape英 [greɪp]  美 [ɡrep] 

5、香蕉banana英 [bə'nɑːnə]  美 [bə'nænə] 

6、菠萝pineapple英 ['paɪnæp(ə)l]  美 ['paɪn'æpl] 

7、西瓜watermelon 英 ['wɔːtəmelən]  美 ['wɔtɚmɛlən] 

8、柠檬lemon英 ['lemən]  美 ['lɛmən] 

9、芒果mango 英 ['mæŋgəʊ]  美 ['mæŋɡo] 

10、草莓strawberry英 ['strɔːb(ə)rɪ]  美 ['strɔbɛri] 
'''
# 水果批发老板每天统计收到的订单，每种水果5kg起订，订单汇总后老板再批量进货。每个学校在前一天需求的水果名称
# 发送到老板手机上，你定义函数的输入是订单，每个学校的需求放在一个数组里,有重复的出现是因为订单信息发送的时间不同：
# 例如：["apple","banana","orange","pear","apple"]

order = [["apple","banana","orange","pear","apple"],
         ["grape","strawberry","orange","lemon"],
         ["citron","litchi","date","cherry","banana"],
         ["grape","apple","orange","grape"]
         ]

connection = [["alex","ada","eric","brown","jerry","andrew","alex"],
           ["charles","mark","ada","john","emma","olivia","isabella"],
            ["ava","daniel","ada","mattew","samuel","lucas","alex"],
           ["joseph","issac","noah","ella","ada","emma","aurora","ada"],
           ["isabella","jason","alex","aurora","jack","ada","emma"]]

from collections import Counter
def common(connection):
    root = Counter(connection[0])
    print(root,connection[1:])
    for p in connection[1:]:
        root &= Counter(p)
    return list(root.elements())

print(common(connection))

'''
今天的任务是在职场社交网站上找线索。你是公司负责招聘的经理，你的日常工作是在著名的linkedin
网站了解求职者的工作经历和同事关系。网站显示了每一位注册者的同事或朋友关系网络，你的公司通过
付费得到求职者的互相关注的​名单。

现在你要分析拿到的名单，找出5位求职者关注的名单中有没有共同认识的人。​已经给出5位求职者的关注
名单，输出同时出现在5份名单中的人，注意有重名的出现，你要做的就是先当作不同的人：

今天的任务是作为侦探的你，在调查学校的偷窃案。​你管辖的地区有5所学校失窃，你能想到的办法是查看最近校门口
放置的摄像头。最终你拿到了5份名单，名单是​

'''
