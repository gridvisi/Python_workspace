# https://www.geeksforgeeks.org/working-images-python/?ref=lbp


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