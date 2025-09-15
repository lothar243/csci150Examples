#!/usr/bin/python3

# if the PIL package ins't already installed, try the following:
# python -m ensurepip --user
# python -m pip install pillow
from PIL import Image

# Load an image
img = Image.open('missoula-college_logo.png')

# Get basic image info
print(img.format)
print(img.mode)
print(img.size)

# show the image
img.show()

# invert the image colors and remove transparancy
(x_size, y_size) = img.size
for x in range(x_size):
    for y in range(y_size):
        (r, g, b, a) = img.getpixel((x, y))
        img.putpixel((x, y), (255 - r, 255 - g, 255 - b, 255))

img.save('mytest.png')
img.show()