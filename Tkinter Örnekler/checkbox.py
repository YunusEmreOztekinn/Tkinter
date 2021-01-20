from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("tkinter ile Arayüz Programlama Dersleri")
window.geometry("500x400")

chk= BooleanVar()
chk.set(True)
chk = Checkbutton(window, text="Seçilecek", var=chk)
chk.grid(column=1,row=0)
window.mainloop()