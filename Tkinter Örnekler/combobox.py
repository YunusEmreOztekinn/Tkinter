from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Tkinter ile Arayüz Programlama Dersleri")
window.geometry("500x400")

combo = Combobox(window)
combo['values']=(1,2,3,4,5,"Text")
combo.current(1)
combo.place(x=200,y=170)
window.mainloop()