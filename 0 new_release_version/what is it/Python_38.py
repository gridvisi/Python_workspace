
'''
赋值表达式
Python 3.8最明显的变化就是赋值表达式，即:=操作符。赋值表达式可以讲一个值赋给一个变量，即使变量不存在也可以。它可以用在表达式中，无需作为单独的语句出现。
while (line := file.readline()) != "end":    print(chunk)"end":
    print(chunk)
上例中，如果变量line不存在则会被创建，然后将file.readline()的返回值赋给它。然后检查line是否为"end"。如果不是，则读取下一行，保存在line中，然后继续测试。
赋值表达式遵循了Python一贯简洁的传统，就像列表解析式一样。其目的在于避免在特定的Python编程模式中出现一些枯燥的样板代码。例如，上述代码用一般写法需要多写两行代码。
'''

