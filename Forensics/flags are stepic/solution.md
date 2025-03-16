## flags are stepic

After scrolling through a webpage of country flags, it's clear which one is the odd one out. Upanzi is the only flag that doesn't belong to a country, and it's also over 14000 pixels wide (as opposed to the usual ~250).

This challenge had one of the lowest like-rates by far (around 25% of participants liked it), so I knew something was up. After doing some research on what *stepic* could mean, I found a Python library called [Stepic](https://pypi.org/project/stepic/) (I also found an UrbanDictionary entry claiming it meant *stellar + epic*). 

I just used the library to decode the hidden message, thinking that it surely wouldn't work.

```python
from PIL import Image
import stepic

im = Image.open("upz.png")
data = stepic.decode(im)
print(data)
```

```
> picoCTF{fl4g_h45_fl4g1a2a9157}
```

Oh, okay.

Let's take a look at `stepic`'s `decode` function to see why that worked.

```python
def decode(image):
    '''Extracts data from an image'''

    _validate_image(image)
    return ''.join(decode_imdata(image.getdata()))

def decode_imdata(imdata):
    '''Given a sequence of pixels, returns an iterator of characters encoded in the image'''

    imdata = iter(imdata)
    while True:
        pixels = list(imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3])
        byte = 0
        for c in range(7):
            byte |= pixels[c] & 1
            byte <<= 1
        byte |= pixels[7] & 1
        yield chr(byte)
        if pixels[-1] & 1:
            break
```

The `decode` function iterates over the image's pixel data and extracts the least significant bit of each color channel. 

I can see why people didn't like this one. It's quite similar to [RED](../RED/solution.md).