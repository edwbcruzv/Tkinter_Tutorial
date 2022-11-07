"""
    Posisicionamiento relativo
    En ligar de especificar coordenadas, solo decimos
    arriba, abajo, derecha o izquierda respecto a otro contenedor
    
    si no indicamos ningun argumento, por defecto tkinter posicionara
    los elementos uno arriba del otro

"""
from tkinter import *

# root1=Tk()
# root1.geometry("200x100")
# entry1=Entry(root1)
# entry1.pack()

# button1=Button(root1,text="boton1")
# button1.pack()

# label1=Label(root1,text="un label1")
# label1.pack()

# root1.mainloop()

"""
    la propiedad que controla la posicion relativa es 
    side
    puede equivaler a 
    
    tk.BUTTOM,tk.TOP(por defecto),tk.LEFT o tk.RIGTH
    (revisar doc)
    de este modo indicamos que la caja de texto debe ir ubicada a la iquierda, 
    los otros controles se mantendran uno arriba de otro

"""
# root2=Tk()
# root2.geometry("200x100")
# entry2=Entry(root2)
# entry2.pack(side="left")

# button2=Button(root2,text="boton1")
# button2.pack()

# label2=Label(root2,text="un label1")
# label2.pack()

# root2.mainloop()


"""
    admite parametros
    
    after y before
    que permiten controlar el orden en que se ubican los elementos en una ventana
"""

root3=Tk()
root3.geometry("200x100")
entry3=Entry(root3)
entry3.pack()

button3=Button(root3,text="boton1")
button3.pack()

# aparecera antes de entry3
label3=Label(root3,text="un label1")
label3.pack(before=entry3)

root3.mainloop()