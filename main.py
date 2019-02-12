from tkinter import *
from tkinter import ttk

class currencyConverter(ttk.Frame):
    def __init__(self,parent,**args):
        ttk.Frame.__init__(self,parent, height=args["height"],width=args["width"])

        #control de entrada
        self.inQuantityEntry = ttk.Entry(self, font=("Helvetica",24,"bold"),width=10).place(x=38,y=23)
        self.inCurrencyCombo = ttk.Combobox(self,width=10,height=5).place(x=38,y=71)
        #no se guarda en variable porque solo se pinta
        ttk.Label(self,text="⥮").place(x=102,y=98)
        self.outCurrencyCombo = ttk.Combobox(self, width=10,height=5).place(x=38,y=120)
        self.outQuantityLabel = ttk.Label(self,width=10,font=("Helvetica",24),text="00000").place(x=38,y=166)


#ventana
class mainApp(Tk):

    __currencyConverter = None

    #constructor
    def __init__(self):
        #iniciar padre
        Tk.__init__(self)
        self.title("Convertidor de divisas")
        #dimensiones
        self.geometry("378x229")

        self.__currencyConverter = currencyConverter(self,width=378,height=229).place(x=0,y=0)

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = mainApp()
    app.start()