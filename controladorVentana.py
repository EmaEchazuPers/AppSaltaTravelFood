import tkinter as tk
#import de vistas
from vistas import vistaPrincipal as Vp
from vistas import vistaDestinos as Vds
from vistas import vistaBusqueda as Vb
from vistas import vistaDetalles as Vdt
from vistas import vistaMapa as Vm
from vistas import vistaRutaVisita as Vru
from vistas import vistaReview as Vre
#import de modelos
from modelos import modeloDestino as Mds
from modelos import modeloActividad as Mac
from modelos import modeloUbicacion as Mub
from modelos import modeloReview as Mr
from modelos import modeloUsuario as Mu
from modelos import modeloRuta as Mru


class controladorVentana(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Salta Food Travel')
        self.geometry('800x500')
        
        #Se crea un contenedor de las vistas

        container = tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_columnconfigure(0,weight=1)
        container.grid_rowconfigure(0,weight=1)
        container.configure(background='blue')

        self.frames = {}

        #Carga las distintas vistas

        for f in (Vp.VistaPrincipal,Vds.VistaDestinos,Vb.VistaBusqueda,Vdt.VistaDetalles,
                Vm.VistaMapa,Vru.VistaRutaVisita, Vre.VistaReview):
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

    #Devuelve lista de objetos

    def obtener_destinos(self):
        destinos = Mds.ModeloDestino.carga_json('data\destinos.json')
        return destinos
    
    def obtener_actividaes(self):
        actividades = Mac.ModeloActividad.carga_json('data\\actividades.json')
        return actividades
    
    def obtener_ubicaciones(self):
        ubicaciones = Mub.ModeloUbicacion.carga_json('data\\ubicaciones.json')
        return ubicaciones
    
    def devolver_ruta_imagen(self,id_destino):
        destinos = self.obtener_destinos()
        ruta_imagen = ''
        for des in destinos:
            if des.id_destino == id_destino:
                ruta_imagen = des.imagen
        return ruta_imagen
    
    def obtener_reviews(self):
        reviews = Mr.ModeloReview.carga_json('data\\reviews.json')
        return reviews
    
    def obtener_usuarios(self):
        usuarios = Mu.ModeloUsuario.carga_json('data\\usuarios.json')
        return usuarios

    def obtener_rutas_visitas(self):
        rutas_visitas = Mru.ModeloRuta.carga_json('data\\rutasvisitas.json')
        return rutas_visitas

    def obtener_coordenadas(self, id_destinos):
        lista_coordenadas = []
        for id_des in id_destinos:
            destinos = self.obtener_destinos()
            for des in destinos:
                if des.id_destino == id_des:
                    id_ubi = des.id_ubicacion
                    ubicaciones = self.obtener_ubicaciones()
                    for ubi in ubicaciones:
                        if ubi.id_ubicacion == id_ubi:
                            lista_coordenadas.append(ubi.coordenadas)
        return lista_coordenadas
    
    def agregar_review(self,aux_dicc):
        pass
