import tkinter as tk
#import de vistas
from vistas import vistaPrincipal as Vp
from vistas import vistaDestinos as Vds
from vistas import vistaBusqueda as Vb
from vistas import vistaDetalles as Vdt
from vistas import vistaMapa as Vm
from vistas import vistaReviews as Vr
#import de modelos
from modelos import modeloDestino as Mds
from modelos import modeloActividad as Mac


class controladorVentana(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Salta Travel Food')
        self.geometry('600x400')

        #Es un contenedor de las vistas
        container = tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_columnconfigure(0,weight=1)
        container.grid_rowconfigure(0,weight=1)
        container.configure(background='blue')

        self.frames = {}

        #Carga las distintas vistas
        for f in (Vp.VistaPrincipal,Vds.VistaDestinos,Vb.VistaBusqueda,Vdt.VistaDetalles,
                Vm.VistaMapa,Vr.VistaReviews):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.mostrar_frame(Vp.VistaPrincipal)
        
    
    #Muestra la vista que tenga el container
    def mostrar_frame(self, container):
        frame = self. frames[container]
        frame.tkraise()

    def cerrar_ventana(self):
        self.destroy()

    def obtener_destinos(self):
        destinos = Mds.ModeloDestino.carga_json('data\destinos.json')
        return destinos
    
    def obtener_actividaes(self):
        actividades = Mac.ModeloActividad.carga_json('data\\actividades.json')
        return actividades

    #def seleccionar_item(self, event):
    #    indice = Vdt.VistaDetalles.listbox_destinos.curselection()