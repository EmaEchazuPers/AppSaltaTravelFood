import tkinter as tk
from vistas import vistaDestinos as Vds


class VistaDetalles(tk.Frame):
    def __init__(self, master, controlador):

        super().__init__(master)
        self.configure(background='#900F0F')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        self.lista_destinos = []
        self.lista_actividades = []
        self.lista_detalles = []
        self.id_item = 0


        self.iniciar_widgets()
    
    def cambio_destino(self):
        self.controlador.mostrar_frame(Vds.VistaDestinos)


    def iniciar_widgets(self):

        #Frame principal

        self.frame_principal = tk.Frame(self,background='#1D1B1B')
        self.frame_principal.pack(side='top',fill='both',expand=True)

        self.titulo = tk.Label(self.frame_principal,text='Detalles de los destinos culinarios',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',18))
        self.titulo.pack(side='top',fill='x', padx=10, pady=10)

        #Frame destinos

        self.frame_destinos = tk.Frame(self.frame_principal,background='#900F0F')
        self.frame_destinos.pack(side='left', fill='both',expand=True, padx=10, pady=10)

        self.lbl_destinos = tk.Label(self.frame_destinos,text='Lista de destinos disponibles',
        background='#1D1B1B',fg='#900F0F',font=('Roboto',13))
        self.lbl_destinos.pack(side='top',fill='x',padx=10,pady=10)

        self.listbox_destinos = tk.Listbox(self.frame_destinos,justify='center',background='#1D1B1B',
        fg='#900F0F', font=('Roboto'))
        self.listbox_destinos.pack(side='top',fill='both',expand=True, padx=10,pady=10)
        self.listbox_destinos.insert(tk.END,self.lista_destinos)

        #Frame detalles

        self.frame_detalles = tk.Frame(self.frame_principal,background='#900F0F')
        self.frame_detalles.pack(side='left', fill='both',expand=True,padx=10,pady=10)

        self.lbl_detalles = tk.Label(self.frame_detalles, text='Detalles del destino',
        background='#1D1B1B',fg='#900F0F',font=('Roboto',13))
        self.lbl_detalles.pack(side='top', fill='x', padx=10,pady=10)

        self.listbox_detalles = tk.Listbox(self.frame_detalles, justify='center',background='#1D1B1B',
        fg='#900F0F', font=('Roboto',10))
        self.listbox_detalles.pack(side='top',fill='both',expand=True,padx=10,pady=10)
        self.listbox_detalles.insert(tk.END,self.lista_detalles)

        #Frame actividades

        self.frame_actividades = tk.Frame(self.frame_principal,background='#900F0F')
        self.frame_actividades.pack(side='left', fill='both',expand=True,padx=10,pady=10)

        self.lbl_actividades = tk.Label(self.frame_actividades, text='Lista de actividades',
        background='#1D1B1B',fg='#900F0F',font=('Roboto',13))
        self.lbl_actividades.pack(side='top', fill='x', padx=10,pady=10)
        
        self.listbox_actividades = tk.Listbox(self.frame_actividades,justify='center',background='#1D1B1B',
        fg='#900F0F', font=('Roboto',10))
        self.listbox_actividades.pack(side='top',fill='both',expand=True, padx=10,pady=10)
        self.listbox_actividades.insert(tk.END,self.lista_actividades)

        #Frame botones

        self.frame_botones = tk.Frame(self.frame_principal, background='#900F0F')
        self.frame_botones.pack(side='left',fill='both',expand=True, padx=10, pady=10)

        self.btn1 = tk.Button(self.frame_botones, text='Seleccionar',command=self.item_seleccionado) 
        self.btn1.pack(side='top',fill='x',padx=10,pady=10) 

        self.btn2 = tk.Button(self.frame_botones, text='Volver',command=self.cambio_destino) 
        self.btn2.pack(side='top',fill='x',padx=10,pady=10) 

        self.actualizar_listbox_destinos()
        
    #Actualiza las listbox

    def actualizar_listbox_destinos(self):
        destinos = self.controlador.obtener_destinos()
        self.listbox_destinos.delete(0, tk.END)
        for des in destinos:
            self.listbox_destinos.insert(tk.END,des.nombre)

    def actualizar_listbox_actividades(self, id):
        actividades = self.controlador.obtener_actividaes()
        self.listbox_actividades.delete(0, tk.END)
        aux_id_dest = 0
        match id:
            case 0:
                aux_id_dest = 1001
            case 1:
                aux_id_dest = 1002
            case 2:
                aux_id_dest = 1003
        
        for act in actividades:
            if act.id_destino == aux_id_dest:
                self.listbox_actividades.insert(tk.END,act.nombre +' - ' + act.hora_inicio + ' hs')
    
    #Obtiene el index del item de la listbox de destinos
    
    def item_seleccionado(self):
        for i in self.listbox_destinos.curselection():
            self.id_item = i
        self.actualizar_txt_detalles(self.id_item)
        self.actualizar_listbox_actividades(self.id_item)
    
    def actualizar_txt_detalles(self, id):
        destinos = self.controlador.obtener_destinos()
        self.listbox_detalles.delete(0,tk.END)
        aux_id_dest = 0
        match id:
            case 0:
                aux_id_dest = 1001
            case 1:
                aux_id_dest = 1002
            case 2:
                aux_id_dest = 1003
        for des in destinos:
            if des.id_destino == aux_id_dest:
                self.listbox_detalles.insert(tk.END,des.nombre)
                self.listbox_detalles.insert(tk.END,'Tipo cocina: ' + des.tipo_cocina)
                self.listbox_detalles.insert(tk.END,'Lista de ingredientes')
                i = 0
                for ing in des.ingredientes:
                    self.listbox_detalles.insert(tk.END,'-'+ ing)
                    i = i+1
                self.listbox_detalles.insert(tk.END,'Precio mínimo: $'+ str(des.precio_min))
                self.listbox_detalles.insert(tk.END,'Precio máximo: $'+ str(des.precio_max))
                self.listbox_detalles.insert(tk.END,'Popularidad: '+ str(des.popularidad))
            


