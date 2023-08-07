import tkinter as tk
from vistas import vistaDestinos as Vds


class VistaDetalles(tk.Frame):
    def __init__(self, master, controlador):

        super().__init__(master)
        self.configure(background='#EEEEEE')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        self.lista_destinos = []
        self.lista_actividades = []
        self.id_item = 0


        self.iniciar_widgets()
    
    def cambio_destino(self):
        self.controlador.mostrar_frame(Vds.VistaDestinos)


    def iniciar_widgets(self):
        self.titulo = tk.Label(self,text='Detalles de los destinos - Actividades'
                        ,justify='center',fg='blue', bg='black')
        self.titulo.grid(row=0, column=0, columnspan=5, sticky='nsew', padx=10, pady=10)    

        self.listbox_destinos = tk.Listbox(self,justify='center')
        self.listbox_destinos.grid(row=1, column=0, columnspan=1, rowspan=3, sticky='nsew', padx=10, pady=10)
        self.listbox_destinos.insert(tk.END,self.lista_destinos)    

        self.listbox_actividades = tk.Listbox(self,justify='center')
        self.listbox_actividades.grid(row=1, column=2, columnspan=2, rowspan=3, sticky='nsew', padx=10, pady=10)
        self.listbox_actividades.insert(tk.END,self.lista_actividades) 

        #Poner command la funcion sin () para que no se inicie cuando se crea el btn
        self.btn1 = tk.Button(self, text='Seleccionar',command=self.item_seleccionado) 
        self.btn1.grid(row=1, column=4, padx=10, pady=10, sticky='ew')

        self.btn2 = tk.Button(self, text='Volver',command=self.cambio_destino) 
        self.btn2.grid(row=2, column=4, padx=10, pady=10, sticky='ew')

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
                self.listbox_actividades.insert(tk.END,act.nombre +' - ' + act.hora_inicio)
    
    #Obtiene el index del item de la listbox de destinos
    
    def item_seleccionado(self):
        for i in self.listbox_destinos.curselection():
            self.id_item = i
        self.actualizar_listbox_actividades(self.id_item)
