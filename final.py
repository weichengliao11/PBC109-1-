import tkinter as tk
import random
import tkinter.messagebox

wordlist = ["soccer" , "basketball" , "international" , "buisness"]


def inputWord():
	global word , word_len , guessed , not_yet_choosed , left_word_len , copy_word
	keyword = entry.get()

	if word_len > 0:
		left_chances = 5
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
						answer.configure(text = "你贏了！")
						message = tk.messagebox.askyesno(title = "HangMan" , message = "You won! \n Want to play again?")

						if message == True:
							chooseword()
						else:
							window.destroy()

		else:
			if left_chances > 0:
				left_chances -= 1
				print(left_chances)
				leftchancelabel.configure(text = "Left Chances = {}".format(left_chances))

			elif left_chances == 0:
				gameover = tk.messagebox.showwarning(title = "HangMan" , message = "Game over! \n Want to play again?")
				if gameover == True:
					chooseword()
				else:
					window.destroy()


window = tk.Tk()
window.title("HangMan")
window.geometry("900x450")
window.configure(bg = "gray")


#Labels
introlabel = tk.Label(window, text = "HangMan Game" , font = ("" , 72) , bg = "gray" , fg = "red")
introlabel.place(x = 200 , y = 0)

wordlabel = tk.Label(window, text = "Guess" , font = ("" , 25) , bg = "gray" , fg = "blue")
wordlabel.place(x = 400 , y = 100)

guesslabel = tk.Label(window, text = "" , font = ("" , 25) , bg = "gray" , fg = "blue")
guesslabel.place(x = 375 , y = 150)

leftwordlabel = tk.Label(window, text = "" , font = ("" , 25) , bg = "gray" , fg = "black")
leftwordlabel.place(x = 700 , y = 75)

leftchancelabel = tk.Label(window, text = "Left Chances = 5" , font = ("" , 25) , bg = "gray" , fg = "black")
leftchancelabel.place(x = 700 , y = 150)

answer = tk.Label(window, text = "" , font = ("" , 25) , bg = "gray" , fg = "black")
answer.place(x = 300 , y = 400)

#Entry
entry = tk.StringVar()
inputEntry = tk.Entry(window, font = ("" , 25) , justify = "center" , textvariable = entry)
inputEntry.place(x = 275 , y = 200)

#button
button1 = tk.Button(window, text = "送出" , font = ("" , 25) , bg = "black" , fg = "red" , command = inputWord)
button1.place(x = 420 , y = 300)

#如何選擇題目
def chooseword():
	global word , word_len , guessed , not_yet_choosed , left_word_len , copy_word
	word = random.choice(wordlist)
	print(word)
	not_yet_choosed = ["*" for i in word]
	copy_word = word
	word_len = len(word)
	left_word_len = word_len
	leftwordlabel.configure(text = "Left Words = {}".format(left_word_len))

	guessed = ""
	for i in not_yet_choosed:
		guessed += i + " "

	guesslabel.configure(text = guessed)

chooseword()

window.mainloop()