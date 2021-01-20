from tkinter import *
window = Tk()
frm = Frame(master=window,width=500,height=500)
frm.pack()

label1 = Label(master=frm, text="0'a 0 noktasındayım",bg="red",fg="white")
label1.place(x=0, y=0)

label2 = Label(master=frm, text="250'ye 250 noktasındayım",bg="purple",fg="white")
label2.place(x=250,y=250)
window.mainloop()