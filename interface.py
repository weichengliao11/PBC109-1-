#TO 廖：目前第2到第151行是遊戲進行的部份，我把可能要呈現在螢幕上的東西，在程式碼裡面用print表示，包含draw、talk result、miss、hint，我猜你是要改寫＠陳 寫的182行到188行的code BY鄧
def game(answer):

    #這部分是遊戲進行中，要印出來的東西
    draw = ""
    talk = "" #這是關於遊戲過程的描述
    result = "" #這是目前猜題的情形
    miss = "" #這是目前猜錯的英文字母
    hint = "" #這是必要的時候，跳出來的提示(尚未設計)

    #輸入我們要猜的答案
    ans_len = str(len(answer))

    #這一部分是儲存的地方    
    in_answer = []
    for letter in answer:
        in_answer.append(letter) #in_answer 儲存正確的字
    correct_letters = [] #correct_letters 儲存猜過且正確的字
    missed_letter = [] #missed_letter 放猜過但錯誤的字
    wrong_time = len(missed_letter) #wrong_time 是猜錯的次數

    
    talk = "單字長度共" + ans_len + "個字!" + "你總共有6次猜題機會，GOGO！"
    #正式開始玩遊戲
    while wrong_time < 6: #當錯誤的次數小於6，就可以進行遊戲
        if wrong_time == 0:
            talk = "請猜猜一個字母吧！"
            print(talk)

        #開始猜字母了
        guess = input()

        #這部分避免玩家猜亂打一些東西，而給出相對應的回饋        
        alp = "abcdefghijklmnopqrstuvwxyz" 
        if guess not in alp: #如果他猜的不是英文
            talk = "這不是英文字母喔，猜個英文字母吧！"
            print(talk)

        elif guess in missed_letter: #如果他猜的是猜過且猜錯的
            talk = str(guess) + "已經猜錯喔！再思考一下吧"
            print(talk)
        
        elif guess in correct_letters: #如果他猜過且猜對
            talk = str(guess) + "已經猜過摟！換一個英文字母吧"
            print(talk)


        else: #如過他猜的是可以猜的字母，遊戲可以繼續        
            
            # 以下是把猜的東西放進資料庫裡
            if guess in in_answer:
                correct_letters.append(guess)
            else:
                missed_letter.append(guess)
                
            # 用 miss 呈現猜錯的狀況
            miss_add = ""
        
            for i in range(len(missed_letter)):
                if i != len(missed_letter) - 1:
                    miss_add += missed_letter[i] + "、"
                else:
                    miss_add += missed_letter[i]
            miss = "目前猜錯的字母有：" + miss_add
    


            # 用 result 呈現目前猜題的狀況
            now_answer = []
            for i in range(len(in_answer)):
                if in_answer[i] in correct_letters:
                    now_answer.append(in_answer[i])
                else:
                    now_answer.append("_")

            result = ""
            for letter in now_answer:
                result += letter

            #如果猜錯了，印出吊人圖案和錯誤的單字
            if len(missed_letter) == 0:

                draw = "吊人圖案零號"
                miss = "厲害喔,目前沒有猜錯的字!"
                print(draw)
                print(miss)
                print(talk)
                print(result)

            if len(missed_letter) == 1:
                draw = "吊人圖案ㄧ號"
                talk = "你還有5次猜錯的機會"
                print(draw)
                print(miss)
                print(talk)
                print(result)

            elif len(missed_letter) == 2:
                draw = "吊人圖案二號"
                talk = "你還有4次猜錯的機會"
                print(draw)
                print(miss)
                print(talk)
                print(result)

            elif len(missed_letter) == 3:
                draw = "吊人圖案三號"
                talk = "你還有3次猜錯的機會"
                print(draw)
                print(miss)
                print(talk)
                print(result)

            elif len(missed_letter) == 4:
                draw ="吊人圖案四號"
                talk = "你還有2次猜錯的機會"
                print(draw)
                print(miss)
                print(talk)
                print(result)

            elif len(missed_letter) == 5:
                draw ="吊人圖案五號"
                talk = "你還有1次猜錯的機會"
                print(draw)
                print(miss)
                print(talk)
                print(result)

            elif len(missed_letter) == 6:
                draw = "吊人圖案六號"
                talk = "遊戲結束！其實答案是" + str(answer) + "!"
                print(draw)
                print(miss)
                print(talk)
                print(result)
                break

            # 如果答對了，就恭喜他
            if result == answer:
                draw = "吊人圖案成功"
                talk = "太強了吧，你竟然猜對了!答案就是:" + str(answer) + "!"
                print(draw)
                print(miss)
                print(talk)
                print(result)

    return talk
    return result
    return miss
    return hint

# 引入 tkinter 模組
import tkinter as tk

def anagram():
    # 取得輸入文字
    print("輸入完畢！")
    answer = format(player_one_entry.get())
    return answer

# 建立主視窗 Frame
window = tk.Tk()

# 設定視窗標題
window.title('Hang Man')

# 設定視窗大小為 900x450，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("900x450+250+150")

# 設定玩家一的輸入位置
# 一行字顯示：玩家一請出題
label_entry = tk.Label(window, text='玩家一請出題')
label_entry.pack()
# 玩家一請輸入：
player_one_entry = tk.Entry(window)
player_one_entry.pack()
# 輸入完成按ok的按鈕
button_entry = tk.Button(window, text="OK", command=anagram())
button_entry.pack()

# 這段要放吊死人那段 code
game(answer)
# 結果是 result

# 結果是猜對了還是被吊死了
result = True

# 結束遊戲
if result == True:
    label_close = tk.Label(window, text='你猜對了！')
else:
    label_close = tk.Label(window, text='你死了！')
label_close.pack()

button_play_again = tk.Button(window, text="Play Again", command=anagram())
button_close = tk.Button(window, text="Leave")
button_play_again.pack()
button_close.pack()
# 執行主程式
window.mainloop()
