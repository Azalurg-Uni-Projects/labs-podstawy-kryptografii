from PIL import Image
import numpy as np
import hashlib
from itertools import cycle

img = Image.open('images/panda.bmp')
img = np.array(img)
img = np.append(img, img[0:], axis=1)

keys = hashlib.md5(b"key").digest()
input_image = Image.open("images/panda.bmp")
image_data = input_image.tobytes()
image_data = bytes(a^b for a, b in zip(image_data, cycle(keys)))
output_image = input_image.copy()
output_image.frombytes(image_data)
output_image.save("images/panda-copy.bmp")


# from PIL import BmpImagePlugin
# import hashlib
# from itertools import cycle
#
# keys = hashlib.md5(b"aaaabbbb").digest()
#
# input_image = BmpImagePlugin.BmpImageFile("img/tea.bmp")
#
# # extract pure image data as bytes
# image_data = input_image.tobytes()
#
# # encrypt
# image_data = bytes(a^b for a, b in zip(image_data, cycle(keys)))
#
# # create new image, update with encrypted data and save
# output_image = input_image.copy()
# output_image.frombytes(image_data)
# output_image.save("img/tea-encrypted.bmp")
