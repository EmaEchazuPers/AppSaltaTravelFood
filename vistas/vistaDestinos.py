import tkinter as tk
from vistas import vistaPrincipal as Vp
from vistas import vistaDetalles as Vdt
from vistas import vistaMapa as Vm
from vistas import vistaReview as Vre



class VistaDestinos(tk.Frame):
    def __init__(self, master, controlador):
        #Master es: Ventana, donde estará Vista Inicio
        super().__init__(master)
        self.configure(background='#EEEEEE')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        self.lista_destinos = []
        self.lista_reviews = []
        self.id_item = 0

        
        self.iniciar_widgets()
    
    #Acciones de botones

    def cambio_principal(self):
        self.controlador.mostrar_frame(Vp.VistaPrincipal)
    
    def cambio_detalles(self):
        self.controlador.mostrar_frame(Vdt.VistaDetalles)
        
    def cambio_mapa(self):
        self.controlador.mostrar_frame(Vm.VistaMapa)
    
    def cambio_review(self):
        self.controlador.mostrar_frame(Vre.VistaReview)
    
    #Posicionamiento de widgets

    def iniciar_widgets(self):

        #Frame principal

        self.frame_principal = tk.Frame(self)
        self.frame_principal.configure(background='yellow')
        self.frame_principal.pack(side='top',fill='both',expand=True)

        self.titulo = tk.Label(self.frame_principal,text='Salta Food Travel - Destinos culinarios en Salta')
        self.titulo.pack(side='top',fill='x', padx=10, pady=10)
        
        #Frame de destinos

        self.frame_destinos = tk.Frame(self.frame_principal)
        self.frame_destinos.pack(side='left', fill='both',expand=True, padx=10, pady=10)

        self.lbl_destinos = tk.Label(self.frame_destinos,text='Lista de destinos disponibles')
        self.lbl_destinos.pack(side='top',fill='x',padx=10,pady=10)

        self.listbox_destinos = tk.Listbox(self.frame_destinos,justify='center')
        self.listbox_destinos.pack(side='top',fill='both',expand=True, padx=10,pady=10)
        self.listbox_destinos.insert(tk.END,self.lista_destinos)

        #Frame de botones

        self.frame_botones = tk.Frame(self.frame_principal, background='black')
        self.frame_botones.pack(side='left',fill='both',expand=True, padx=10, pady=10)

        self.btn_detalles = tk.Button(self.frame_botones, text='Ver detalles', command=self.cambio_detalles)
        self.btn_detalles.pack(side='top',fill='x',padx=10,pady=10) 

        self.btn_mapas = tk.Button(self.frame_botones, text='Ver mapas', command=self.cambio_mapa)
        self.btn_mapas.pack(side='top',fill='x',padx=10,pady=10) 

        self.btn_review = tk.Button(self.frame_botones, text='Ver review', command=self.item_seleccionado)
        self.btn_review.pack(side='top',fill='x',padx=10,pady=10)

        self.btn_carga = tk.Button(self.frame_botones, text='Agregar review', command=self.cambio_review)
        self.btn_carga.pack(side='top',fill='x',padx=10,pady=10)

        self.btn_volver = tk.Button(self.frame_botones, text='Volver', command=self.cambio_principal)
        self.btn_volver.pack(side='top',fill='x',padx=10,pady=10) 

        #Muestra reviews  

        self.lbl_reviews = tk.Label(self.frame_botones, text='Mira los reviews')
        self.lbl_reviews.pack(side='top',fill='x', padx=10, pady=10)

        self.listbox_reviews = tk.Listbox(self.frame_botones, justify='left')
        self.listbox_reviews.pack(side='top',fill='both', expand=True, padx=10, pady=10)
        self.listbox_reviews.insert(tk.END,self.lista_reviews)

        self.actualizar_listbox()
    
    def actualizar_listbox(self):
        destinos = self.controlador.obtener_destinos()
        self.listbox_destinos.delete(0, tk.END)
        for des in destinos:
            self.listbox_destinos.insert(tk.END,des.nombre)
    
    def cargar_reviews(self,id):
        reviews = self.controlador.obtener_reviews()
        usuarios = self.controlador.obtener_usuarios()
        self.listbox_reviews.delete(0, tk.END)
        aux_id_dest = 0
        aux_id_usu = 0
        match id:
            case 0:
                aux_id_dest = 1001
            case 1:
                aux_id_dest = 1002
            case 2:
                aux_id_dest = 1003
        for rev in reviews:
            if rev.id_destino == aux_id_dest:
                self.listbox_reviews.insert(tk.END,'Comentario: ')
                self.listbox_reviews.insert(tk.END,'-'+ rev.comentario)
                self.listbox_reviews.insert(tk.END,'Calificación: '+ str(rev.calificacion))
                self.listbox_reviews.insert(tk.END,'Animo: ' + rev.animo)
                for usu in usuarios:
                    if usu.id_usuario == rev.id_usuario:
                        self.listbox_reviews.insert(tk.END,'Usuario: ' + usu.nombre + ' ' + usu.apellido)
                        self.listbox_reviews.insert(tk.END,'-----------------')

    def item_seleccionado(self):
        for i in self.listbox_destinos.curselection():
            self.id_item = i
        self.cargar_reviews(self.id_item)
        

