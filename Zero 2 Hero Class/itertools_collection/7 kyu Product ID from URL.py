'''
https://www.codewars.com/kata/5e2c7639b5d728001489d910/train/python

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(get_product_id("http://www.exampleshop.com/fancy-coffee-cup-p-90764-12052019.html"), "90764", 'should return 90764')
    test.assert_equals(get_product_id("http://www.exampleshop.com/dry-water-just-add-water-to-get-water-p-147-24122017.html"), "147", 'should return 147')
    test.assert_equals(get_product_id("http://www.exampleshop.com/public-toilet-proximity-radar-p-942312798-01012020.html"), "942312798", 'should return 942312798')
'''
url = "http://www.exampleshop.com/public-toilet-proximity-radar-p-942312798-01012020.html"
def get_product_id(url):
    #url_split = url.split('-')
    return url.split('-')[-2]
print(get_product_id(url))