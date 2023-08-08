import tkinter as tk
from PIL import Image, ImageTk
import tkintermapview as tkmp
from vistas import vistaDestinos as Vds
from vistas import vistaDetalles as Vdt
from vistas import vistaRutaVisita as Vru


class VistaMapa(tk.Frame):
    def __init__(self, master, controlador):
        #Master es: Ventana, donde estará Vista Inicio
        super().__init__(master)
        self.configure(background='#EEEEEE')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        self.lista_destinos = []
        self.lista_rutas = []
        #self.lista_ubicaciones = []
        self.id_item = 0

        self.iniciar_widgets()
    
    #Acciones de botones

    def cambio_destino(self):
        self.controlador.mostrar_frame(Vds.VistaDestinos)
    
    def cambio_visitas(self):
        self.controlador.mostrar_frame(Vru.VistaRutaVisita)

    
    #Posicionamiento de widgets

    def iniciar_widgets(self):

        #Frame principal

        self.frame_principal = tk.Frame(self)
        self.frame_principal.configure(background='yellow')
        self.frame_principal.pack(side='top',fill='both',expand=True)

        self.titulo = tk.Label(self.frame_principal,text='Salta Food Travel - Mapa de destinos en Salta')
        self.titulo.pack(side='top',fill='x', padx=10, pady=10)

        #Frame destinos

        self.frame_destinos = tk.Frame(self.frame_principal)
        self.frame_destinos.pack(side='left', fill='both',expand=True)

        self.lbl_destinos = tk.Label(self.frame_destinos, text='Lista de destinos')
        self.lbl_destinos.pack(side='top', fill='x', padx=10,pady=10)

        self.listbox_destinos = tk.Listbox(self.frame_destinos,justify='center')
        self.listbox_destinos.pack(side='top',fill='both',expand=True, padx=10,pady=10)
        self.listbox_destinos.bind('<Button-1>',self.item_seleccionado)
        self.listbox_destinos.insert(tk.END,self.lista_destinos)

        #Frame rutas

        self.lbl_rutas = tk.Label(self.frame_destinos, text='Lista de rutas')
        self.lbl_rutas.pack(side='top', fill='x', padx=10,pady=10)

        self.listbox_rutas = tk.Listbox(self.frame_destinos,justify='center')
        self.listbox_rutas.pack(side='top',fill='both',expand=True, padx=10,pady=10)
        self.listbox_rutas.bind('<Button-1>',self.item_seleccionado_ruta)
        self.listbox_rutas.insert(tk.END,self.lista_rutas)

        #Frame mapa

        self.frame_mapa = tk.Frame(self.frame_principal)
        self.frame_mapa.pack(side='left', fill='both',expand=True)

        self.lbl_mapa = tk.Label(self.frame_mapa, text='Destino en mapa')
        self.lbl_mapa.pack(side='top', fill='x', padx=10,pady=10)

        self.mapa_widget = tkmp.TkinterMapView(self.frame_mapa)
        self.mapa_widget.pack(side='top',fill='both',expand=True, padx=10, pady=10)
        self.mapa_widget.set_position(-24.789695,-65.411059)
        self.mapa_widget.set_zoom(13)

        #Frame botones

        self.frame_botones = tk.Frame(self.frame_principal, background='black')
        self.frame_botones.pack(side='left',fill='both',expand=True, padx=10, pady=10)

        self.btn_visitas = tk.Button(self.frame_botones, text='Ver rutas', command=self.cambio_visitas)
        self.btn_visitas.pack(side='top',fill='x',padx=10,pady=10)

        self.btn_volver = tk.Button(self.frame_botones, text='Volver', command=self.cambio_destino)
        self.btn_volver.pack(side='top',fill='x',padx=10,pady=10)

        self.actualizar_listbox()
        self.actualizar_rutas()
    
    def actualizar_listbox(self):
        destinos = self.controlador.obtener_destinos()
        self.listbox_destinos.delete(0, tk.END)        
        for des in destinos:
            self.listbox_destinos.insert(tk.END,des.nombre)

    def actualizar_rutas(self):
        rutas_visitas = self.controlador.obtener_rutas_visitas()
        self.listbox_rutas.delete(0, tk.END)        
        for rut in rutas_visitas:
            self.listbox_rutas.insert(tk.END,rut.nombre)
        
    
    def ubicar_en_mapa(self,id):
        self.mapa_widget.delete_all_path()
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
    
    def ubicar_ruta(self,id):
        rutas_visitas = self.controlador.obtener_rutas_visitas()
        aux_id_visita = 0
        aux_num_destinos = 0
        match id:
            case 0:
                aux_id_visita = 1301
                aux_num_destinos = 3
            case 1:
                aux_id_visita = 1302
                aux_num_destinos = 2

        for rut in rutas_visitas:
            if rut.id_visita == aux_id_visita:
                lista_coordenadas = self.controlador.obtener_coordenadas(rut.destinos)
                self.mapa_widget.delete_all_path()
                self.mapa_widget.delete_all_marker()
                self.mapa_widget.set_path(lista_coordenadas)
        self.poner_todos_destinos(aux_id_visita)
    
    def item_seleccionado(self,event):
        for i in self.listbox_destinos.curselection():
            self.id_item = i
        self.ubicar_en_mapa(self.id_item)

    def item_seleccionado_ruta(self,event):
        for i in self.listbox_rutas.curselection():
            self.id_item = i
        self.ubicar_ruta(self.id_item)

    def poner_todos_destinos(self,id_visita):
        self.mapa_widget.delete_all_marker()
        lista = [] 
        if id_visita == 1301:
            lista.append(1001)
            lista.append(1002)
            lista.append(1003)
        if id_visita == 1302:
            lista.append(1001)
            lista.append(1002)
        for id_des in lista:
            for ubi in self.controlador.obtener_ubicaciones():
                if ubi.id_ubicacion == id_des-1000:
                    imagen = ImageTk.PhotoImage(Image.open('assets\\'+ self.controlador.devolver_ruta_imagen(id_des)).resize((100,100)))
                    self.mapa_widget.set_marker(ubi.coordenadas[0],ubi.coordenadas[1],image=imagen)
