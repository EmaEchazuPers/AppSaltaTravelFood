import json

class ModeloReview:
    def __init__(self, id_review, id_destino, id_usuario,calificacion, comentario, animo):
        self.id_review = id_review
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
    
    @classmethod
    def carga_json(cls,archivo):
        with open(archivo,'r') as f:
            data = json.load(f)
        return [cls(**review) for review in data]

    @classmethod
    def escribir_json(cls, dicc, archivo):
        with open(archivo,'w+') as f:
            json.dump(dicc,f)
