from tkinter import *
window = Tk()
window.title("Tkinter ile Arayüz Programlama Dersleri")
window.geometry("500x500")
lbl = Label(window, text="Merhaba, Python",font=("Arial Bold",20))
lbl.grid(column=0,row=0)
txt = Entry(window,width=10)
txt.grid(column=1,row=0)

def clicked():
    x = "Hoş Geldiniz "+ txt.get()+" Bey"
    lbl.configure(text=x)

btn = Button(window,text="Tıkla",bg="Purple",fg="white",width=15,height=5,command=clicked)
btn.grid(column=2,row=0)

window.mainloop()