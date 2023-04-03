import os
from fontTools.ttLib import TTFont
from fontTools.pens.freetypePen import FreeTypePen
from freetype import ft_errors

png_f = "png_fonts\\"
not_work_list = []
#cyrillic = [
#    chr(n) for n in range(ord("а"), ord("я") + 1)
#] + [
#    chr(n) for n in range(ord("А"), ord("Я") + 1)
#]

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
        pass
    
    for n in range(0, 1000):
        c = chr(n)
        try:
            glyph = font.getGlyphSet()[c]
            pen = FreeTypePen(None)
            glyph.draw(pen)
            a = 0
            a = pen.image(width=0, height=0, contain=True)
            a = a.resize((256, 256))
            a.save(f"{png_f}{name}\\{n}{c}.png")
        except:
            pass


    work = False
    for i in range(81):
        code_ = "uni0" + str(hex(int(0x401) + i))[2:].upper()
        try:
            glyph = font.getGlyphSet()[code_]
            pen = FreeTypePen(None)
            glyph.draw(pen)
            a = pen.image(width=0, height=0, contain=True)
            a = a.resize((256, 256))
            a.save(f"{png_f}{name}\\cyr_{i}.png")
            work = True
        except KeyError:
            pass
        except TypeError:
            pass
        except ft_errors.FT_Exception:
            pass
    if work == False: # type: ignore
        del_(name)
    else:
        print("success")
