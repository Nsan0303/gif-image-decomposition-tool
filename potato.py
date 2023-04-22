from PIL import Image
import os
from tkinter import filedialog

typ = [('テキストファイル', '*.gif')]
dir = 'C:\\pg'
fle = filedialog.askopenfilename(filetypes=typ, initialdir=dir)

# GIFファイルを開く
gif_image = Image.open(fle)

# 出力先のフォルダーを作成する
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    # 新しいフォルダ名を生成する
    i = 1
    while True:
        new_output_folder = f"output_{i}"
        if not os.path.exists(new_output_folder):
            output_folder = new_output_folder
            os.makedirs(output_folder)
            break
        i += 1

# GIFをフレームごとに分解する
try:
    while True:
        current_frame = gif_image.tell()
        output_file = f"{output_folder}/frame_{current_frame}.png"
        if os.path.exists(output_file):
            # 新しいファイル名を生成する
            i = 1
            while True:
                new_output_file = f"{output_folder}/frame_{current_frame}_{i}.png"
                if not os.path.exists(new_output_file):
                    output_file = new_output_file
                    break
                i += 1
        gif_image.save(output_file, "png")
        gif_image.seek(current_frame + 1)
except EOFError:
    pass