# https://www.geeksforgeeks.org/working-images-python/?ref=lbp

from PIL import Image

image = Image.open('E://brilliant//fail to pay.jpg')  # 创建图像实例
# 查看图像实例的属性
print(image.format, image.size, image.mode)

image.show() # 显示图像
import PIL
image = PIL.Image.new(mode = "RGB",
                      size = (200, 200),
                      color = (255, 153, 255))
image.show()

from PIL import Image

image = Image.open('2092.jpg')
image.show()
image.save('1.jpg')
print(image.mode, image.size, image.format)
# RGB (481, 321) JPEG