from PIL import Image
import hashlib
import random

block_size = 8
input_image = Image.open("images/mcqueen.bmp")
image_data = input_image.tobytes()
new_data = []
size = input_image.size

keys = []
for x in range(block_size):
    #key = hashlib.md5(str(x ** 3 + x).encode("UTF-8")).digest()
    key = hashlib.md5(str(random.random() * x).encode("UTF-8")).digest()
    keys.append(key)

for x in range(size[0]):
    for y in range(size[1]):
        pp = x * size[1] + y  # pixel position
        op = image_data[pp]  # original pixel
        pta = op ^ keys[x % block_size][y % block_size]     # pixel to add
        new_data.append(pta)

new_data = bytes(new_data)

output_image = input_image.copy()
output_image.frombytes(new_data)
output_image.save("images/ECB.bmp")
print("I'm speed!")
