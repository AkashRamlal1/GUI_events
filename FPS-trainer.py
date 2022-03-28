
from secrets import choice
import tkinter as tk
import time
import random

bind_list = ['<w>','<s>','<r>','<a>','<space>','<Button>','<Double-Button>','<Triple-Button>']
binded =  True


started = False
timer = 20
punten = 0
window = tk.Tk()
window.geometry("1000x1000")

keuze = random.choice(bind_list)
def start():
    global started,timerlabel,timer,opdrachtlabel, puntenlabel
    startknop.destroy()
    started = True
    timerlabel.place(x=950,y=30,)
    puntenlabel.place(x=951,y=50)
    opdrachtlabel.place(x=(random.randrange(1000)),y=(random.randrange(1000)))

    timerlabel.after(1000,timerla)
def timerla():
    global timerlabel,timer,started,punten,opdrachtlabel
    print(timer)
    timer = timer - 1
    timerlabel.config(text=timer)
    if timer > 0:
        timerlabel.after(1000,timerla)
        

    if timer == 0:
        window.destroy()
        print('je tijd is op dit was de score ', punten)

    if timer == 0 and punten == 0:
        print('not so good')


timerlabel =  tk.Label(text=timer)
puntenlabel = tk.Label(text=punten)
opdrachtlabel = tk.Label(text = "klik op {}".format(keuze))

def opdracht(event):
    
    global punten,opdrachtlabel,bind_list,timer,binded,keuze
    punten = punten+ 1
    puntenlabel.config(text=punten)
    opdrachtlabel.place(x=(random.randrange(1000)),y=(random.randrange(1000)))
    window.unbind(keuze)
    keuze = random.choice(bind_list)
    
    opdrachtlabel.config(text="klik op {}".format(keuze))
    window.bind(keuze,opdracht)
    

    

        

startknop = tk.Button(window,bg="grey",text= "start trainer", command=start)




print(keuze)
startknop.place(x=480,y=420)

window.bind(keuze, opdracht)

window.mainloop()