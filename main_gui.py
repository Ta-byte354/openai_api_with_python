import tkinter as tk
from file_controll import FileControll

class MainGui:
    

    #ウィンドウの表示を設定する。
    def __init__(self):
        #tkinterのインスタンスを作成
        self.window = tk.Tk()
        self.window.resizable(True, True)

        #送受信のテキストエリアを作成
        self.text_sen = tk.Text(self.window)
        self.text_rec = tk.Text(self.window)

        #インスタンスを作成
        self.text_controll = FileControll()

        #ラベルを作成
        self.label = tk.Label(self.window, text="teach me EMA")
    
        #受信のテキストエリアの設定
        answer = ""
        self.text_rec.insert(tk.END, answer)
        self.text_rec.config(state=tk.DISABLED)


        #送信ボタン押下後の処理
        def send_text():
            question = self.text_sen.get("1.0", tk.END)
            answer = self.text_controll.api_send_text(question)
            self.text_rec.config(state=tk.NORMAL)
            self.text_rec.insert(tk.END, answer)
            self.text_rec.config(state=tk.DISABLED)

        #送信のボタンを作成
        self.button_sen = tk.Button(self.window, text="送信", command=send_text)


        #保存ボタン押下後の処理
        def save_text():
            pass

        #保存のボタンを作成
        self.button_save = tk.Button(self.window, text="保存", command=save_text)

        #ウィジェットを配置
        self.label.pack()
        self.text_sen.pack()
        self.text_rec.pack()
        self.button_sen.pack(anchor=tk.SE, padx=10, pady=10)
        self.button_save.pack(anchor=tk.SE, padx=10, pady=10)

        #ウィンドウが閉じないようにする。
        self.window.mainloop()

if __name__ == '__main__':
    MainGui()
