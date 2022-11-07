"""
    manejo de grilla
    grid
    
    como se maneja la cuadricula en CSS y sus filas y columnas como una matrix
    
    
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
root.geometry("500x300")

lbl1=Label(root,text="Primer numero sssssss", bg="blue")
lbl1.grid(row=0,column=0,padx=10,pady=10,sticky="w")

txt1=Entry(root, bg="pink")
txt1.grid(row=0,column=1,padx=10,pady=10)

lbl2=Label(root,text="segundo numero", bg="red")
lbl2.grid(row=1,column=0,padx=10,pady=10,sticky="w")

txt2=Entry(root, bg="pink")
txt2.grid(row=1,column=1,padx=10,pady=10)

lbl3=Label(root,text="Tercer num", bg="yellow")
lbl3.grid(row=2,column=0,padx=10,pady=10,sticky="w")

txt3=Entry(root, bg="pink")
txt3.grid(row=2,column=1,padx=10,pady=10)

btn1=Button(root,text="sumar",command=suma)
btn1.grid(row=1,column=2,padx=10,pady=10)


root.mainloop()