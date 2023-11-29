from tkinter import*
from time import*

def update():
    afficher_heure = strftime("%I:%M:%S %p")
    time_label.config(text=afficher_heure)
    
    time_label.after(1000,update)

window = Tk()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

update()


window.mainloop()