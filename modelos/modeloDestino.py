import json

class ModeloDestino:
    def __init__(self, id_destino, nombre, tipo_cocina, ingredientes, precio_min, precio_max, popularidad, disponibilidad, id_ubicacion,imagen):        
        self.id_destino = id_destino
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_min = precio_min
        self.precio_max = precio_max
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**destino) for destino in data]
 