import os
import shutil

n = 118
val = 33 * 2
train = 26 * 2
for dir_ in os.listdir("./png_fonts"):
    try:
        os.mkdir(f"./AI_train/train/{dir_}")
    except:
        pass
    try:
        os.mkdir(f"./AI_train/val/{dir_}")
    except:
        pass
    
    files = os.listdir(f"./png_fonts/{dir_}")
    for i in range(train):
        file = os.listdir(f"./png_fonts/{dir_}")[i]
        try:
            os.mkdir(f'./Ai_train/train/{dir_}') #всё равно, папка и так норм создавалась
        except:
            pass
        shutil.copy(f"./png_fonts/{dir_}/{file}", f'./Ai_train/train/{dir_}/{file}')
    for j in range(val):
        file = os.listdir(f"./png_fonts/{dir_}")[train + j]
        shutil.copy(f"./png_fonts/{dir_}/{file}", f'./Ai_train/val/{dir_}/{file}')