from itertools import count
import tkinter as tk

from pygame import event



counter = 0
window = tk.Tk()

window.geometry("500x500")



button_up = tk.Button(text= 'up')

counter_label = tk.Label(
    window,
    text= counter
)

button_down = tk.Button(text= 'down')

def up_button():
    global counter, counter_label,window
    counter = counter + 1
    counter_label.config(text= counter, bg=color(counter))
    
    

def down_button():
    global counter, counter_label,window, color
    counter = counter - 1
    counter_label.config(text= counter, bg=color(counter))
    
   
def color(counter):
    
    if counter < 0:
        color_choice = "red"
        

    elif counter > 0:
     color_choice = "green"

    else:
        color_choice = "grey"
    return color_choice



window.config(

 bg = color(counter)   
)

def TempColor(event):
    counter_label.config(bg='yellow')
def TempcolorEnd(event):
    counter_label.config(bg=color(counter))




button_up.config(command= up_button)
button_down.config(command= down_button)




button_up.pack(
    ipady=25,
    ipadx=100,
    
    
)

counter_label.pack(ipady=25,
    ipadx=100)

button_down.pack(ipady=25,
    ipadx=100,)

counter_label.bind("<Enter>",TempColor)
counter_label.bind("<Leave>",TempcolorEnd)

window.mainloop()