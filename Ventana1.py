
from tkinter import Button, Label, Tk


def mensaje():
    print("Presionando el boton")

# permite crear la ventana principal
ventana=Tk()
ventana.geometry("1000x500")
ventana.title("Ventana1")

lbl=Label(ventana,text="Estese un label")

# ubica los widgets en una posicion que podemos cambiar a traves de los correspondientes atributos
lbl.pack()


btn=Button(ventana,text="preiona el boton",command=mensaje)
btn.pack()

# inicia el bucle de mensajes
# aqui se monitorea la interaccion del usuario por medio del raton y teclado con la app
ventana.mainloop()