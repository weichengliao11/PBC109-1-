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
