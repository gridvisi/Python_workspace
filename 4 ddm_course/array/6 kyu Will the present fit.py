'''
https://www.codewars.com/kata/52b23340c65ea422b1000045/train/python
圣诞老人的精灵们正在给礼物装箱，他们需要你的帮助。写一个函数，分别接受礼物和盒子的两个尺寸序列，
并根据礼物是否能装进提供的盒子里返回一个布尔值。盒子的壁厚是一个单位，所以一定要考虑到这一点。

举例说明。礼物和盒子分别是

[10, 7, 16], [13, 32, 10] --> true, 箱子比礼物大。
[5, 7, 9], [9, 5, 7] --> false, present和盒子的大小相同。
[17, 22, 10], [5, 5, 10]) --> false, 箱子太小了。
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(will_fit((10, 2, 4), (6, 4, 12)), True)
    test.assert_equals(will_fit((1, 2, 3), (2, 1, 3)), False)
'''
def will_fit(present, box):
    return all([x < y-1 for x,y in zip(sorted(present),sorted(box))])
