from tkinter import *
import tkinter as tk
import pyqrcode


root = Tk()
root.geometry("190x300")
root["background"] = "#38005F"

root.title("QrCode Gerador") # Titulo

def exit_bt():
    exit()

def gerar_qr():
    qr=pyqrcode.create(qrger.get())#Recebe a descrição
    qr.png(titleqr.get() + '.png', scale=7)#Recebe o Título
    obs = Label(root, text="Qr gerado... \nprocure na pasta do arquivo.",bg="#38115A", fg="yellow")
    obs.place(x=17,y=229)
    bt_exit = Button(root, text="Exit", font="Bahnschrift 8", bg="red", fg="white", command=exit_bt)
    bt_exit.place(x=161,y=277)

btt = Button(text="GERAR",
                    command=gerar_qr)
btt.place(x=70,y=197)

qr = Label(root, text="Gerador de QrCode", font="Aspirin 11", width=17, fg="white", bg="#38005F")
qr.place(x=17, y=9)

qrTITLE = Label(root, text="Título do Qr", bg="#38005F", fg="yellow")
qrTITLE.place(x=61,y=53)
titleqr = Entry(root)#escolher nome para Titulo
titleqr.place(x=35, y=79)

qrTITLE = Label(root, text="Descrição", bg="#38005F", fg="yellow")
qrTITLE.place(x=69,y=111)
qrger = Entry(root)#escolher nome para Descrição
qrger.place(x=35,y=139)









root.mainloop()
