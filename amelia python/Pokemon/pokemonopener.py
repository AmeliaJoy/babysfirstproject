import pickle
from tkinter import *
tk = Tk()
def q():
    load_file = open('pokemonopener', 'rb')
    pokemonh = pickle.load(load_file)
    load_file.close()
    print(pokemonh)
btnq = Button(tk,text = "Load",command=q)
btnq.pack()
