
# return masked string
'''
通常，当你买东西时，你会被问到你的信用卡号码，电话号码或你最秘密的问题的答案是否仍然正确。
然而，由于有人可能会从你的肩膀上看，你不希望在你的屏幕上显示出来。相反，我们对它进行屏蔽。
你的任务是写一个函数maskify，它可以将所有的字符（除了最后四个字符）变成'#'。

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
'''
def maskify(cc):
    return ''.join(['#' for _ in list(cc)[:-4]] + list(cc)[-4:])
cc = "4556364607935616"
#cc = "Skippy"
print(maskify(cc))

def maskify(cc):
    return f"{'#'*len(cc[:-4])}{cc[-4:]}"
# return masked string
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

# return masked string
def maskify(cc):
    return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))

def maskify(cc):
    return cc[-4:].rjust(len(cc), "#")