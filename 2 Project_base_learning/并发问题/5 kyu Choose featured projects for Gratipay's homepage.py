'''
https://www.codewars.com/kata/591b9c07266a3164c90001fe/train/python

Gratipay通过提供一个每周提示/捐款的平台来帮助资助开源项目。目前的主页列出了所有的项目，并附有图片。由于项目的数量不断增加，Gratipay现在遇到了扩展问题 帮助Gratipay设计一个解决方案，使主页上只显示少数几个 "特色 "项目。

这个解决方案的核心是一个单一的函数。

def get_featured_projects(all_projects):
  ...
all_projects是一个项目数组，它是格式为字典/散列的。

{
  'name': 'Project name',
  'nreceiving_from': 10,
  'receiving':  10,
}
get_featured_projects/getFeaturedProjects预计将根据以下规范过滤出一个特色项目列表。

总是返回10个或更少的项目。
其中7个项目应该从热门项目库中随机抽取（nreceiving_from>5的项目被认为是热门项目）。剩下的三个应该从其他项目中随机抽取。
如果总共有少于10个项目，只需返回所有项目。
如果少于7个受欢迎的项目，或者少于3个不受欢迎的项目，如果可能的话，从另一组项目中填补空白。
将结果的顺序随机化，这样受欢迎的项目就不会总是出现在上面。
注意：Gratipay的代码库是开放源代码的，尽量抵制作弊的诱惑吧

def get_fake_projects(npopular, nunpopular):
    popular = [
        { 'name': 'Popular Project %s' % str(p), 'nreceiving_from': 7, 'receiving': 10 }
        for p in range(0, npopular)
    ]

    unpopular = [
        { 'name': "Unpopular Project %s" % str(p), 'nreceiving_from': 3, 'receiving': 4 }
        for p in range(0, nunpopular)
    ]

    return popular + unpopular

def get_featured_project_counts(projects):
    featured_projects = get_featured_projects(projects)
    popular = [x for x in featured_projects if x['nreceiving_from'] > 5]
    unpopular = [x for x in featured_projects if x['nreceiving_from'] <= 5]

    return [len(popular), len(unpopular)]

def test_should_choose_more_popular_than_unpopular():
    projects = get_fake_projects(10, 5)
    npopular, nunpopular = get_featured_project_counts(projects)

    test.assert_equals(npopular, 7, "Expected 7 popular projects")
    test.assert_equals(nunpopular, 3, "Expected 3 unpopular projects")

test.it("should choose more popular than unpopular")
test_should_choose_more_popular_than_unpopular()

def test_should_deal_with_zero_unpopular_projects():
    projects = get_fake_projects(10, 0)

    npopular, nunpopular = get_featured_project_counts(projects)
    test.assert_equals(npopular, 10, "Expected 0 popular projects")
    test.assert_equals(nunpopular, 0, "Expected 10 unpopular projects")

test.it("should deal with zero unpopular projects")
test_should_deal_with_zero_unpopular_projects()
'''

def get_featured_projects(all_projects):
    '''
    {
    'name': 'Project name',
    'nreceiving_from': 10,
    'receiving':  10,
    }

    '''
    popular,unpopular = [],[]
    for n in all_projects:
        if n["nreceiving_from"] > 5:
            popular.append(n['name'])

        elif n["nreceiving_from"] <= 5:
            unpopular.append(n['name'])

    return 'featured_projects'