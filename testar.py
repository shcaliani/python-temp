## propriedade rowspan e columnspan 
## mesclar colunas e linhas

from tkinter import *

janela = Tk()

## definindo os elementos
lb1 = Label(janela, width=15, height=5, bg="red")
lb2 = Label(janela, width=15, height=5, bg="blue")
lb3 = Label(janela, width=15, height=5, bg="black")
lb4 = Label(janela, width=15, height=5, bg="yellow")
lb5 = Label(janela, height=3, bg="green")
lb6 = Label(janela, width=5, bg="pink")

#2 posicionando3
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
lb3.grid(row=0, column=1)
lb4.grid(row=1, column=1)
lb5.grid(row=2, column=0, columnspan=2, sticky=W+E)     # ocupar toda área de oeste a leste
lb6.grid(row=0, column=2, rowspan=2, sticky=N+S)

janela.geometry("500x300+500+200")
janela.mainloop()