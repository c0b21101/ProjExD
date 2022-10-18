import tkinter as tk
from turtle import bgcolor

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習1
    
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()#練習2

    tori = tk.PhotoImage(file="fig/0.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori") #練習3

    root.mainloop()