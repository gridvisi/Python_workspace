'''
今天是草原动物园的升级任务：准备参加出国编程夏令营。
运用数组循环操作实现查询是否成功申请到签证，是否成功申请到资金，
并合并以上步骤，查询是否完全具备条件顺利出行，每一步给与成功或失败提示
'''

applicant = ['jiajia','lucas','Peter_parker','mcree','alex']

'''
my_name = input('name:')
for name in applicant:
    if my_name == name:
        print('yes,i apply for visa success!')
    else:
        print('sorry,try it again')
    if my_name != name:
        print('?')
'''
# apply for visa and funding
# 草原动物园的升级任务
# 申请出国参加编程夏令营的过程中，如何查询是否申请到签证，和是否申请到资金？
# 如何合并上述步骤，查出能否最终顺利出发

my_name = input('name:')
# 查询自己是否在已经成功申请到签证的名单里？
#
applicant_visa = ['jiajia','lucas','Peter_parker','mcree','alex','tommy']

if my_name in applicant_visa:
    print(my_name,'yes,i apply for visa success')
else:
    print(my_name,'You fail to apply for visa , try again!')

# 查询自己是否在已经成功申请到预算的名单里？

applicant_funding = ['eric','bill','jiajia','summer','Peter_parker','mcree','emma']
#my_name = input('name:')
if my_name in applicant_funding:
    print(my_name,'yes,i apply for founding success')
else:
    print(my_name,'you fail to apply for funding, try it again')

print('两步合并为一步,第一种写法：')
if my_name in applicant_funding:
    if my_name in applicant_visa:
        print(my_name,'apply for MIT university success')
    else:
        print(my_name,'Try it again')

tommy_profile = {'year':12,'school':'yizhong','family':'extend','glass':True}
alex_profile = {'year':12,'school':'巴蜀','family':4,'glass':False}
# key 键值

print('第2种写法,how to show the error tips：')
# 以下代码压根没有执行？ why？ 为什么，那怎么改？

if my_name in applicant_visa:

    if my_name in applicant_funding:
        print("in visa")
        print(my_name,'apply for MIT university success,really?')
    else:
        print("in visa")
        print(my_name,'Try it again')
else:
    print("not in visa")
    if my_name in applicant_funding:
        print(my_name,'apply for MIT university success,really?')
    else:
        print(my_name,'Try it again')


print('换个方式')
if my_name in applicant_funding:
    if my_name in applicant_visa:
        print(my_name,'apply for MIT university success')
    else:
        print(my_name,'Try it again')

print('第3种写法：')

# 以下代码压根没有执行？ why？ 为什么，那怎么改？

if my_name in applicant_visa:
    if my_name in applicant_funding:
        print(my_name,'apply for MIT university success')
    else:
        print(my_name,'Try it again')

print('# 终极写法？')
#该怎么解决第一次查询的踩空的问题？


print('两步合并为一步')
if my_name in applicant_funding and applicant_visa:
    print(my_name,'apply for MIT university success')
else:
    print(my_name,'Try it again')

if my_name in applicant_funding and my_name in applicant_visa:
    print(my_name,'apply for MIT university success')
else:
    print(my_name,'Try it again')
