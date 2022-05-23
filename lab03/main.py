# Copyrights
# Patryk Wawrzyniak

from PIL import Image
import hashlib
import random

input_image = Image.open("images/b.bmp")


def save(data, where="images/image.bmp", message="Done"):
    new_data = bytes(data)

    output_image = input_image.copy()
    output_image.frombytes(new_data)
    output_image.save(where)
    print(message)


block_size = 8
image_data = input_image.tobytes()
size = input_image.size

# ECB
new_data = []
keys = []
for x in range(block_size):
    # key = hashlib.md5(str(x ** 3 + x).encode("UTF-8")).digest()
    key = hashlib.md5(str(random.random() * x).encode("UTF-8")).digest()
    keys.append(key)

for x in range(size[0]):
    for y in range(size[1]):
        pp = x * size[0] + y  # pixel position
        op = image_data[pp]  # original pixel
        pta = op ^ keys[x % block_size][y % block_size]     # pixel to add
        new_data.append(pta)

save(new_data, "images/ecb_crypto.bmp", "you can see me :-(")


# CBC
new_key = 13
new_data = [image_data[0] ^ new_key]
for x in range(size[0]*size[1]):
    new_data.append(new_data[x-1] ^ image_data[x] ^ keys[x%64//8][x%8])

save(new_data, "images/cbc_crypto.bmp", "you can't see me ;-D")

print("Done")
