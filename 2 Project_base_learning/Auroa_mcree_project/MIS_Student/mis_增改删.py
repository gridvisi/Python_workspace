import json  # 把字符串类型的数据转换成Python基本数据类型或者将Python基本数据类型转换成字符串类型。


def login_user():
    while True:
        register = input('学生姓名：')
        try:
            with open(register + '.json')as file_object:
                user_message = json.load(file_object)  # json.load(obj)	读取文件中的字符串，序列化成Python的基本数据类型
        except FileNotFoundError:
            print('该用户不存在！')
            break
        else:
            print('_' * 20)
            register_password = input('请输入学号：')
            if user_message['id'] == register and user_message['password'] == register_password:

                str_print = '姓名：{}\t数学成绩：{}\t语文成绩：{}\t英语成绩: {}'
                grade_list = []
                while 1:

                    print('''******************************
                          欢迎使用【学生信息管理系统】
                          请选择你想要进行的操作
                          1.新建学生信息
                          2.显示全部信息
                          3.查询学生信息
                          4.删除学生信息
                          5.修改学生信息
                          0.退出系统
                    ******************************''')

                    action = input('请选择你想要的进行操作:\n')
                    if action == '1':
                        '''新建学生信息'''
                        name = input('请输入名字')
                        math = input('请输入数学成绩')
                        chinese = input('请输入语文成绩')
                        english = input('请输入英语成绩')

                        total = int(math) + int(chinese) + int(english)
                        grade_list.append([name, math, chinese, english, total])
                        print([name, math, chinese, english, total])
                        print('姓名：{}\t数学成绩：{}\t语文成绩：{}\t英语成绩: {}'.format(name, math, chinese, english, total))
                        pass



                    elif action == '2':
                        '''显示全部信息'''
                        for info in grade_list:
                            print(str_print.format(*info))


                    elif action == '3':

                        '''查询学生信息'''
                        name = input('请输入你需要查询学生的姓名：')
                        for info in grade_list:
                            if name in info:
                                print(str_print.format(*info))
                                break
                            else:

                                print('此学生不存在')




                    elif action == '4':

                        '''删除学生信息'''
                        name = input('请输入你需要查询学生的姓名：')
                        for info in grade_list:
                            if name in info:
                                info_ = grade_list.pop(grade_list.index(info))
                                print('这个学员的信息已经被删除\n', info_)
                                break
                            else:
                                print('此学生不存在')



                    elif action == '5':
                        '''修改学生信息'''
                        name = input('请输入你需要查询学生的姓名：')
                        for info in grade_list:
                            if name in info:
                                index = grade_list.index(info)

                                break
                            else:
                                print('此学生不存在')
                                continue

                        math = input('请输入数学成绩:')
                        chinese = input('请输入语文成绩:')
                        english = input('请输入英语成绩:')
                        total = int(math) + int(chinese) + int(english)
                        grade_list[index][0:] = [name, math, chinese, english, total]
                        print('修改后的一个成绩', grade_list[index])

                    elif action == '0':
                        '''退出系统'''
                        break
                    else:
                        print('输入信息有误，请重新输入')

                # print('登陆成功')
                return register, user_message
            else:
                print('登陆失败！用户名或密码错误')
                break


def register_user():
    new_user = input('增加学生姓名：')
    try:
        with open(new_user + ',.jion', 'r') as file_object:
            pass
    except FileNotFoundError:

        new_password_one = input('请确认学号：')
        new_password_two = input('请再次确认学号：')
        if new_password_one == new_password_two:
            user_message = {'id': new_user, 'password': new_password_one}
            with open(new_user + '.json', 'w')as file_object:
                json.dump(user_message, file_object)  # json.dump(obj)	将Python的基本数据类型序列化成字符串并写入到文件中
                print('新用户已经注册成功！可以登录了。')
        else:
            print('两次输入不一致')
    else:
        print('该用户已经存在')


while True:
    print('*' * 50)
    print('*      1.登录用户          *')
    print('*                           *')
    print('*       2.注册用户          *')
    print('*                           *')
    print('*        3.退出             *')
    print('*' * 50)
    test_content = input('请输入你的选项：')
    if test_content == '1':
        try:

            user_id, user_system = login_user()
            pass
        except TypeError:
            print('请重新输入')
    # print('登录用户！')
    elif test_content == '2':
        register_user()

        # print('注册用户')
    elif test_content == '3':

        print('退出系统')
        break
    else:
        print('非法输入字符')
