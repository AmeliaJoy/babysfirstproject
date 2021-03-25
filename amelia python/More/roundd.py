from tkinter import*
tk = Tk()
canvas = Canvas(tk, width=500, height = 500)
canvas.pack()
tk.wm_attributes("-topmost", 1)
canvas.create_oval(x=1, y=1, width=25, height=25, fill='green')
for a in range (0,250):
    canvas.move(1,1,1)
