from tkinter import *

def num(numero):
    numero = numero['text']
    if numero == 'X':
        conta.append('*')
        conta_lb['text'] = conta
    elif numero == '÷':
        conta.append('/')
        conta_lb['text'] = conta
    else:
        conta.append(numero)
        conta_lb['text'] = conta

#Pega os valores da lista e faz os cálculos
def calcular():
    global conta
    try:
        conta_lb['text'] = eval(str("".join(conta)))
        conta = []
    except:
        conta_lb['text'] = 'E R R O'
        conta = []

#Limpa a conta
def limp():
    global conta
    conta_lb['text'] = ' '
    conta = []

tela = Tk()
tela.title('Calculadora')
tela.geometry('350x500')
tela.resizable(True, False)
conta = []


conta_lb = Label(tela, text = '', font=12)
conta_lb.pack(side = TOP, anchor=E)

n1 = Button (tela, text='1', border=4, width=8, height= 4, command= lambda : num(n1))
n1.place(x = 10, y = 100)

n2 = Button (tela, text = '2', border=4,  width= 8, height=4, command= lambda : num(n2))
n2.place(x = 90, y = 100)

n3 = Button (tela, text= '3', border=4,  width= 8 , height= 4, command= lambda : num(n3))
n3.place(x = 170, y = 100)

n4 = Button (tela, text= '4', border=4,  width= 8, height=4, command= lambda : num(n4))
n4.place(x=10, y= 180)

n5 = Button (tela, text= '5', border=4,  width= 8, height=4, command= lambda : num(n5))
n5.place(x=90, y=180)

n6 = Button (tela, text = '6', border=4,  width = 8, height = 4, command = lambda : num(n6))
n6.place(x = 170, y = 180)

n7 = Button (tela, text = '7', border=4,  width = 8, height = 4, command = lambda : num(n7))
n7.place(x = 10, y = 260)

n8 = Button (tela, text = '8', border=4,  width = 8, height = 4, command = lambda : num(n8))
n8.place(x = 90, y = 260)

n9 = Button (tela, text = '9', border=4,  width = 8, height = 4, command = lambda : num(n9))
n9.place(x = 170, y = 260)

n0 = Button (tela, text = '0', border=4,  width = 8, height = 4, command = lambda : num(n0))
n0.place(x = 10, y = 340)

ponto = Button(tela, text='.', border=4,  width=8, height=4, command= lambda : num(ponto))
ponto.place(x=170, y=340)

result = Button (tela, text='=', border=4,  width=20, height=4, fg = 'white', bg='grey', command= calcular)
result.place(x = 170, y=420)

limpar = Button (tela, text = 'C', border=4,  width = 8, height = 4, fg = "white", bg = "teal", command = limp)
limpar.place(x = 90, y = 340)

soma = Button(tela, text = '+', border=4,  width = 8, height = 4, command = lambda : num(soma))
soma.place(x = 260, y = 100)

sub = Button(tela, text = '-', border=4,  width = 8, height = 4, command = lambda : num(sub))
sub.place(x = 260, y = 180)

mult = Button(tela, text = 'X', border=4,  width = 8, height = 4, command = lambda : num(mult))
mult.place(x = 260, y = 260)

div = Button(tela, text = '÷', border=4,  width = 8, height = 4, command = lambda : num(div))
div.place(x = 260, y = 340)

p1 = Button(tela, text = '(', border=4,  width = 8, height = 4, command = lambda : num(p1))
p1.place(x = 10, y = 420)

p2 = Button(tela, text = ')', border=4,  width = 8, height = 4, command = lambda : num(p2))
p2.place(x = 90, y = 420)



mainloop()