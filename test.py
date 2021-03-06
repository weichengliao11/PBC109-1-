import tkinter as tk
import random
import tkinter.messagebox
import p_new as file  # 單字以及大小寫切換function
import string
from PIL import Image, ImageTk
import tkinter.font as tkFont

left_chances = 5  # 總共五次機會
wrong_words_list = []  # 猜錯的字
guessed_words_list = []  # 猜對過的字
wrong_word = ""
time = 120  # 以秒為單位


# 倒數計時器
def countdown():
    global time , left_chances , wrong_words_list , wrong_word , guessed_words_list , wrong_words_list
    time -= 1
    if time >= 0:
        timelabel.configure(text = str(time) + "sec")
        #每一秒處發一次countdown function
        window.after(1000, countdown)

    if time == 0:
        gameover = tk.messagebox.askyesno(title = "HangMan" , message = "遊戲結束！\n你沒有時間了！\n答案是" + "\n" + word + "\n想再試一次嗎？")

        if gameover == True:
            left_chances = 5
            time = 120
            guessed_words_list = []
            wrong_words_list = []
            wrong_word = ""
            chooseword()

            img = Image.open('1 .jpg')
            img = img.resize((560, 350), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            imLabel = tk.Label(window, image=img)
            imLabel.place(x=25, y=150)
            imLabel.image = img

            wrongwordlabel.configure(text = "猜錯的字：")
            leftchancelabel.configure(text = "剩餘次數 = 5")
        else:
            window.destroy()


# 主要的function
def inputWord():
    global left_chances, wrong_words_list, wrong_word, time, guessed_words_list, wrong_words_list
    # 取得輸入的東西
    keyword = entry.get()
    # 如果輸入的是一個大寫的英文字母
    if keyword in string.ascii_uppercase:  # A~Z
        # 轉成小寫的
        keyword = file.alphabet_change(keyword)

    # 清除輸入框
    inputEntry.delete(0, "end")

    # 如果輸入的字母為謎底的其中一個且還沒猜過這個字母的話
    if (keyword in word) and keyword not in guessed_words_list and len(keyword) == 1:
        for i in range(word_len):
            if word[i] == keyword and not_yet_choosed[i] == "*":
                # 將＊換成keyword
                not_yet_choosed.pop(i)
                not_yet_choosed.insert(i, keyword)
                ans = "".join(not_yet_choosed)
                guesslabel.configure(text=not_yet_choosed)
                # 將這次猜的字母放進猜對過的字清單中
                guessed_words_list.append(keyword)

                # 如果全部猜到
                if ans == word:
                    message = tk.messagebox.askyesno(title="HangMan",
                                                     message="你贏了！\n答案是" + "\n" + word + "\n想再玩一次嗎？")
                    img = Image.open('7 .jpg')
                    img = img.resize((560, 350), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    imLabel = tk.Label(window, image=img)
                    imLabel.place(x=25, y=150)
                    imLabel.image = img

                    # 如果要再玩一次的話
                    if message == True:
                        # 重置剩餘機會
                        left_chances = 5
                        time = 120
                        guessed_words_list = []
                        wrong_words_list = []
                        chooseword()
                        wrong_word = ""
                        wrongwordlabel.configure(text="猜錯的字：")
                        leftchancelabel.configure(text="剩餘次數 = 5")

                        img = Image.open('1 .jpg')
                        img = img.resize((560, 350), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        imLabel = tk.Label(window, image=img)
                        imLabel.place(x=25, y=150)
                        imLabel.image = img

                    else:
                        # 將程式關閉
                        window.destroy()

    # 如果輸入的字母已經猜對過了
    elif (keyword in word) and keyword in guessed_words_list:
        warning = tk.messagebox.showwarning(title="HangMan", message="你已經猜過了！")

    # 如果輸入的字母多於一個
    elif len(keyword) > 1:
        warning = tk.messagebox.showwarning(title="HangMan", message="只能輸入一個字母！")

    # 如果輸入的不是英文字母
    elif keyword not in string.ascii_lowercase:
        warning = tk.messagebox.showwarning(title="HangMan", message="你輸入的不是英文喔！\n請輸入英文字母！")

    # 如果格式正確但是猜錯的話
    else:

        if left_chances > 0:
            if keyword in wrong_words_list:
                warning = tk.messagebox.showwarning(title="HangMan", message="你已經錯過了！\n試試看別的字母～")

            # 列出猜錯過的字
            else:
                wrong_word += (keyword + "、")

                # 將猜錯的字加入錯字清單
                wrong_words_list.append(keyword)
                left_chances -= 1

                wrongwordlabel.configure(text="猜錯的字：" + wrong_word)
                leftchancelabel.configure(text="Left Chances = {}".format(left_chances))

            if left_chances == 4:
                img = Image.open('2 .jpg')
                img = img.resize((560, 350), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                imLabel = tk.Label(window, image=img)
                imLabel.place(x=25, y=150)
                imLabel.image = img
                leftchancelabel.configure(text = "剩餘次數 = {}".format(left_chances))
            if left_chances == 3:
                img = Image.open('3 .jpg')
                img = img.resize((560, 350), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                imLabel = tk.Label(window, image=img)
                imLabel.place(x=25, y=150)
                imLabel.image = img
                leftchancelabel.configure(text = "剩餘次數 = {}".format(left_chances))
            if left_chances == 2:
                img = Image.open('4 .jpg')
                img = img.resize((560, 350), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                imLabel = tk.Label(window, image=img)
                imLabel.place(x=25, y=150)
                imLabel.image = img
                leftchancelabel.configure(text = "剩餘次數 = {}".format(left_chances))
            if left_chances == 1:
                img = Image.open('5 .jpg')
                img = img.resize((560, 350), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                imLabel = tk.Label(window, image=img)
                imLabel.place(x=25, y=150)
                imLabel.image = img
                leftchancelabel.configure(text = "剩餘次數 = {}".format(left_chances))

            if left_chances == 0:

                img = Image.open('6 .jpg')
                img = img.resize((560, 350), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                imLabel = tk.Label(window, image=img)
                imLabel.place(x=25, y=150)
                imLabel.image = img


                # leftchancelabel.configure(text = "Left Chances = {}".format(left_chances))

                gameover = tk.messagebox.askyesno(title="HangMan",
                                                  message="遊戲結束！\n答案是" + "\n" + word + "\n想再試一次嗎？")

                # 如果選擇再玩一次
                if gameover == True:
                    # 重置剩餘機會
                    left_chances = 5
                    time = 120
                    wrong_word = ""
                    guessed_words_list = []
                    wrong_words_list = []
                    # 選擇單字
                    chooseword()

                    img = Image.open('1 .jpg')
                    img = img.resize((560, 350), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    imLabel = tk.Label(window, image=img)
                    imLabel.place(x=25, y=150)
                    imLabel.image = img

                    wrongwordlabel.configure(text="猜錯的字：")
                    leftchancelabel.configure(text="剩餘次數 = 5")
                else:
                    window.destroy()


# 按enter也可以輸入的function
def call_inputWord(event):
    inputWord()


window = tk.Tk()
window.title("HangMan")
window.geometry("1010x530")
window.configure(bg="LightGrey")

img = Image.open('bg.jpg')
img = img.resize((1000, 520), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
imLabel = tk.Label(window, image=img)
imLabel.place(x=0, y=0)
imLabel.image = img

# Labels
# 標題
# introlabel = tk.Label(window, text="- HangMan Game -", font=("", 44), bg="LightGrey", fg="black")
# introlabel.place(x=300, y=15)

wordlabel = tk.Label(window, text="Guess", font=("Courier", 25), bg="#f0ceb6", fg="Black")
wordlabel.place(x=625, y=230)

# 謎底
guesslabel = tk.Label(window, text="", font=("", 25), bg="#f0ceb6", fg="Black")
guesslabel.place(x=625, y=263)

# 遊戲規則
# rulelabel = tk.Label(window,
#                      text="遊戲規則：\n\n簡單來說，就是猜英文單字遊戲！\n如果你猜不到單字或是沒有在時間內猜完，牙籤人就會被吊死\n\n請在空白格內輸入「一個英文字母」，\n「＊」符號代表英文單字的長度，有幾個「＊」就有幾個字母。\n若該字母有出現在單字中，按下送出後字母會出現在正確的位置上；\n若該字母不在單字中，代表你猜錯了，牙籤人會逐漸邁向死亡！\n\n你有五次猜錯字母的機會以及120秒的時間，趕快猜猜看吧，加油！\n（注意：一次只能輸入一個英文字母）",
#                      font=("", 16), bg="LightGrey", fg="black", justify="left")
# rulelabel.place(x=50, y=135)

# 剩餘機會
leftchancelabel = tk.Label(window, text="Left Chances = 5", font=("Courier", 20), bg="#def6f3", fg="black")
leftchancelabel.place(x=620, y=415)

# 錯字
wrongwordlabel = tk.Label(window, text="猜錯的字：", font=("Courier", 20), bg="#def6f3", fg="black")
wrongwordlabel.place(x=620, y=450)

# 倒數計時器
timelabel = tk.Label(window, text="10sec", font=("Courier", 30), bg="#80011f", fg="white")
timelabel.place(x=620, y=160)

# Entry
entry = tk.StringVar()
inputEntry = tk.Entry(window, font=("Courier", 25), justify="center", textvariable=entry, bg="#dbccf8", width=10)
inputEntry.place(x=625, y=335)

# button
# 送出輸入的東西的按鈕
button1 = tk.Button(window, text="送出", font=("Microsoft YaHei", 25, tkFont.BOLD), bg="#bde3fb", fg="#ab4d5d", command=inputWord)
button1.place(x=830, y=335)
# 按enter鍵也能輸入的function
window.bind("<Return>", call_inputWord)


# 如何選擇題目
def chooseword():
    global word, word_len, guessed, not_yet_choosed, left_chances
    # 從單字海中選一個單字
    word = random.choice(file.dictionary())
    print(word)
    # 把選到的字用成＊字號
    not_yet_choosed = ["*" for i in word]
    word_len = len(word)

    # 把一堆米字號轉成字串
    guessed = ""
    for i in not_yet_choosed:
        guessed += i + " "

    guesslabel.configure(text=guessed)
    inputEntry.delete(0, "end")


# 遊戲開始前的介紹詞
start = tk.messagebox.askyesno(title="HangMan", message="歡迎來到 HangMan Game!\n準備好了嗎？")
if start == True:
    countdown()
    chooseword()
    img = Image.open('1 .jpg')
    img = img.resize((560, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    imLabel = tk.Label(window, image=img)
    imLabel.place(x=25, y=150)
    imLabel.image = img

else:
    window.destroy()

window.mainloop()
