import json

class ModeloUbicacion:
    def __init__(self,id_ubicacion, direccion,coordenadas):
        self.id_ubicacion = id_ubicacion
        self.direccion = direccion
        self.coordenadas= coordenadas

    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**ubicacion) for ubicacion in data]
