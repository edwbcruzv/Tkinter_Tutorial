"""
    posicionamiento de controles en una ventana
    modo de colocar widgets en una ventana
    -place
    -pack
    -grid
    
    no debemos mezclar los distintos metodos
    
      
"""

"""
    self.button.place(x=60,y=40,width=100,height=30)
    x,y posicion respecto al elemento padre
    width y height tamaño del widget
    VALORES ABSOLUTOS, no cambian   
    
    medidas con respecto al padre contenedor
    self.button.place(relx=0.1,rely=0.1,relwidth=0.5,relheight=0.5)  
    
    VALORES RELATIVOS AL PADRE CONTENEDOR, valores entre 0 y 1 
"""

from tkinter import *

root=Tk()

def suma():
    txt3.delete(0,'end')
    n1=float(txt1.get())
    n2=float(txt2.get())
    
    r=n1+n2
    
    txt3.insert(0,r)

root.title("Ejemplo de place")
root.geometry("600x300")

lbl1=Label(root,text="Primer numero", bg="blue")
lbl1.place(relx=0.1,rely=0.2,relwidth=0.2,relheight=0.1)

txt1=Entry(root, bg="pink")
txt1.place(relx=0.4,rely=0.2,relwidth=0.2,relheight=0.1)

lbl2=Label(root,text="segundo numero", bg="red")
lbl2.place(relx=0.1,rely=0.4,relwidth=0.2,relheight=0.1)

txt2=Entry(root, bg="pink")
txt2.place(relx=0.4,rely=0.4,relwidth=0.2,relheight=0.1)

lbl3=Label(root,text="Tercer numero", bg="yellow")
lbl3.place(relx=0.1,rely=0.6,relwidth=0.2,relheight=0.1)

txt3=Entry(root, bg="pink")
txt3.place(relx=0.4,rely=0.6,relwidth=0.2,relheight=0.1)

btn1=Button(root,text="sumar",command=suma)
btn1.place(relx=0.7,rely=0.4,relwidth=0.2,relheight=0.1)


root.mainloop()