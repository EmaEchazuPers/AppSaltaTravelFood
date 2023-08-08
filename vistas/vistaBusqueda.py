import tkinter as tk
from tkinter import ttk
from vistas import vistaDestinos as Vd


class VistaBusqueda(tk.Frame):
    def __init__(self, master, controlador):
       #Master es: Ventana, donde estará Vista Inicio
       super().__init__(master)
       self.configure(background='#900F0F')
       self.rowconfigure(0,weight=1)
       self.columnconfigure(0,weight=1)
       self.controlador = controlador
       self.lista_buscar = []
       self.lista_filtrar = []
       self.precio_min = tk.DoubleVar()
       self.precio_max = tk.DoubleVar()
       self.lista_tipos_cocina = []
       self.destinos = self.controlador.obtener_destinos()
       
       self.iniciar_widgets()
    
    def cambio_principal(self):
        self.controlador.mostrar_frame(Vd.VistaDestinos)
    
    def iniciar_widgets(self):
        
        #Frame principal

        self.frame_principal = tk.Frame(self)
        self.frame_principal.configure(background='#1D1B1B')
        self.frame_principal.pack(side='top',fill='both',expand=True)

        self.titulo = tk.Label(self.frame_principal,text='Busqueda de destinos',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',18))
        self.titulo.pack(side='top',fill='x', padx=10, pady=10)

        #Frame contenedores

        self.frame_busqueda = tk.Frame(self.frame_principal,background='#900F0F')
        self.frame_busqueda.pack(side='left',fill='both',expand=True,padx= 10, pady=10)

        self.frame_filtrar = tk.Frame(self.frame_principal,background='#900F0F')
        self.frame_filtrar.pack(side='left',fill='both',expand=True,padx=10, pady=10)

        #Frame de precios
        self.frame_precio = tk.Frame(self.frame_busqueda,background='#900F0F')
        self.frame_precio.pack(side='top',fill='both',expand=True,padx=10, pady=10)

        self.lbl_precios = tk.Label(self.frame_precio,text='Filtrado por rango de precios',
        background='#1D1B1B', fg='#900F0F',font=('Roboto',13))
        self.lbl_precios.pack(side='top',fill='both')

        self.frame_precio_min = tk.Frame(self.frame_precio,background='#1D1B1B')
        self.frame_precio_min.pack(side='top',fill='both',expand=True,padx=10, pady=10)

        self.frame_precio_max = tk.Frame(self.frame_precio,background='#1D1B1B')
        self.frame_precio_max.pack(side='top',fill='both',expand=True,padx=10, pady=10)

        self.lbl_precio_min = tk.Label(self.frame_precio_min, text='Precio minimo:',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',12))
        self.lbl_precio_min.pack(side='left',fill='both',expand=True, padx=10,pady=10)

        self.txt_precio_min = tk.Entry(self.frame_precio_min, textvariable=self.precio_min)
        self.txt_precio_min.pack(side='left',fill='x',expand=True, padx=10,pady=10)

        self.lbl_precio_max = tk.Label(self.frame_precio_max, text='Precio maximo:',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',12))
        self.lbl_precio_max.pack(side='left',fill='both',expand=True, padx=10,pady=10)

        self.txt_precio_max = tk.Entry(self.frame_precio_max, textvariable=self.precio_max)
        self.txt_precio_max.pack(side='left',fill='x',expand=True, padx=10,pady=10)

        self.btn_buscar = tk.Button(self.frame_busqueda, text='Buscar',command=self.buscar_precio)
        self.btn_buscar.pack(side='top',fill='x',padx=10,pady=10)        

        self.listbox_buscar = tk.Listbox(self.frame_busqueda, justify='center',background='#1D1B1B',
        fg='#900F0F', font=('Roboto',12))
        self.listbox_buscar.pack(side='top',fill='x',expand=True, padx=10,pady=10)
        self.listbox_buscar.insert(tk.END,self.lista_buscar)

        #Frame tipos cocina

        self.frame_cocina = tk.Frame(self.frame_filtrar,background='#900F0F')
        self.frame_cocina.pack(side='top',fill='both',expand=True)

        self.lbl_precios = tk.Label(self.frame_cocina,text='Filtrado por tipos de cocina',
        background='#1D1B1B', fg='#900F0F',font=('Roboto',13))
        self.lbl_precios.pack(side='top',fill='both',padx=10, pady=10)

        self.combo_tipo_cocina = ttk.Combobox(self.frame_cocina,state='readonly')
        self.combo_tipo_cocina.pack(side='left',fill='x',expand=True, padx=10,pady=10)

        self.btn_filtrar = tk.Button(self.frame_cocina, text='Filtrar',command=self.buscar_cocina)
        self.btn_filtrar.pack(side='left',fill='x',padx=10,pady=10)

        self.listbox_filtrar = tk.Listbox(self.frame_filtrar, justify='center',background='#1D1B1B',
        fg='#900F0F', font=('Roboto',12))
        self.listbox_filtrar.pack(side='top',fill='both',expand=True, padx=10,pady=10)
        self.listbox_filtrar.insert(tk.END,self.lista_filtrar)

        #Frame botones

        self.frame_botones = tk.Frame(self.frame_principal, background='#900F0F')
        self.frame_botones.pack(side='right',fill='both',expand=True, padx=10, pady=10)
        
        self.btn_volver = tk.Button(self.frame_botones, text='Volver', command=self.cambio_principal)
        self.btn_volver.pack(side='top',fill='x',padx=10,pady=10) 
        
        #self.btn2 = tk.Button(self.frame_botones, text='Btn2')
        #self.btn2.pack(side='top',fill='x',padx=10,pady=10)

        #self.btn3 = tk.Button(self.frame_botones, text='Btn3') 
        #self.btn3.pack(side='top',fill='x',padx=10,pady=10)

        self.cargar_tipos_cocina()

        
    #Actualiza las listbox    
    
    def buscar_precio(self):
        aux_min = self.precio_min.get()
        aux_max = self.precio_max.get()
        self.listbox_buscar.delete(0,tk.END)
        for des in self.destinos:
            if aux_min >= des.precio_min and aux_max >= des.precio_max:
                self.listbox_buscar.insert(tk.END,des.nombre)
        if self.listbox_buscar.size() == 0:
            tk.messagebox.showinfo(title='Salta Travel Food', message=
                'No encontramos lugares por ese rango de precios')

    def buscar_cocina(self):
        aux_cocina = self.combo_tipo_cocina.get()
        self.listbox_filtrar.delete(0,tk.END)
        for des in self.destinos:
            if des.tipo_cocina == aux_cocina:
                self.listbox_filtrar.insert(tk.END,des.nombre)
    
    def cargar_tipos_cocina(self):
        aux_tipos_cocina = []
        for des in self.destinos:
            aux_tipos_cocina.append(des.tipo_cocina)
        self.combo_tipo_cocina['values'] = aux_tipos_cocina

    """
    def actualizar_listbox_filtrar(self, id):

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
    
    def item_seleccionado_b(self):
        for i in self.listbox_destinos.curselection():
            self.id_item = i
        self.actualizar_listbox_actividades(self.id_item)
    
    def item_seleccionado_f(self):
        for i in self.listbox_destinos.curselection():
            self.id_item = i
        self.actualizar_listbox_actividades(self.id_item)
    """