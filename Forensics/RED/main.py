from PIL import Image
import base64

im = Image.open('red.png')
pixels = list(im.getdata())

width, height = im.size
lsbs = []

for i in range(0, width):
    pixel = pixels[i]
    r, g, b, a = pixel
    lsbs.append((r & 1, g & 1, b & 1, a & 1))

# LSBs of r, g, b, a, all concatenated into a single binary string 
binary = ''.join(f"{r_lsb}{g_lsb}{b_lsb}{a_lsb}" for r_lsb, g_lsb, b_lsb, a_lsb in lsbs)

# Converting to text results in a base64 encoded string
n = int(binary, 2)
b64 = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

# Decoding the base64 string
decoded = base64.b64decode(b64)
print(decoded)