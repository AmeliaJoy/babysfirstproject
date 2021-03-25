import pickle
import time
from random import *
from tkinter import *
caughtt=["caught","missed"]
backpack=["Bulbasaur", "Charmander"]
ballcaught=["Poke Ball", "Poke Ball"]
for i in range(0,10):
    for i in range(0,10):
       time.sleep(0.5) 
    balls=["Great Ball","Master Ball","Poke Ball","Ultra Ball"]
    things=["Solgaleo", "Lunala", "Cosmog", "Charizard", "Charmeleon","Charmander","Venusaur","Ivysaur", "Bulbasaur", "Blastoise","Wartortle", "Squirtle","Grimer","Muk","Machamp","Machop", "Machoke"]
    found=choice(things)
    ball=choice(balls)
    caught=choice(caughtt)
    print('You found a wild %s' % found)
    print('You %s it with a %s' % (caught,ball))
    if caught=='caught' :
        backpack.append(found)
        ballcaught.append(ball)
for x in range(0,len(backpack)):
    print('%s was caught by an %s' % (backpack[x], ballcaught[x]))
pq=[backpack, ballcaught]
tk = Tk()
def q():
    save_file = open('pokemonopener','wb')
    pickle.dump(pq, save_file)
btnq = Button(tk,text = "Save",command=q)
btnq.pack()
