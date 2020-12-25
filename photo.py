import tkinter as tk

def main():
    root = Tk()
    # 40個字符寬  30行,為了更好的展示圖片
    my_text = Text(root, width=40, height=30)
    my_text.pack(padx=10, pady=10)

    my_photo = PhotoImage(file="/Users/liao/Desktop/hangman_1.png")  # 這裏對圖片的格式也有要求的
    # 第一次我用的是 jpg 編輯器報錯了.

    my_text.image_create(END, image=my_photo)

    mainloop()


if __name__ == '__main__':
    main()