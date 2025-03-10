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

I can see why people didn't like this one.