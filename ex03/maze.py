import tkinter as tk
import maze_maker as mm #練習8

#練習5
def key_down(event):
    global key
    key = event.keysym #練習5


#練習6
def key_up(event):
    global key
    key = ""  #どのキーも押されていないことを意味する


#練習7
def main_proc():
    global cx, cy, key
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


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
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc()

    #練習9
    maze_lst = mm.make_maze(15, 9)
    #print(maze_lst)
    mm.show_maze(canv, maze_lst)


    root.mainloop()