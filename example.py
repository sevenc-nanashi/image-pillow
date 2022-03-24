import pjsekai_background_gen_pillow as pjbg
from PIL import Image

generator = pjbg.Generator()
generator.generate(Image.open("test.png")).save("dist.png")
