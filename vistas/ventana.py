import tkinter as tk
#Trae la carpera y luego el modulo
from vistas import vistaPrincipal
from vistas import vistaDestinos
from vistas import vistaBusqueda
from vistas import vistaDetalles
from vistas import vistaMapa
from vistas import vistaReviews


#Contiene los metodos para gestionar todas las pantallas

class Ventana(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title('Salta Travel Food')
        self.geometry('600x400')

        #Trabaja como el contenedor del resto de pantallas
        contendor = tk.Frame(self)
        contendor.pack(side='top', fill='both', expand=True)

        #Acomoda el frame si se expande o contrae la ventana
        contendor.columnconfigure(0,weight=1)
        contendor.rowconfigure(0,weight=1)
        contendor.configure(background='#EEEEEE')

        self.frames = {}
         
        #Recorre las distintas vistas - Desde el modulo de cada vista trae la clase
        for f in (vistaPrincipal.VistaPrincipal, vistaDestinos.VistaDestinos, vistaBusqueda.VistaBusqueda
        ,vistaDetalles.VistaDetalles, vistaMapa.VistaMapa, vistaReviews.VistaReviews):
            frame = f(contendor,self) #Se le pasa el contenedor y el controlador a la vista seleccionada
            self.frames[f] = frame #Se guarda la vista seleccionada
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.mostrar_frame(vistaPrincipal.VistaPrincipal) #Primera vista que aparece
        
    def mostrar_frame(self, contenedor):
        frame = self.frames[contenedor]
        frame.tkraise() #Coloca la vista seleccionada delante del resto

