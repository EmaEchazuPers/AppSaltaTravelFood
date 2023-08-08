import tkinter as tk
from tkinter import ttk
from vistas import vistaDestinos as Vds


class VistaReview(tk.Frame):
    def __init__(self, master, controlador):

        super().__init__(master)
        self.configure(background='#900F0F')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.controlador = controlador
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.comentario = tk.StringVar()
        self.usuarios = self.controlador.obtener_usuarios()
        self.destinos = self.controlador.obtener_destinos()
        self.reviews = self.controlador.obtener_reviews()


        self.iniciar_widgets()
    
    def cambio_destino(self):
        self.controlador.mostrar_frame(Vds.VistaDestinos)


    def iniciar_widgets(self):

        #Frame principal

        self.frame_principal = tk.Frame(self,background='#1D1B1B')
        self.frame_principal.pack(side='top',fill='both',expand=True)

        self.titulo = tk.Label(self.frame_principal,text='Formulario - Salta Food Travel',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',18))
        self.titulo.pack(side='top',fill='x', padx=10, pady=10)

        #Frame formulario

        self.frame_formulario = tk.Frame(self.frame_principal,background='#900F0F')
        self.frame_formulario.pack(side='left', fill='both',expand=True,padx=10, pady=10)

        self.lbl_formulario = tk.Label(self.frame_formulario, text='Carga tu review aquí',
        background='#1D1B1B',fg='#900F0F',font=('Roboto',13))
        self.lbl_formulario.pack(side='top', fill='x', padx=10,pady=10)

        #Frame destino

        self.frame_destino = tk.Frame(self.frame_formulario,background='#1D1B1B')
        self.frame_destino.pack(side='top', fill='both',expand=True,padx=10, pady=10)

        self.lbl_destino = tk.Label(self.frame_destino,text='Destino: ',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',13) ,width=10)
        self.lbl_destino.pack(side='left',fill='both',expand=True, padx=10,pady=10)

        self.combo_destino = ttk.Combobox(self.frame_destino,state='readonly',width=10)
        self.combo_destino.pack(side='left',fill='x',expand=True, padx=10,pady=10)

        #Frame nombre

        self.frame_nombre = tk.Frame(self.frame_formulario,background='#1D1B1B')
        self.frame_nombre.pack(side='top', fill='both',expand=True,padx=10, pady=10)

        self.lbl_nombre = tk.Label(self.frame_nombre,text='Nombre: ',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',13) ,width=10)
        self.lbl_nombre.pack(side='left',fill='both',expand=True, padx=10,pady=10)

        self.txt_nombre = tk.Entry(self.frame_nombre,textvariable=self.nombre,width=10)
        self.txt_nombre.pack(side='left',fill='x',expand=True,padx=10,pady=10)

        #Frame apellido
        
        self.frame_apellido = tk.Frame(self.frame_formulario,background='#1D1B1B')
        self.frame_apellido.pack(side='top', fill='both',expand=True,padx=10, pady=10)

        self.lbl_apellido = tk.Label(self.frame_apellido,text='Apellido: ',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',13),width=10)
        self.lbl_apellido.pack(side='left',fill='x',expand=True,padx=10,pady=10)

        self.txt_apellido = tk.Entry(self.frame_apellido,textvariable=self.apellido,width=10)
        self.txt_apellido.pack(side='left',fill='x', expand=True,padx=10,pady=10)

        #Frame comentario

        self.frame_comentario = tk.Frame(self.frame_formulario,background='#1D1B1B')
        self.frame_comentario.pack(side='top', fill='both',expand=True, padx=10, pady=10)

        self.lbl_comentario = tk.Label(self.frame_comentario,text='Comentario: ',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',13),width=10)
        self.lbl_comentario.pack(side='left',fill='x', expand=True,padx=10,pady=10)

        self.txt_comentario = tk.Entry(self.frame_comentario,textvariable=self.comentario,width=10)
        self.txt_comentario.pack(side='left',fill='x',expand=True,padx=10,pady=10)

        #Frame calificacion

        self.frame_calificacion = tk.Frame(self.frame_formulario,background='#1D1B1B')
        self.frame_calificacion.pack(side='top', fill='both',expand=True, padx=10, pady=10)

        self.lbl_calificacion = tk.Label(self.frame_calificacion,text='Calificacion: ',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',13),width=10)
        self.lbl_calificacion.pack(side='left',fill='x', expand=True,padx=10,pady=10)

        self.combo_calificacion = ttk.Combobox(self.frame_calificacion,state='readonly',width=10)
        self.combo_calificacion.pack(side='left',fill='x',expand=True, padx=10,pady=10)
        self.combo_calificacion['values'] = [1,2,3,4,5]

        #Frame animo

        self.frame_animo = tk.Frame(self.frame_formulario,background='#1D1B1B')
        self.frame_animo.pack(side='top', fill='both',expand=True,padx=10, pady=10)

        self.lbl_animo = tk.Label(self.frame_animo,text='Animo: ',
        background='#900F0F',fg='#1D1B1B',font=('Roboto',13),width=10)
        self.lbl_animo.pack(side='left',fill='x',expand=True,padx=10,pady=10)

        self.combo_animo = ttk.Combobox(self.frame_animo,state='readonly',width=10)
        self.combo_animo.pack(side='left',fill='x',expand=True, padx=10,pady=10)
        self.combo_animo['values'] = ['Positivo','Negativo']

        #Frame botones

        self.frame_botones = tk.Frame(self.frame_principal,background='#900F0F')
        self.frame_botones.pack(side='left',fill='both',expand=True, padx=10, pady=10)

        self.btn1 = tk.Button(self.frame_botones, text='Cargar',command=self.cargar_datos)
        self.btn1.pack(side='top',fill='x',padx=10,pady=10) 

        self.btn2 = tk.Button(self.frame_botones, text='Volver',command=self.cambio_destino) 
        self.btn2.pack(side='top',fill='x',padx=10,pady=10) 

        self.cargar_destinos()
    
    def cargar_datos(self):
        aux_destino = self.combo_destino.get()
        aux_nombre = self.nombre.get()
        aux_apellido = self.apellido.get()
        aux_comentario = self.comentario.get()
        aux_calificacion = self.combo_calificacion.get()
        aux_animo = self.combo_animo.get()
        id_usuario = 0
        
        if self.existe_usuario(aux_nombre,aux_apellido):
            pass
        else:
            lista_aux = self.crear_lista_usuarios(aux_nombre, aux_apellido)
            self.controlador.carga_datos_usuario(lista_aux)
            id_usuario = self.devolver_id_usuario()
            tk.messagebox.showinfo(title='Salta Travel Food', message=
                'Se cargo con éxito tu review!')
        lista_aux_rev = self.crear_lista_reviews(aux_destino,id_usuario,aux_calificacion, aux_comentario, aux_animo)
        self.controlador.carga_datos_reviews(lista_aux_rev)
        self.limpiar()
        
    
    def crear_lista_usuarios(self,nombre,apellido):
        aux_id = 0
        lista_aux = []
        for usu in self.usuarios:
            dicc_aux = {}
            dicc_aux['id_usuario'] = usu.id_usuario
            dicc_aux['nombre'] = usu.nombre
            dicc_aux['apellido'] = usu.apellido
            dicc_aux['historial_rutas'] = usu.historial_rutas
            lista_aux.append(dicc_aux)
            aux_id = usu.id_usuario
        aux_id = aux_id + 1
        dicc_usuario = { 
            'id_usuario' : aux_id,
            'nombre' : nombre,
            'apellido' : apellido,
            'historial_rutas' : []
        }
        
        lista_aux.append(dicc_usuario)        
        return lista_aux
    
    def crear_lista_reviews(self, destino, id_usuario, calificacion, comentario, animo):
        aux_id = 0
        lista_aux = []
        aux_id_destino = self.devolver_id_destino(destino)
        for rev in self.reviews:
            dicc_aux = {}
            dicc_aux['id_review'] = rev.id_review
            dicc_aux['id_destino'] = rev.id_destino
            dicc_aux['id_usuario'] = rev.id_usuario
            dicc_aux['calificacion'] = rev.calificacion
            dicc_aux['comentario'] = rev.comentario
            dicc_aux['animo'] = rev.animo
            lista_aux.append(dicc_aux)
            aux_id = rev.id_review
        aux_id = aux_id + 1
        dicc_review = { 
            'id_review' : aux_id,
            'id_destino' : aux_id_destino,
            'id_usuario' : id_usuario,
            'calificacion' : int(calificacion),
            'comentario': comentario,
            'animo' : animo
        }
        
        lista_aux.append(dicc_review)
        return lista_aux
    
    def existe_usuario(self, nombre,apellido):
        existe_bool = False
        for usu in self.usuarios:
            if usu.nombre == nombre:
                if usu.apellido == apellido:
                    return True
                else:
                    existe_bool = False
            else:
                existe_bool = False
        return existe_bool

    def cargar_destinos(self):
        lista = []
        for des in self.destinos:
            lista.append(des.nombre)
        self.combo_destino['values']=lista
    
    def id_usuario(self, id):
        return id

    def devolver_id_destino(self,destino):
        id_aux = 0
        for des in self.destinos:
            if destino == des.nombre:
                id_aux = des.id_destino
        return id_aux

    def devolver_id_usuario(self):
        id_aux = 0
        for usu in self.usuarios:
            id_aux = usu.id_usuario
        return id_aux
        
    def limpiar(self):
        self.txt_nombre.delete(0,tk.END)
        self.txt_apellido.delete(0,tk.END)
        self.txt_comentario.delete(0,tk.END)
        self.combo_calificacion.delete(0,tk.END)
        self.combo_animo.delete(0,tk.END)