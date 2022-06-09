try:
    import os
    maindl = "pip install -i "
    print("---===Python 库下载器===---")
    libname = input("请输入库名:")
    print("下载源:")
    print("1.阿里镜像(mirrors.aliyun.com)")
    print("2.豆瓣镜像(pypi.douban.com)")
    print("3.清华镜像(pypi.tuna.tsinghua.edu.cn)")
    print("4.中国科大(pypi.mirrors.ustc.edu.cn)")
    print("5.华中科大(pypi.hustunique.com)")
    print("6.官方下载(pypi.org)")
    sel = int(input("请选择:"))
    if sel == 1:
        os.system(maindl+"http://mirrors.aliyun.com/pypi/simple/ "+libname)
    elif sel == 2:
        os.system(maindl + "http://pypi.douban.com/simple/ " + libname)
    elif sel == 3:
        os.system(maindl + "https://pypi.tuna.tsinghua.edu.cn/simple/ " + libname)
    elif sel == 4:
        os.system(maindl + "http://pypi.mirrors.ustc.edu.cn/simple/ " + libname)
    elif sel == 5:
        os.system(maindl + "http://pypi.hustunique.com/ " + libname)
    elif sel == 6:
        os.system("pip install "+libname)
except: quit()