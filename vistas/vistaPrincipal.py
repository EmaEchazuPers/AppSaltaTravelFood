import tkinter as tk
from tkinter import PhotoImage
from vistas import vistaDestinos as Vds
from vistas import vistaBusqueda as Vb
from PIL import Image, ImageTk


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
        self.controlador.mostrar_frame(Vds.VistaDestinos)
    
    def cambio_busqueda(self):
        self.controlador.mostrar_frame(Vb.VistaBusqueda)

    def cerrar_ventana(self):
        self.controlador.cerrar_ventana()

    #Posicionamiento de widgets

    def iniciar_widgets(self):

        #imagen = ImageTk.PhotoImage(Image.open('assets\\'+ self.controlador.devolver_ruta_imagen(aux_id_des)).resize((100,100)))
        #imagen = ImageTk.PhotoImage(Image.open('assets\\salta_bandera.jpg'))
        #text='Salta Food Travel - Destinos culinarios'
        #self.imagen = PhotoImage(file='assets\\salta_bandera2.png')
        self.img_bg = PhotoImage(file='assets\\monumento_guemes2.png') 
        self.titulo = tk.Label(self,image=self.img_bg)
        self.titulo.grid(row=0, columnspan=3, rowspan=1, sticky='ew', padx=10, pady=10)
        #self.titulo.configure(height=1)
   
        self.descripcion = tk.Label(self, text='Esta es la descripcion de la aplicacion', justify='center', bg='red')
        self.descripcion.grid(row=1, column=0, columnspan=2, rowspan=3, sticky='nsew', padx=10, pady=10)
        self.descripcion.configure(height=20)


        #Poner command la funcion sin () para que no se inicie cuando se crea el btn
        self.btn1 = tk.Button(self, text='Ver Destinos',command=self.cambio_destino, justify='center') 
        self.btn1.grid(row=1, column=2, padx=10, pady=10, sticky='ew')
        self.btn1.configure(height=2)

        self.btn2 = tk.Button(self, text='Buscar Destinos',command=self.cambio_busqueda, justify='center')
        self.btn2.grid(row=2, column=2, padx=10, pady=10,sticky='ew')
        self.btn2.configure(height=2)

        self.btn3 = tk.Button(self, text='Salir', command=self.cerrar_ventana, justify='center')
        self.btn3.grid(row=3, column=2, padx=10, pady=10,sticky='ew')
        self.btn3.configure(height=2)
    
    