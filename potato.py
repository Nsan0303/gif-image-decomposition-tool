import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from tkinter import filedialog

# 参照ボタンのイベント
# button1クリック時の処理
def button1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file1.set(filepath)


# button2クリック時の処理
def button2_clicked():
    gif_image = Image.open(file1.get())



def show_complete_message():
    messagebox.showinfo("完了", "処理が完了しました。")
    sys.exit()

# button2クリック時の処理
def button2_clicked():
    gif_image = Image.open(file1.get())

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

    # 完了メッセージを表示する
    show_complete_message()

if __name__ == '__main__':
    # rootの作成
    root = Tk()
    root.title('')
    root.resizable(False, False)

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 参照ボタンの作成
    button1 = ttk.Button(frame1, text=u'参照', command=button1_clicked)
    button1.grid(row=0, column=3)

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('ファイル>>')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルパス表示ラベルの作成
    file1 = StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
    file1_entry.grid(row=0, column=2)

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=(0,5))
    frame2.grid(row=1)

    # Startボタンの作成
    button2 = ttk.Button(frame2, text='Start', command=button2_clicked)
    button2.pack(side=LEFT)

    # Cancelボタンの作成
    button3 = ttk.Button(frame2, text='Cancel', command=quit)
    button3.pack(side=LEFT)

    root.mainloop()
