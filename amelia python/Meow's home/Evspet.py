import turtle
meow = turtle.Pen()
meow.color(0,1,0)
meow.clear()
meow.up()
from tkinter import *
tk = Tk()
def q():
    for y in range(0,5):
        meow.left(180)
btnq = Button(tk,text = "Spin",command=q)
btnq.pack()
def b():
    for c in range(0,5):
        meow.forward(50)
        meow.left(180)
        meow.forward(50)
btna = Button(tk,text = "Pace",command=b)
btna.pack()
def r():
   meow.reset()
   meow.clear()
   meow.color(0,1,0)
btnb = Button(tk,text = "Erase",command=r)
btnb.pack()
def spin1():
    meow.reset()
    for x in range(1,38):
        meow.forward(100)
        meow.left(175)
btnspin1 = Button(tk,text = "Spin 1",command=spin1)
btnspin1.pack()
def car():
    meow.reset()
    meow.color(1,0,0)
    meow.begin_fill()
    meow.forward(100)
    meow.left(90)
    meow.forward(20)
    meow.left(90)
    meow.forward(20)
    meow.right(90)
    meow.forward(20)
    meow.left(90)
    meow.forward(60)
    meow.left(90)
    meow.forward(20)
    meow.right(90)
    meow.forward(20)
    meow.left(90)
    meow.forward(20)
    meow.end_fill()
    meow.color(0,0,0)
    meow.up()
    meow.forward(10)
    meow.down()
    meow.begin_fill()
    meow.circle(10)
    meow.end_fill()
    meow.setheading(0)
    meow.up()
    meow.forward(90)
    meow.right(90)
    meow.forward(10)
    meow.setheading(0)
    meow.begin_fill()
    meow.down()
    meow.circle(10)
    meow.end_fill()
btncar = Button(tk, text = "Car",command=car)
btncar.pack()
def snowflake():
    meow.right(180)
    meow.forward(70)
    meow.right(180)
    meow.forward(140)
    meow.right(180)
    meow.forward(70)
    meow.right(60)
    meow.forward(70)
    meow.right(180)
    meow.forward(140)
    meow.right(180)
    meow.forward(70)
    meow.right(60)
    meow.forward(70)
    meow.right(180)
    meow.forward(140)
btnsnow = Button(tk, text = "Snowflake", command=snowflake)
btnsnow.pack()
def yarn():
    meow.begin_fill()
    meow.circle(10)
    meow.end_fill()
    meow.forward(50)
btnyarn = Button(tk, text = "Yarn", command=yarn)
btnyarn.pack()
