from PIL import Image
import stepic
import inspect

im = Image.open("upz.png")
data = stepic.decode(im)
print(inspect.getsource(stepic.decode_imdata))
print(data)