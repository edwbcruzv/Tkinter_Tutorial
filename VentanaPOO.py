"""
    Los Frames son marcos de contenedores de otros widgets.
    Pueden tener tamaño propio y posicionarse en distindos lugares
    de otro contenedor, (ya sea la raiz u otro marco)
    
    
"""

from tkinter import Tk,Label,Frame,Entry,Button

# la clase no es una ventana raiz, es un FRAME
class Application(Frame):
    
    def __init__(self,master,width:int,height:int):
        # Constructor de Frame()
        super().__init__(master,width=width,height=height)
        # empaquetando elementos dentro de su ventana contenedora
        self.pack()
        self.createWidgets()
        
    
    # Aqui se crean todos los widgets del frame
    def createWidgets(self):

        self.lbl1=Label(self,text="Primer numero", bg="blue")
        self.lbl1.place(x=10,y=10,width=100,height=30)

        self.txt1=Entry(self, bg="pink")
        self.txt1.place(x=120,y=10,width=100,height=30)

        self.lbl2=Label(self,text="segundo numero", bg="red")
        self.lbl2.place(x=10,y=50,width=100,height=30)

        self.txt2=Entry(self, bg="pink")
        self.txt2.place(x=120,y=50,width=100,height=30)

        self.lbl3=Label(self,text="Tercer numero", bg="yellow")
        self.lbl3.place(x=10,y=100,width=100,height=30)

        self.txt3=Entry(self, bg="pink")
        self.txt3.place(x=120,y=100,width=100,height=30)

        self.btn1=Button(self,text="sumar",command=self.suma)
        self.btn1.place(x=250,y=50,width=100,height=30)
    
    def suma(self):
        self.txt3.delete(0,'end')
        n1=float(self.txt1.get())
        n2=float(self.txt2.get())
        
        r=n1+n2
        
        self.txt3.insert(0,r)

root=Tk()
root.title("Ejemplo de place")
app=Application(root,500,300)
app.mainloop()