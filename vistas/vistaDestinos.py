import tkinter as tk
from vistas import vistaPrincipal as Vp
from vistas import vistaDetalles as Vdt
from vistas import vistaMapa as Vm


class VistaDestinos(tk.Frame):
    def __init__(self, master, controlador):
        #Master es: Ventana, donde estará Vista Inicio
        super().__init__(master)
        self.configure(background='#EEEEEE')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        self.lista_destinos = []

        
        self.iniciar_widgets()
    
    #Acciones de botones

    def cambio_principal(self):
        self.controlador.mostrar_frame(Vp.VistaPrincipal)
    
    def cambio_detalles(self):
        self.controlador.mostrar_frame(Vdt.VistaDetalles)

    def cambio_mapa(self):
        self.controlador.mostrar_frame(Vm.VistaMapa)
    
    #Posicionamiento de widgets

    def iniciar_widgets(self):
        self.titulo = tk.Label(self,text='Salta Food Travel - Lista de destinos en Salta'
                        ,justify='center',fg='blue', bg='black')
        self.titulo.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)        

        self.listbox_destinos = tk.Listbox(self,justify='center')
        self.listbox_destinos.grid(row=1, column=0, columnspan=2, rowspan=3, sticky='nsew', padx=10, pady=10)
        self.listbox_destinos.insert(tk.END,self.lista_destinos)
   
        self.btn1 = tk.Button(self, text='Ver detalles', command=self.cambio_detalles)
        self.btn1.grid(row=1, column=2, padx=10, pady=10, sticky='ew')

        self.btn2 = tk.Button(self, text='Ver mapa', command=self.cambio_mapa)
        self.btn2.grid(row=2, column=2, padx=10, pady=10,sticky='ew')

        self.btn3 = tk.Button(self, text='Volver', command=self.cambio_principal)
        self.btn3.grid(row=3, column=2, padx=10, pady=10,sticky='ew')

        self.actualizar_listbox()
    
    def actualizar_listbox(self):
        destinos = self.controlador.obtener_destinos()
        self.listbox_destinos.delete(0, tk.END)
        for des in destinos:
            self.listbox_destinos.insert(tk.END,des.nombre)


    
