import os
from fontTools.ttLib import TTFont
from fontTools.pens.freetypePen import FreeTypePen

png_f = "png_fonts\\"
not_work_list = []
cyrillic = [
    chr(n) for n in range(ord("а"), ord("я") + 1)
] + [
    chr(n) for n in range(ord("А"), ord("Я") + 1)
]

def del_(name):
    dir_ = png_f + name
    for file in os.listdir(dir_):
        os.remove(dir_ + "\\" + file)
    os.rmdir(png_f + name)

for name in os.listdir("fonts"):
    print(name)
    font = TTFont(f"fonts\\{name}")

    name = name[:-4]

    try:
        os.mkdir(png_f + name)
    except:
        print("exists")
    
    for c in [chr(n) for n in range(0, 10000)]:
        try:
            glyph = font.getGlyphSet()[c]
            pen = FreeTypePen(None)
            glyph.draw(pen)
            a = 0
            a = pen.image(width=0, height=0, contain=True)
            a = a.resize((256, 256))
            a.save(f"{png_f}{name}\\{c}.png")
        except:
            pass

    for code in [("uni0", 0x40F)]:
        work = False
        for i in range(66):
            code_ = code[0] + str(hex(int(code[1]) + i))[2:].upper()
            try:
                glyph = font.getGlyphSet()[code_]
                pen = FreeTypePen(None)
                glyph.draw(pen)
                a = pen.image(width=0, height=0, contain=True)
                a = a.resize((256, 256))
                a.save(f"{png_f}{name}\\{i * 'а'}.png")
                work = True
            except KeyError:
                pass
    if work != True: # type: ignore
        del_(name)

