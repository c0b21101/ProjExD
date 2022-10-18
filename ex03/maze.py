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


#練習7,11,12
def main_proc():
    global mx, my
    global cx, cy
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] == 0: #床だったら
        cx, cy = mx*100+50, my*100+50
    else: #壁だったら
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習1
    
    #練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    #練習9
    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst)

    #練習10
    mm.show_maze(canv, maze_lst)

    tori = tk.PhotoImage(file="fig/0.png")
    mx, my = 1, 1 #練習11
    cx, cy = mx*100, my*100 #練習11
    canv.create_image(cx, cy, image=tori, tag="tori") #練習3
    
    #練習4 
    key = ""  #グローバル変数keyは、現在押されているキーを表す変数である

    #練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc()
    
    root.mainloop()