from tkinter import *
from tkinter.ttk import *
from time import strftime#string format time
window=Tk()#creates window
window.geometry("400x400")#the measureemnts of the window
window.title("digital clock and calendar :)")
window.config(background="dark orange")

def timecalc():
    timeformat=strftime("%H:%M:%S")#formats the clock as per the formatting codes
    label.configure(text=timeformat)#puts the time in the label
    label.after(1000,timecalc)#update the clock after 1000 milli seconds
    caleformat=strftime("%d/%m/%Y")
    cale.configure(text=caleformat)
    label.after(1000,timecalc)

label=Label(window,font=("Arial",17))
label.place(x=150,y=150)
cale=Label(window,font=("Arial",17))
cale.place(x=150,y=200)
timecalc()

window.mainloop()
