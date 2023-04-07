import os

os.chdir("png_fonts")

n = 0
for font in os.listdir():
    cnt = len(os.listdir(font))
    if cnt != 118:
        n += 1

print(n, "incorrect fonts")