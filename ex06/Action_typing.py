import tkinter as tk
from tkinter import messagebox
import sys
import time
import threading
import tkinter.scrolledtext as tkscr


# class me :                  # 自分自身のクラスを定義する
#     def __init__(self):     #
#         self.HP = 100       # 生命点(HP)
#         self.score = 0      # 得点(スコア)

# class monster :             # モンスターのクラスを定義する

#     def __init__(self):     # モンスタークラスの初期化関数
#         self.name = ""      # 名前
#         self.attack_pt = 0  # 攻撃力
#         self.exp_pt = 0     # 経験値（スコアになる）

#     def set(self, img, name, attack_pt, exp):   # モンスターの情報を設定する関数
#         self.image = img            # 画像を設定する
#         self.name = name            # 名前を設定する
#         self.attack_pt = attack_pt  # 攻撃力を設定する
#         self.exp = exp              # 相手に与える経験値(=スコア)を設定する

#     def attack(self, anyone):       # モンスターが攻撃する関数
#         anyone.HP -= self.attack_pt # だれかの生命点(HP)を減らす


QUESTION = ["experimental building", "school of computer science ", "katayanagi academy", "katayanagi laboratory", "flag",
             "tokyo university of technoogy", "kokaton", "tubakiya", "yoshinoya", "foods foo"]


class Typing(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry("1000x500")
        master.title("こうかとんを倒せ！")

        # 問題インデックス
        self.index = 0

        # 正解数カウント用
        self.correct_cnt = 0

        self.create_widgets()

        # 経過時間スレッドの開始
        t = threading.Thread(target=self.timer)
        t.start()

        # TKインスタンスに対してキーイベント処理を実装
        self.master.bind("<KeyPress>", self.type_event)


    # ウィジェットの生成と配置
    def create_widgets(self):
        self.q_lab = tk.Label(self, text="Question：", font=("",20))
        self.q_lab.grid(row=0, column=0)
        self.q_lab2 = tk.Label(self, text=QUESTION[self.index], width=30, anchor="w", font=("",20))
        self.q_lab2.grid(row=0, column=1)
        self.ans_lab = tk.Label(self, text="Answer：", font=("",20))
        self.ans_lab.grid(row=1, column=0)
        self.ans_lab2 = tk.Label(self, text="", width=30, anchor="w", font=("",20))
        self.ans_lab2.grid(row=1, column=1)
        self.result_lab = tk.Label(self, text="", font=("",20))
        self.result_lab.grid(row=2, column=0, columnspan=2)

        # 時間計測用のラベル
        self.time_lab = tk.Label(self, text="", font=("", 20))
        self.time_lab.grid(row=3, column=0, columnspan=2)

        self.fig2 = True


    # def putText(self,text):
    #     # 次の行にテキストを表示する
    #     self.textbox.insert(str(self.text_r)+'.0', text + '\n')
    #     self.textbox.see('end')             # 最後の行にスクロールさせる
    #     self.text_r += 1   


    # キー入力時のイベント
    def type_event(self, event):
        # 入力値がEntterの場合は答え合わせ
        if event.keysym == "Return":
            if self.q_lab2["text"] == self.ans_lab2["text"]:
                self.result_lab.configure(text="正解！", fg="red")
                self.correct_cnt += 1
            else:
                self.result_lab.config(text="残念！", fg="blue")

            # 解答をクリア
            self.ans_lab2.configure(text="")

            # 次の問題を出題
            self.index += 1
            if self.index == len(QUESTION):
                self.fig = False
                self.q_lab2.configure(text="終了！")
                messagebox.showinfo("結果", f"あなたのスコアは{self.correct_cnt}/{self.index}問正解です。\nクリアタイムは{self.second}秒です。")
                sys.exit(0)
            self.q_lab2.configure(text=QUESTION[self.index])

        elif event.keysym == "BackSpace":
            text = self.ans_lab2["text"]
            self.ans_lab2["text"] = text[:-1]

        elif event.keysym == "space":
            text = self.ans_lab2["text"]
            self.ans_lab2["text"] += " "

        else:
            # 入力値がEnter以外の場合は文字入力としてラベルに追記
            self.ans_lab2["text"] += event.keysym


    def timer(self):
        self.second = 0
        self.fig = True
        while self.fig:
            self.second += 1
            self.time_lab.configure(text=f"経過時間：{self.second}秒")
            time.sleep(1)


class Kokaton(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()


if __name__ == "__main__":
    root = tk.Tk()
    Typing(master=root)
    root.mainloop()