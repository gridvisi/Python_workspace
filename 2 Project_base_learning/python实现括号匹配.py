'''
由于存在多种不同的括号对，每种括号都可能任意出现多次，而且还有可能嵌套，为了检查是否匹配，扫描中必须保存遇到的开括号。由于写程序时候无法预知要处理多少括号，因此不能用固定数量的变量保存所以我们必须要借助缓存结构。

由于在匹配的过程中会出现嵌套，所以进行逐对的匹配。会拿右括号和最近的左括号进行匹配，如果匹配成功就会删除匹配成功的括号，进行下一次匹配。所以是后存入的括号最先进行匹配，因此选择栈结构作为缓存结构。

Python程序的实现的步骤如下：

1.顺序检查被检查的字符串

2.直到遇到开括号时候将其压入栈中

3.遇到右括号的时候将弹出当前的栈顶元素与之进行匹配

4.如果匹配成功则继续进行匹配，发现不匹配时候，匹配结束，结束匹配

'''
class SStack():
    def __init__(self):
        self.__elem = []
    def is_empty(self):
        return self.__elem == []
    def top(self):
        return self.__elem[-1]
    def push(self,elem):
        self.__elem.append(elem)
    def pop(self):
        return self.__elem.pop()

def kuohao(text):
    kinds = "()[]{}"#用来定义出现的括号，因为待匹配的字符中含有其他的字符，我们值检查括号是否匹配，而且是只有出现括号后再进行匹配
    zuo = "([{" #定义左括号，如果是左括号就入栈
    dict0 = {")":"(","]":"[","}":"{"}#匹配字典，这个字典定义了匹配规则，如果字典的键值对匹配就可以认定括号是匹配的
    def pipei(text):     #将等待匹配的文本输入，这个函数的目标是从文本中过滤出括号
        i,text_len = 0,len(text) #扫描指针用来记录匹配位置
        while True:
            while  i< text_len and text[i] not in kinds: #用来寻找到括号
                i += 1
            if i >= text_len: #如果字符串中没有包含括号则结束
                return
            yield text[i],i  #返回括号字符和字符对应的下标
            i += 1

    st = SStack()
    for text0,i in pipei(text):#获取得到的符号进行匹配,因为pipei（）是一个含有yield函数，所以是一个生成器，调用它会产生一个可迭代的对象
        if text0 in zuo: #如果是左括号就让它入栈
            #print(text0)
            st.push(text0)
        elif st.pop() != dict0[text0]:#如果是右括号，就弹出栈顶元素进行匹配检查
            print("本次不匹配")
            return False #遇到不匹配的，就直接退出函数，结束匹配
    print("所有的括号都已经匹配完毕，匹配成功！") #如果函数还能够执行到这里说明所有的括号都是匹配的
    return True
#kuohao("({{[]}})")
kuohao("[{]}")
kuohao("hello example (words(more words) here) something")



SYMBOLS = {'}': '{', ']': '[', ')': '(', '>': '<'}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()

def check(s):
    arr = []
    for c in s:
        if c in SYMBOLS_L:
            # 左符号入栈
            arr.append(c)
        elif c in SYMBOLS_R:
            # 右符号要么出栈，要么匹配失败
            if arr and arr[-1] == SYMBOLS[c]:
                arr.pop()
            else:
                return False

    return True

print(check("3 * {3 +[(2 -3) * (4+5)]}"))
print(check("3 * {3+ [4 - 6}]"))


# 存储左括号和右括号
open_brackets = '([{<'
close_brackets = ')]}>'
# 映射左右括号便于出栈判断
brackets_map = {')': '(', ']': '[', '}': '{', '>': '<'}

# 对于每一行数据，进行如下判定若括号为左括号，加入栈，若括号为右括号，判断是否跟栈尾括号对应，
#  若对应，弹出栈尾元素，若所有括号均正确闭合，则最后栈为空。

rows = [
'([<^>x[ ]{a}]{/}{t}g<^>)<{x}b>{x}<z({%}w >[b][c[c]]{<h>{h}}',
 '[/]{((x)({{*}*}w)w){f}{v}[%(^[z]{u}{ })([[ ]-]h)]{c}(*)[y]}',
 '<<(^)z>>[b]< >[[(c)u[v]{z<b< >><b>}]g][/b[(])v(v)(+)](v)',
 '[[b]][(v)g]<z>([{{<->+}e}[*]d<+>]g[[a] <+>(v){b}<e>]){a}[u]']

for row in rows:
    stack = []
    label = True
    for char in row:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if len(stack) < 1:
                label = False
                break
            elif brackets_map[char] == stack[-1]:
                stack.pop()
            else:
                label = False
                break
        else:
            continue
    if stack != []:
        label = False
    print(label)

