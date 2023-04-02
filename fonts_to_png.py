import os
from fontTools.ttLib import TTFont
from fontTools import config
from fontTools.pens.freetypePen import FreeTypePen
from fontTools.misc.transform import Offset
import PIL

pen = FreeTypePen(None)
font_name, way = "Disket-Mono-Regular", r"C:\Users\cycli\AppData\Local\Microsoft\Windows\Fonts"
font = TTFont(f"{way}\\{font_name}.ttf")

try:
    os.chdir(font_name)
except:
    os.mkdir(font_name)
    os.chdir(font_name)
for c in [chr(n) for n in range(0, 10000)]:
    try:
        glyph = font.getGlyphSet()[c]
        pen = FreeTypePen(None)
        glyph.draw(pen)
        a = 0
        a = pen.image(width=0, height=0, contain=True)
        a = a.resize((256, 256))
        a.save(f"{c}.png")
    except:
        pass

for code in ["ch247", "uni0410", "Iocyrillic"]:
    try:
        glyph = font.getGlyphSet()[code]
        pen = FreeTypePen(None)
        glyph.draw(pen)
        a = pen.image(width=0, height=0, contain=True)
        a = a.resize((256, 256))
        a.save(f"code.png")
    except KeyError:
        print(f"Некорректный код: {code}")

font.saveXML("AA.xml")