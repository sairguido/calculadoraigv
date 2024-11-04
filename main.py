#Desarrollo por BC-TEC
#version: 0.1 fecha:21/02/2023
#==============================
from tkinter import *
from tkinter import messagebox

def Consumo():
    try:
        montoIGV.set(float(consumo.get())*0.18)
        montoTotal.set(float(consumo.get())+float(montoIGV.get()))
    except:
        messagebox.showinfo("cuidado","Solo Ingresa\nnumero")
def Limpiar():
    consumo.set("")
    montoIGV.set("")
    montoTotal.set("")

def Salir():
    vent.destroy()
vent=Tk()
vent.title("calculo del IGV")
vent.geometry("350x180")#anchoxalto#para, dar el tamaño a la ventana
vent.iconbitmap("iconos/logo.ico")#para cambier el icono de lo que viene a la pantalla predeterminada
vent.config(bg="#0795d6")#para cambiar el color de fondo
vent.resizable(False, False)#sirve para que no se pueda agrandar ni achicar el tamaño de la ventana
#============================= Variables
consumo=StringVar()
montoIGV=StringVar()
montoTotal=StringVar()
#==============================imagenes(Photoimage)
imgEnter=PhotoImage(file="imagenes/enter.png")
imgBorrar=PhotoImage(file="imagenes/borrar.png")
imgCierrar=PhotoImage(file="imagenes/salir.png")
#============================Etiquetas(Label)
lblconsumo=Label(vent, text="Ingrese Consumo: ",bg="#0795d6" )#Esto es para escribir la etiqueta en la ventana
lblconsumo.place(x=15,y=10)#Para pocisionar en que lado va a estar nuestra etiqueta
lblconsumo.config(font=("Helvetica", 13),fg="black")#esto sirve para que poder configurar el grosor de la letra tamaño y color

lbligv=Label(vent, text="Monto IGV   : ", bg="#0795d6")
lbligv.place(x=15, y=40)
lbligv.config(font=("Helvetica", 13),fg="black")

lbltotal=Label(vent, text="Monto total   : ", bg="#0795d6")
lbltotal.place(x=15,y=70)
lbltotal.config(font=("Helvetica", 13),fg="black")
#============================Caja de texto(Entrary)
txtconsumo=Entry(vent,textvariable=consumo,width=17)
txtconsumo.place(x=165,y=10)#Para poder colocar en que pocision va a estas nuestro cuadro de texto
txtconsumo.config(font=("Helvetica", 13), fg="black")#

txtigv=Entry(vent,textvariable=montoIGV,width=17)
txtigv.place(x=150,y=40)
txtigv.config(font=("Helvetica", 13), fg="black")

txttotal=Entry(vent,textvariable=montoTotal,width=17)
txttotal.place(x=150,y=70)
txttotal.config(font=("Helvetica", 13), fg="black")
#==================================botones
btnconsumo=Button(vent,image=imgEnter,width=85,bg="green",height=68)
btnconsumo.place(x=15,y=100)
btnconsumo.config(command=Consumo)

btnigv=Button(vent,image=imgBorrar,width=85,bg="green",height=68)
btnigv.place(x=130,y=100)
btnigv.config(command=Limpiar)

btntotal=Button(vent,image=imgCierrar,width=85,bg="green",height=68)
btntotal.place(x=245,y=100)
btntotal.config(command=Salir)

vent.mainloop()