#import libraries
from tkinter import *
import random

rot = Tk()
rot.geometry("190x300")
rot["background"] = "#18222b"
rot.title("Generator")
gerador = Label(rot, text="Password generator",font="arial", fg="white", bg="#18222b").place(x=23, y=38)

#Create function for buttom action
def go():
    contents = "abcdefghijklmnopqrstuvwxyz123456789@&#?\/ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw_length = 8
    output = ""
    for i in range(pw_length):
        next_index = random.randrange(len(contents))
        output = output + contents[next_index]
    pas = Label(rot, text=output, width='12', font=('arial', 14)).place(x=28,y=148)
    #print(output) # Se quiser aparecer no Terminal
dev = Label(rot, text='GitHub -> OseiasMzM', font=('arial', 8),fg='white', bg='#18222b').place(x=41,y=282)

bt = Button(width=6, text="Go", command=go)
bt.place(x=68, y=96)




#Finish





rot.mainloop()
