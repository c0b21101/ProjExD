import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = btn["text"]
    # tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num)


def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

def click_c(event):
    eqn = entry.get()
    entry.delete(len(eqn)-1, tk.END)


def click_ac(event):
    entry.delete(0, tk.END)


root = tk.Tk()
root.geometry("300x600")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right")
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0
numbers = list(range(9, -1, -1))
operators = ["+"]
for i, num in enumerate(numbers+operators, 1):
    btn = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    btn.bind("<1>", click_number)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

btn = tk.Button(root, text=f"=", width=4, height=2, font=("", 30), bg = "light blue")
btn.bind("<1>", click_equal)
btn.grid(row=r, column=c)

btn = tk.Button(root, text="C", width=4, height=2, font=("",30), bg = "light blue")
btn.bind("<1>", click_c)
btn.grid(row=r+1, column=c)

btn = tk.Button(root, text="AC", width=4, height=2, font=("", 30), bg = "light blue")
btn.bind("<1>", click_ac)
btn.grid(row=r+1, column=1)

root.mainloop()        