
from cgitb import text
from itertools import count
import tkinter as tk
import time
from pygame import event

up = ''

counter = 0
window = tk.Tk()

window.geometry("500x500")



button_up = tk.Button(text= 'up')

counter_label = tk.Label(
    window,
    text= counter
)

button_down = tk.Button(text= 'down')

button_reset = tk.Button(text='reset')

reset_label = tk.Label(text= '')

def up_button(event):
    global counter, counter_label,window, up
    counter = counter + 1
    counter_label.config(text= counter, bg=color(counter))
    up = True
    
    

def down_button(eventt):
    global counter, counter_label,window, color, up
    counter = counter - 1
    counter_label.config(text= counter, bg=color(counter))
    up = False
    
   
def color(counter):
    
    if counter < 0:
        color_choice = "red"
        

    elif counter > 0:
     color_choice = "green"

    else:
        color_choice = "grey"
    return color_choice

def reset():
    global counter, counter_label, reset_label

    if counter > 0 or counter < 0 :
        counter = 0
        counter_label.config(text= counter)
    
    
       




window.config(

 bg = color(counter)   
)

def TempColor(event):
    counter_label.config(bg='yellow')
def TempcolorEnd(event):
    counter_label.config(bg=color(counter))
def DoubleClick(event):
    global  counter, counter_label

    if up:
        counter = counter * 3
        counter_label.config(text= counter)
    else:
        counter = counter / 3
        counter_label.config(text= counter)
  


button_up.config(command= up_button)
button_down.config(command= down_button)
button_reset.config(command= reset)




button_up.pack(
    ipady=25,
    ipadx=100,
    
    
)

counter_label.pack(ipady=25,
    ipadx=100)

button_down.pack(ipady=25,
    ipadx=100,)

button_reset.pack(ipady=25,
    ipadx=100,)

counter_label.bind("<Enter>",TempColor)
counter_label.bind("<Leave>",TempcolorEnd)
counter_label.bind("<Double-Button-1>", DoubleClick)
window.bind('<Up>', up_button)
window.bind('<Down>', down_button)
window.bind('<space>', DoubleClick)


window.mainloop()