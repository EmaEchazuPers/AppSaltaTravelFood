import tkinter as tk
from tkinter import ttk
from vistas import vistaDestinos as Vds


class VistaReview(tk.Frame):
    def __init__(self, master, controlador):

        super().__init__(master)
        self.configure(background='#EEEEEE')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.comentario = tk.StringVar()


        self.iniciar_widgets()
    
    def cambio_destino(self):
        self.controlador.mostrar_frame(Vds.VistaDestinos)


    def iniciar_widgets(self):

        #Frame principal

        self.frame_principal = tk.Frame(self)
        self.frame_principal.configure(background='yellow')
        self.frame_principal.pack(side='top',fill='both',expand=True)

        self.titulo = tk.Label(self.frame_principal,text='Formulario - Salta Food Travel')
        self.titulo.pack(side='top',fill='x', padx=10, pady=10)

        #Frame destinos

        self.frame_formulario = tk.Frame(self.frame_principal)
        self.frame_formulario.pack(side='left', fill='both',expand=True)

        self.lbl_formulario = tk.Label(self.frame_formulario, text='Carga tu review aquí')
        self.lbl_formulario.pack(side='top', fill='x', padx=10,pady=10)

        #Frame nombre

        self.frame_nombre = tk.Label(self.frame_formulario)
        self.frame_nombre.pack(side='top', fill='both', padx=10,pady=10)

        self.lbl_nombre = tk.Label(self.frame_nombre,text='Nombre: ',textvariable=self.nombre)
        self.lbl_nombre.pack(side='left',fill='x',padx=10,pady=10)

        self.txt_nombre = tk.Entry(self.frame_nombre)
        self.txt_nombre.pack(side='left',fill='x',padx=10,pady=10)

        #Frame apellido
        
        self.frame_apellido = tk.Label(self.frame_formulario)
        self.frame_apellido.pack(side='top', fill='both', padx=10,pady=10)

        self.lbl_apellido = tk.Label(self.frame_apellido,text='Apellido: ',textvariable=self.apellido)
        self.lbl_apellido.pack(side='left',fill='x',padx=10,pady=10)

        self.txt_apellido = tk.Entry(self.frame_apellido)
        self.txt_apellido.pack(side='left',fill='x',padx=10,pady=10)

        #Frame comentario

        self.frame_comentario = tk.Label(self.frame_formulario)
        self.frame_comentario.pack(side='top', fill='both', padx=10,pady=10)

        self.lbl_comentario = tk.Label(self.frame_comentario,text='Comentario: ',textvariable=self.comentario)
        self.lbl_comentario.pack(side='left',fill='x',padx=10,pady=10)

        self.txt_comentario = tk.Entry(self.frame_comentario)
        self.txt_comentario.pack(side='left',fill='x',padx=10,pady=10)

        #Frame calificacion

        self.frame_calificacion = tk.Label(self.frame_formulario)
        self.frame_calificacion.pack(side='top', fill='both', padx=10,pady=10)

        self.lbl_calificacion = tk.Label(self.frame_calificacion,text='Calificacion: ')
        self.lbl_calificacion.pack(side='left',fill='x',padx=10,pady=10)

        self.combo_calificacion = ttk.Combobox(self.frame_calificacion,state='readonly')
        self.combo_calificacion.pack(side='left',fill='x',expand=True, padx=10,pady=10)
        self.combo_calificacion['values'] = [1,2,3,4,5]

        #Frame animo

        self.frame_animo = tk.Label(self.frame_formulario)
        self.frame_animo.pack(side='top', fill='both', padx=10,pady=10)

        self.lbl_animo = tk.Label(self.frame_animo,text='Animo: ')
        self.lbl_animo.pack(side='left',fill='x',padx=10,pady=10)

        self.combo_animo = ttk.Combobox(self.frame_animo,state='readonly')
        self.combo_animo.pack(side='left',fill='x',expand=True, padx=10,pady=10)
        self.combo_animo['values'] = ['Positivo','Negativo']

        #Frame botones

        self.frame_botones = tk.Frame(self.frame_principal, background='black')
        self.frame_botones.pack(side='left',fill='both',expand=True, padx=10, pady=10)

        self.btn1 = tk.Button(self.frame_botones, text='Cargar',command=self.cargar_datos)#,command=self.item_seleccionado) 
        self.btn1.pack(side='top',fill='x',padx=10,pady=10) 

        self.btn2 = tk.Button(self.frame_botones, text='Volver',command=self.cambio_destino) 
        self.btn2.pack(side='top',fill='x',padx=10,pady=10) 
    
    def cargar_datos(self):
        aux_nombre = self.nombre.get()
        aux_apellido = self.nombre.get()
        aux_comentario = self.comentario.get()
        aux_calificacion = self.combo_calificacion.get()
        aux_animo = self.combo_animo.get()
        dicc_aux = { 
        }
        pass