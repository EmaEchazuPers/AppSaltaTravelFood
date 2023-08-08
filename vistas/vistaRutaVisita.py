import tkinter as tk
from PIL import Image, ImageTk
import tkintermapview as tkmp
from vistas import vistaDestinos as Vds
from vistas import vistaDetalles as Vdt
from vistas import vistaMapa as Vm


class VistaRutaVisita(tk.Frame):
    def __init__(self, master, controlador):
        #Master es: Ventana, donde estará Vista Inicio
        super().__init__(master)
        self.configure(background='#EEEEEE')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        self.lista_rutas = []
        #self.lista_ubicaciones = []
        self.id_item = 0

        self.iniciar_widgets()
    
    #Acciones de botones

    def cambio_destino(self):
        self.controlador.mostrar_frame(Vm.VistaMapa)

    
    #Posicionamiento de widgets

    def iniciar_widgets(self):

        #Frame principal

        self.frame_principal = tk.Frame(self)
        self.frame_principal.configure(background='yellow')
        self.frame_principal.pack(side='top',fill='both',expand=True)

        self.titulo = tk.Label(self.frame_principal,text='Salta Food Travel - Rutas de visitas')
        self.titulo.pack(side='top',fill='x', padx=10, pady=10)

        #Frame rutas

        self.frame_rutas = tk.Frame(self.frame_principal)
        self.frame_rutas.pack(side='left', fill='both',expand=True)

        self.lbl_rutas = tk.Label(self.frame_rutas, text='Lista de rutas')
        self.lbl_rutas.pack(side='top', fill='x', padx=10,pady=10)

        self.listbox_rutas = tk.Listbox(self.frame_rutas,justify='center')
        self.listbox_rutas.pack(side='top',fill='both',expand=True, padx=10,pady=10)
        self.listbox_rutas.bind('<Button-1>',self.item_seleccionado)
        self.listbox_rutas.insert(tk.END,self.lista_rutas)

        #Frame mapa

        self.frame_mapa = tk.Frame(self.frame_principal)
        self.frame_mapa.pack(side='left', fill='both',expand=True)

        self.lbl_mapa = tk.Label(self.frame_mapa, text='Destino en mapa')
        self.lbl_mapa.pack(side='top', fill='x', padx=10,pady=10)

        self.mapa_widget = tkmp.TkinterMapView(self.frame_mapa)#,width=300, height=300,corner_radius=0)
        self.mapa_widget.pack(side='top',fill='both',expand=True, padx=10, pady=10)
        self.mapa_widget.set_position(-24.789695,-65.411059)
        self.mapa_widget.set_zoom(13)
        self.mapa_widget.add_left_click_map_command(self.left_click_event)

        #Frame botones

        self.frame_botones = tk.Frame(self.frame_principal, background='black')
        self.frame_botones.pack(side='left',fill='both',expand=True, padx=10, pady=10)

        self.btn_volver = tk.Button(self.frame_botones, text='Volver', command=self.cambio_destino)
        self.btn_volver.pack(side='top',fill='x',padx=10,pady=10)

        self.actualizar_listbox()
    
    def actualizar_listbox(self):
        rutas_visitas = self.controlador.obtener_rutas_visitas()
        self.listbox_rutas.delete(0, tk.END)        
        for rut in rutas_visitas:
            self.listbox_rutas.insert(tk.END,rut.nombre)
        
    
    def ubicar_en_mapa(self,id):
        rutas_visitas = self.controlador.obtener_rutas_visitas()
        aux_id_visita = 0
        match id:
            case 0:
                aux_id_visita = 1301
            case 1:
                aux_id_visita = 1302

        for rut in rutas_visitas:
            if rut.id_visita == aux_id_visita:
                lista_coordenadas = self.controlador.obtener_coordenadas(rut.destinos)
                #self.mapa_widget.delete_all_marker()
                self.mapa_widget.delete_all_path()
                self.mapa_widget.delete_all_marker()
                self.mapa_widget.set_path(lista_coordenadas)
                self.poner_marcadores(lista_coordenadas)
                #for coord in lista_coordenadas:             
                    #imagen = ImageTk.PhotoImage(Image.open('assets\\'+ self.controlador.devolver_ruta_imagen(id)).resize((100,100)))
                    #marcador = self.mapa_widget.set_marker(ubi.coordenadas[0],ubi.coordenadas[1],text=aux_nombre,image=imagen)
                 #   self.mapa_widget.set_path(lista_coordenadas)
        
    
    def item_seleccionado(self,event):
        for i in self.listbox_rutas.curselection():
            self.id_item = i
        #for i in self.listbox_destinos.curselection():
        #    self.id_item = i
        self.ubicar_en_mapa(self.id_item)
    
    def poner_marcadores(self, lista_coordenadas):
        for coord in lista_coordenadas:
            self.mapa_widget.set_marker(coord[0],coord[1])

    def left_click_event(coordenadas):
        
        pass

        