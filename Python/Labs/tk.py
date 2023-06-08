
from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L2 = Label(top, text="Password")

L1.pack( side = LEFT)
E1 = Entry(top, bd =3)
E1.pack(side = RIGHT)
E2 = Entry(top, bd =3)
E2.pack(side = LEFT)
top.mainloop()

