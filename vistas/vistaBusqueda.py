import tkinter as tk


class VistaBusqueda(tk.Frame):
    def __init__(self, master, controlador):
       #Master es: Ventana, donde estará Vista Inicio
       super().__init__(master)
       self.configure(background='#EEEEEE')
       self.rowconfigure(0,weight=1)
       self.columnconfigure(0,weight=1)
       self.controlador = controlador
       
       self.iniciar_widgets()
    
    def iniciar_widgets(self):
        self.titulo = tk.Label(self,text='Un titulo',background='blue')
        self.titulo.grid(row=4, column=0, columnspan=3, rowspan=1, padx=10, pady=10,sticky='nsew')
        #self.titulo.pack(side='top',fill='x', expand=True,padx=10, pady=10)
        self.titulo.configure(height=0)

        self.lbl = tk.Label(self,text='Ingrese ingrediente',background='red')
        self.lbl.grid(row=0, column=0, rowspan=1, padx=10, pady=10,sticky='nsew')
        self.lbl.configure(height=2)
        self.lbl.columnconfigure(0,weight=1)
        #self.lbl.pack(side='left',fill='x',expand=True,padx=10,pady=10)

        self.txt = tk.Entry(self)
        self.txt.grid(row=1, column=1, rowspan=1, padx=10, pady=10,sticky='nsew')

        self.btn1 = tk.Button(self, text='Buscar')
        self.btn1.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
        self.btn1.columnconfigure(2,weight=1)
        self.btn1.rowconfigure(1,weight=1)
        
        #self.txt.pack(side='right',fill='x',expand=True,padx=10,pady=10)

        self.lbl2 = tk.Label(self,text='Titulo bajo')
        self.lbl2.grid(row=2, columnspan=3, rowspan=1, padx=10, pady=10,sticky='nsew')
        self.lbl2.configure(height=1)
        #self.lbl2.pack(side='bottom',fill='x',expand=True)

        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=3, column=0, columnspan=3, rowspan=3, padx=10, pady=10, sticky='nsew')
        self.listbox.configure(height=10)
