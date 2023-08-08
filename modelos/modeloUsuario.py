import json
import controladorVentana

class ModeloUsuario:
    def __init__(self,id_usuario,nombre,apellido,historial_rutas):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas
    
    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**usuario) for usuario in data]
    
    @classmethod
    def escribir_json(cls, dicc, archivo):
        with open(archivo,'w+') as f:
            json.dump(dicc,f)
    #   return cls(**datos)


    