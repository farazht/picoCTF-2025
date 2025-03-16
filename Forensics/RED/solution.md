## RED

The first thing I did with the image was open it in an image editor to see if every pixel was truly the same color - it wasn't. 

Then, I checked the metadata, which revealed a cryptic message:

> Crimson heart, vibrant and bold, Hearts flutter at your sight. Evenings glow softly red, Cherries burst with sweet life. Kisses linger with your warmth. Love deep as merlot. Scarlet leaves falling softly, Bold in every stroke.

After a concerningly time of thinking this was just a distraction, we found out that the first letter of each sentence spelled out "CHECK LSB". Even though this was exactly what I was already doing, it was reassuring to know that I wasn't wasting my time.

Using Python's `PIL` library, I wrote a script to extract the least significant bit of each pixel in the image, from all four of the RGBA channels. Since every row was the same, I only needed to check the first row. After concatenating the bits, I converted them from binary to ASCII to get the following base64 encoded string:

`cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==`

Finally, I decoded the string to get the flag: `picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}`

Here's a snippet of the script I used:

```python
for i in range(0, width):
    pixel = pixels[i]
    r, g, b, a = pixel
    lsbs.append((r & 1, g & 1, b & 1, a & 1))

# LSBs of r, g, b, a, all concatenated into a single binary string 
binary = ''.join(f"{r_lsb}{g_lsb}{b_lsb}{a_lsb}" for r_lsb, g_lsb, b_lsb, a_lsb in lsbs)

# Converting to text results in a base64 encoded string
n = int(binary, 2)
b64 = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
```