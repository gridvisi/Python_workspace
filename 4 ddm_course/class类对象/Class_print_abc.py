# 定义三角形类
class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def getArea(self):
        area = self.width * self.height / 2.0
        return area

# 定义正方形类
class Square:
    def __init__(self, size):
        self.size = size

    def getArea(self):
        area = self.size * self.size
        return area


# 初始化三角形类，建立实例myTriangle
myTriangle = Triangle(4, 5)
# 输出实例myTriangle的宽、高
print(myTriangle.width)

print(myTriangle.height)

#输出实例myTriangle的方法getArea()的返回值area
print(myTriangle.getArea())

# 注意不能用myTriangle.getArea()  代替，无输出结果显示或者
# 获取三角形类中的方法getArea()的返回值赋值给result
result = myTriangle.getArea()
# 输出getArea()的返回值area
print(result)


mySquare = Square(7)
print(mySquare.size)

print(mySquare.getArea())
