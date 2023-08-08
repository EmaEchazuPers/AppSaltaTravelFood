import tkinter as tk
from tkinter import PhotoImage
from vistas import vistaDestinos as Vds
from vistas import vistaBusqueda as Vb
from PIL import Image, ImageTk


class VistaPrincipal(tk.Frame):
    def __init__(self, master, controlador):
        #Master es: Ventana, donde estará Vista Inicio
        super().__init__(master)
        self.configure(background='#900F0F')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        

        self.iniciar_widgets()

    def cambio_destino(self):
        self.controlador.mostrar_frame(Vds.VistaDestinos)
    
    def cambio_busqueda(self):
        self.controlador.mostrar_frame(Vb.VistaBusqueda)

    def cerrar_ventana(self):
        self.controlador.cerrar_ventana()

    #Posicionamiento de widgets

    def iniciar_widgets(self):

        #Frame principal
        self.frame_principal = tk.Frame(self)
        self.frame_principal.configure(background='yellow')
        self.frame_principal.pack(side='top',fill='both',expand=True)

        self.titulo = tk.Label(self.frame_principal,text='Salta Food Travel')
        self.titulo.pack(side='top',fill='x', padx=10, pady=10)

        self.descripcion = tk.Label(self.frame_principal, text='Esta es la descripcion de la aplicacion', bg='red', width=60)
        self.descripcion.pack(side='left',fill='both',expand=True, padx=10,pady=10)
        
        #Frame botones

        self.frame_botones = tk.Frame(self.frame_principal, background='black')
        self.frame_botones.pack(side='right',fill='both',expand=True, padx=10, pady=10)
        
        self.btn1 = tk.Button(self.frame_botones, text='Ver Destinos',command=self.cambio_destino, justify='center') 
        self.btn1.pack(side='top',fill='x',padx=10,pady=10) 
        
        self.btn2 = tk.Button(self.frame_botones, text='Buscar Destinos',command=self.cambio_busqueda, justify='center')
        self.btn2.pack(side='top',fill='x',padx=10,pady=10)

        self.btn3 = tk.Button(self.frame_botones, text='Salir', command=self.cerrar_ventana, justify='center')
        self.btn3.pack(side='bottom',fill='x',padx=10,pady=10)
        
    
    