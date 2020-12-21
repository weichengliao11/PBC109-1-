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
label = tk.Label(window, text = '玩家一請出題')
label.pack()
player_one_entry = tk.Entry(window)
player_one_entry.pack()
button = tk.Button(window, text = "OK", command = anagram())
button.pack()

# 執行主程式
window.mainloop()


