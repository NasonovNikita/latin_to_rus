import os
from fontTools.ttLib import TTFont
from fontTools.pens.freetypePen import FreeTypePen

png_f = "png_fonts/"
success = 0
failure = 0
size = 72
#cyrillic = [
#    chr(n) for n in range(ord("а"), ord("я") + 1)
#] + [
#    chr(n) for n in range(ord("А"), ord("Я") + 1)
#]

def del_(name):
    dir_ = png_f + name
    for file in os.listdir(dir_):
        os.remove(dir_ + "/" + file)
    os.rmdir(png_f + name)

for name in os.listdir("fonts"):
    print(name)
    font = TTFont(f"./fonts/{name}")

    name = name[:-4]

    try:
        os.mkdir(png_f + name)
    except:
        print("exists")
        #continue    #turn on, if you are sure, that existing fonts are correct

    cnt = 0
    for n in range(0, 1000):
        c = chr(n)
        try:
            glyph = font.getGlyphSet()[c]
            pen = FreeTypePen(None)
            glyph.draw(pen)
            a = pen.image(width=0, height=0, contain=True)
            a = a.resize((size, size))
            a.save(f"{png_f}{name}/{n}{c}.png")
            cnt += 1
        except:
            pass
    
    for i in range(81):
        code_ = "uni0" + str(hex(int(0x401) + i))[2:].upper()
        try:
            glyph = font.getGlyphSet()[code_]
            pen = FreeTypePen(None)
            glyph.draw(pen)
            a = pen.image(width=0, height=0, contain=True)
            a = a.resize((size, size))
            a.save(f"{png_f}{name}/cyr_{i}.png")
            cnt += 1
        except:
            pass

    if cnt != 118: # type: ignore
        del_(name)
        print("failure")
        failure += 1
    else:
        print("success")
        success += 1

print(f"Success: {success}, fails: {failure}")