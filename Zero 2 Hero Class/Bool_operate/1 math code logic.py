# 一个年级有300个同学，每个同学都有数学成绩记录，但没有参加逻辑和编程课的经历
# 所以，无法提供上述两门课程的成绩。我们需要评估，按照上述选拔的标准，选拔结果
# 各有不同，差别是多少？


math,logic,code = (0,1),(0,1),(0,1)

for m in math:
    for l in logic:
        for c in code:
            if math == True:
                print(True)
import random
math, logic, code = True, True, random.choices([True, False])#random.choices(True, False)
print(code)
print(math and logic == True)
print(math and logic and code[0] == True)
print(math and logic or code[0] == True)
