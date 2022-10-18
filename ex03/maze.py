import tkinter as tk

#練習5
def key_down(event):
    global key
    key = event.keysym #練習5

#練習6
def key_up(event):
    global key
    key = event.keysym


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習1
    
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()#練習2

    tori = tk.PhotoImage(file="fig/0.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori") #練習3
    
    #練習4 
    key = ""  #グローバル変数keyは、現在押されているキーを表す変数である

    #練習5,6
    root.bind("KeyPress", key_down)
    root.bind("<KeyRelease", key_up)

    root.mainloop()