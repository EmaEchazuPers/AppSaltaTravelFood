import json

class ModeloActividad:
    def __init__(self, id_actividad, nombre, id_destino, hora_inicio):
        self.id_actividad = id_actividad
        self.nombre = nombre
        self.id_destino = id_destino
        self.hora_inicio = hora_inicio
    
    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**actividad) for actividad in data]
    
    
