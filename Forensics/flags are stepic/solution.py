from PIL import Image
import stepic

im = Image.open("upz.png")
data = stepic.decode(im)
print(data)