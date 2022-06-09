
class Get_weight:
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def compare(self):
        return sum(self.left) - sum(self.right)

def find_Apple(scales,step):
    #balls = [0, 1, 2, 3, 4, 5, 6, 7]

    balls = scales
    while len(balls) > 1:
        balls = balls[1:] if len(balls) % 2 else balls
        left, right = balls[:len(balls)//2], balls[len(balls)//2:]
        #scales = Get_weight(left,right)
        w = Get_weight(left,right).compare()
        if w == 0:
            return '1',balls[0],step
        else:
            balls = left if w > 0 else right
            print('balls =',balls)
            step += 1
    return '2',balls[0],step

scales,step = [5,5,5,5,8,5,5,5,5,5,5,5,5,5,5,5,5],0
scales,step = [5,5,5,5,8,5,5,5,5],0
#scales,step = [5,5,5,5,5,5,5,5,5,5,5,5,8],0 #len=13
print(find_Apple(scales,step))

# step == math.log
import math
print(math.ceil(math.log(len(scales),2)))
print(math.ceil(math.log(2*len(scales),3))+1)


print("------- 三分必居其一 ----")


class Get_weight: #模拟天平
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def compare(self):
        return sum(self.left) - sum(self.right)

def find_Apple(scales,step):

    balls,head = scales,scales[:len(scales)%3]

    while len(balls) > 1:
        print('balls =', balls)
        n = len(balls)
        pre,balls = balls[:n%3],balls[n%3:]

        left, right, table = balls[:n//3], balls[n//3:2*(n//3)],balls[2*(n//3):]
        print(n,pre,left,right,table)
        if sum(left) == sum(right):
            balls = pre + table
            step += 1
        else:
            if sum(left) == sum(table):
                balls = pre+right
                step += 1

            elif sum(right) == sum(table):

                balls = pre+left
                step += 1

    return '目标球和称重次数:',balls[0],step

scales,step = [5,5,5,5,8,5,5,5,5],0
scales,step = [5,5,5,8,5,5,5,5,5],0 #len=13

scales,step = [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
               5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
               5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
               5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
               5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
               5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
               5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
               5,5],0
print(find_Apple(scales,step))

# step == math.log
import math
#print(math.ceil(math.log(len(scales),2)))
print(len(scales),math.ceil(math.log(len(scales),3)))

print(scales[:len(scales)%3])