import tkinter as tk
import random
import tkinter.messagebox
import p_new as file
from PIL import Image, ImageTk

left_chances = 5

def inputWord():
	global word , word_len , guessed , not_yet_choosed , left_word_len , copy_word , left_chances
	keyword = entry.get()
	inputEntry.delete(0 , "end")

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

img = Image.open('1 .jpg')
img = img.resize((400, 300), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
imLabel = tk.Label(window, image=img)
imLabel.place(x=450, y=100)

# leftwordlabel = tk.Label(window, text = "" , font = ("" , 25) , bg = "gray" , fg = "black")
# leftwordlabel.place(x = 500 , y = 75)

leftchancelabel = tk.Label(window, text = "Left Chances = 5" , font = ("" , 25) , bg = "gray" , fg = "black")
leftchancelabel.place(x = 450 , y = 412)


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
	global word , word_len , guessed , not_yet_choosed , left_word_len , copy_word
	word = random.choice(file.dictionary())
	print(word)
	not_yet_choosed = ["*" for i in word]
	copy_word = word
	word_len = len(word)
	left_word_len = word_len
	#leftwordlabel.configure(text = "Left Words = {}".format(left_word_len))

	guessed = ""
	for i in not_yet_choosed:
		guessed += i + " "

	guesslabel.configure(text = guessed)
	inputEntry.delete(0 , "end")

chooseword()

window.mainloop()
