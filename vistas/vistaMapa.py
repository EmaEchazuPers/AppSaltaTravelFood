import tkinter as tk
from PIL import Image, ImageTk
import tkintermapview as tkmp
from vistas import vistaDestinos as Vds
from vistas import vistaDetalles as Vdt


class VistaMapa(tk.Frame):
    def __init__(self, master, controlador):
        #Master es: Ventana, donde estará Vista Inicio
        super().__init__(master)
        self.configure(background='#EEEEEE')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        self.lista_destinos = []
        #self.lista_ubicaciones = []
        self.id_item = 0

        self.iniciar_widgets()
    
    #Acciones de botones

    def cambio_destino(self):
        self.controlador.mostrar_frame(Vds.VistaDestinos)

    
    #Posicionamiento de widgets

    def iniciar_widgets(self):
        self.titulo = tk.Label(self,text='Salta Food Travel - Mapa de destinos en Salta'
                        ,justify='center',fg='blue', bg='black',height=10)
        self.titulo.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)        
        self.titulo.configure(height=5)

        self.listbox_destinos = tk.Listbox(self,justify='center')
        self.listbox_destinos.grid(row=1, column=0,columnspan=1, rowspan=2, sticky='nsew', padx=10, pady=10)
        self.listbox_destinos.insert(tk.END,self.lista_destinos)
        self.listbox_destinos.configure(height=20,width=5)

        self.mapa_widget = tkmp.TkinterMapView(self,width=300, height=300,corner_radius=0)
        self.mapa_widget.grid(row=1, column=1, columnspan=3, rowspan=2, sticky='nsew',padx=10, pady=10)
        self.mapa_widget.set_position(-24.789695,-65.411059)
        self.mapa_widget.set_zoom(13)
        #self.mapa_widget.configure(height=20, width=30)
   
        self.btn1 = tk.Button(self, text='Seleccionar', command=self.item_seleccionado)
        self.btn1.grid(row=1, column=3, padx=10, pady=10, sticky='ew')

        self.btn2 = tk.Button(self, text='Volver', command=self.cambio_destino)
        self.btn2.grid(row=2, column=3, padx=10, pady=10,sticky='ew')

        self.actualizar_listbox()
    
    def actualizar_listbox(self):
        destinos = self.controlador.obtener_destinos()
        self.listbox_destinos.delete(0, tk.END)        
        for des in destinos:
            self.listbox_destinos.insert(tk.END,des.nombre)
        
    
    def ubicar_en_mapa(self,id):
        ubicaciones = self.controlador.obtener_ubicaciones()
        destinos = self.controlador.obtener_destinos()
        aux_nombre=''
        aux_id_ubi = 0
        aux_id_des = 0
        match id:
            case 0:
                aux_id_ubi = 1
                aux_id_des = 1001
            case 1:
                aux_id_ubi = 2
                aux_id_des = 1002
            case 2:
                aux_id_ubi = 3
                aux_id_des = 1003
        for des in destinos:
            if des.id_ubicacion == aux_id_ubi:
                aux_nombre = des.nombre
        for ubi in ubicaciones:
            if ubi.id_ubicacion == aux_id_ubi:
                self.mapa_widget.delete_all_marker()                
                imagen = ImageTk.PhotoImage(Image.open('assets\\'+ self.controlador.devolver_ruta_imagen(aux_id_des)).resize((100,100)))
                self.mapa_widget.set_marker(ubi.coordenadas[0],ubi.coordenadas[1],text=aux_nombre,image=imagen)
        
    
    def item_seleccionado(self):
        for i in self.listbox_destinos.curselection():
            self.id_item = i
        self.ubicar_en_mapa(self.id_item)
