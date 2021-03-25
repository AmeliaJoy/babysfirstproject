from tkinter import*
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
tk.wm_attributes("-topmost", 1)
mytriangle = canvas.create_oval(1, 1, 25, 25, fill="green")
def oval_left():
    canvas.move(1, -3, 0)
def oval_right():
    canvas.move(1, 3, 0)
def oval_down():
    canvas.move(1, 0, 3)
def oval_up():
    canvas.move(1, 3, 0)
canvas.bind_all('<KeyPress-Left>', oval_left)
canvas.bind_all('<KeyPress-Right>', oval_right)
canvas.bind_all('<KeyPress-Up>', oval_up)
canvas.bind_all('<KeyPress-Down>', oval_down)
    


ab = True
while ab == True:
    canvas.create_oval(1,1,1,1, outline="white", fill= "white")
    canvas.move(2,0,1)
