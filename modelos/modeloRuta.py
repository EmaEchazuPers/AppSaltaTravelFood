import json

class ModeloRuta:
    def __init__(self,id_visita, nombre, destinos):
        self.id_visita = id_visita
        self.nombre = nombre
        self.destinos= destinos
    
    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**ruta) for ruta in data]

 
