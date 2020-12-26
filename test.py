import tkinter as tk
import random
import tkinter.messagebox
import p_new as file
from PIL import Image, ImageTk

left_chances = 5
wrong_words_list = []

def inputWord():
	global word , word_len , guessed , not_yet_choosed , left_word_len , copy_word , left_chances , wrong_words_list
	keyword = entry.get()
	if keyword in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		keyword = file.alphabet_change(keyword)

	inputEntry.delete(0 , "end")
	wrong_word = ""

	if word_len > 0:
		if (keyword in word):
			for i in range(word_len):
				if word[i] == keyword and not_yet_choosed[i] == "*":
					not_yet_choosed.pop(i)
					not_yet_choosed.insert(i, keyword)
					ans = "".join(not_yet_choosed)
					#guessed.replace(guessed[i] , keyword)
					guesslabel.configure(text = not_yet_choosed)
					#print(left_word_len)

					if ans == word:
						message = tk.messagebox.askyesno(title = "HangMan" , message = "You won!\nThe answer is" + "\n" + word + "\nWant to play again?")

						if message == True:
							left_chances = 5
							chooseword()
							leftchancelabel.configure(text = "Left Chances = 5")
						else:
							window.destroy()


		elif len(keyword) > 1:
			warning = tk.messagebox.showwarning(title = "HangMan" , message = "只能輸入一個字母！")

		elif keyword not in "abcdefghijklmnopqrstuvwxyz":
			warning = tk.messagebox.showwarning(title = "HangMan" , message = "你輸入的不是英文喔！\n請輸入英文字母！")

		else:
			if left_chances > 0:
				left_chances -= 1
				if wrong_word not in wrong_words_list:
					wrong_word += (keyword + "、")

				wrong_words_list.append(keyword)
				wrongwordlabel.configure(text = "猜錯的字：" + wrong_word)
				leftchancelabel.configure(text = "Left Chances = {}".format(left_chances))
				"""

		else:
			if left_chances > 0:
				left_chances -= 1

				if left_chances == 4:
					img = Image.open('2 .jpg')
					img = img.resize((400, 300), Image.ANTIALIAS)
					img = ImageTk.PhotoImage(img)
					imLabel = tk.Label(window, image=img)
					imLabel.place(x=450, y=100)
					print(left_chances)
					leftchancelabel.configure(text = "Left Chances = {}".format(left_chances))

				if left_chances == 3:
					img = Image.open('3 .jpg')
					img = img.resize((400, 300), Image.ANTIALIAS)
					img = ImageTk.PhotoImage(img)
					imLabel = tk.Label(window, image=img)
					imLabel.place(x=450, y=100)
					leftchancelabel.configure(text = "Left Chances = {}".format(left_chances))

				if left_chances == 2:
					img = Image.open('5 .jpg')
					img = img.resize((400, 300), Image.ANTIALIAS)
					img = ImageTk.PhotoImage(img)
					imLabel = tk.Label(window, image=img)
					imLabel.place(x=450, y=100)
					leftchancelabel.configure(text = "Left Chances = {}".format(left_chances))

				if left_chances == 1:
					img = Image.open('6 .jpg')
					img = img.resize((400, 300), Image.ANTIALIAS)
					img = ImageTk.PhotoImage(img)
					imLabel = tk.Label(window, image=img)
					imLabel.place(x=450, y=100)
					leftchancelabel.configure(text = "Left Chances = {}".format(left_chances))
				"""

				if left_chances == 0:
					gameover = tk.messagebox.askyesno(title = "HangMan" , message = "Game over!\nThe answer is" + "\n" + word + "\nWant to play again?")

					if gameover == True:
						left_chances = 5
						chooseword()
						leftchancelabel.configure(text = "Left Chances = 5")
					else:
						window.destroy()


def call_inputWord(event):
	inputWord()

#def wrong_word():



window = tk.Tk()
window.title("HangMan")
window.geometry("900x480")
window.configure(bg = "gray")
#Labels
introlabel = tk.Label(window, text = "HangMan Game" , font = ("" , 72) , bg = "gray" , fg = "black")
introlabel.place(x = 200 , y = 0)

wordlabel = tk.Label(window, text = "Guess" , font = ("" , 25) , bg = "gray" , fg = "blue")
wordlabel.place(x = 50 , y = 100)

guesslabel = tk.Label(window, text = "" , font = ("" , 25) , bg = "gray" , fg = "blue")
guesslabel.place(x = 50 , y = 150)

rulelabel = tk.Label(window, text = "遊戲規則：簡單來說，就是猜英文單字遊戲！\n如果你猜不到單字，牙籤人就會被吊死><\n請在空白格內輸入「一個英文字母」\n「＊」符號代表英文單字的長度，有幾個「＊」就有幾個字母\n若該字母有出現在單字中，按下送出後字母會出現在正確的位置上\n若該字母不在單字中，代表你猜錯了\n牙籤人會逐漸邁向死亡!\n你有五次猜錯字母的機會，加油！\n（注意：一次只能輸入一個英文字母" , font = ("" , 14) , bg = "yellow" , fg = "black")
rulelabel.place(x = 450 , y = 100)
"""
img = Image.open('1 .jpg')
img = img.resize((400, 300), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
imLabel = tk.Label(window, image=img)
imLabel.place(x=450, y=100)
"""

leftchancelabel = tk.Label(window, text = "Left Chances = 5" , font = ("" , 25) , bg = "gray" , fg = "black")
leftchancelabel.place(x = 450 , y = 412)

wrongwordlabel = tk.Label(window, text = "猜錯的字：" , font = ("" , 20) , bg = "yellow" , fg = "black")
wrongwordlabel.place(x = 50 , y = 270)


#Entry
entry = tk.StringVar()
inputEntry = tk.Entry(window, font = ("" , 25) , justify = "center" , textvariable = entry)
inputEntry.place(x = 50 , y = 200)

#button
button1 = tk.Button(window, text = "送出" , font = ("" , 25) , bg = "black" , fg = "red" , command = inputWord)
button1.place(x = 50 , y = 300)
window.bind("<Return>" , call_inputWord)



#如何選擇題目
def chooseword():
	global word , word_len , guessed , not_yet_choosed , copy_word , left_chances
	word = random.choice(file.dictionary())
	print(word)
	not_yet_choosed = ["*" for i in word]
	copy_word = word
	word_len = len(word)
	left_word_len = word_len

	guessed = ""
	for i in not_yet_choosed:
		guessed += i + " "

	guesslabel.configure(text = guessed)
	inputEntry.delete(0 , "end")

chooseword()

window.mainloop()
