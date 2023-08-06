import tkinter as tk
from vistas import vistaDestinos
from vistas import vistaBusqueda



class VistaPrincipal(tk.Frame):
    def __init__(self, master, controlador):
        #Master es: Ventana, donde estará Vista Inicio
        super().__init__(master)
        self.configure(background='#EEEEEE')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        

        self.iniciar_widgets()

    def cambio_destino(self):
        self.controlador.mostrar_frame(vistaDestinos.VistaDestinos)
    
    def cambio_busqueda(self):
        self.controlador.mostrar_frame(vistaBusqueda.VistaBusqueda)

    def cerrar_ventana(self):
        self.controlador.cerrar_ventana()

    #Posicionamiento de widgets

    def iniciar_widgets(self):
        self.titulo = tk.Label(self,text='Salta Food Travel - Destinos culinarios'
                        ,justify='center',fg='blue', bg='black')
        self.titulo.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)        
   
        self.descripcion = tk.Label(self, text='Esta es la descripcion de la aplicacion', justify='center', bg='red')
        self.descripcion.grid(row=1, column=0, columnspan=2, rowspan=3, sticky='nsew', padx=10, pady=10)

        #Poner command la funcion sin () para que no se inicie cuando se crea el btn
        self.btn1 = tk.Button(self, text='Ver Destinos',command=self.cambio_destino) 
        self.btn1.grid(row=1, column=2, padx=10, pady=10, sticky='ew')

        self.btn2 = tk.Button(self, text='Buscar Destinos',command=self.cambio_busqueda)
        self.btn2.grid(row=2, column=2, padx=10, pady=10,sticky='ew')

        self.btn3 = tk.Button(self, text='Salir', command=self.cerrar_ventana)
        self.btn3.grid(row=3, column=2, padx=10, pady=10,sticky='ew')
    
    