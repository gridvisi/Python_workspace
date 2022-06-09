
#25、下面函数的功能为_____。（将序列循环左移k位，得到新序列并返回）
lst = list('hello world,I love python')
k = 3
def demo(lst, k):
    head = lst[k % len(lst):]
    tail = lst[:k % len(lst)]  #[::-1]
    return ''.join(head + [' '] + tail)      #''.join(f"{head + tail}")
print(demo(lst, k))