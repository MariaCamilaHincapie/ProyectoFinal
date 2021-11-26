import uuid


class Cuadro:


    def __init__(self, nombre, artista, descripcion, alto, ancho,
                 tipo_pintura, tipo_tela, precio,  *args, **kargs):
        self.serial = uuid.uuid4()
        self.nombre = nombre
        self.artista = artista
        self.descripcion = descripcion
        self.alto = alto
        self.ancho = ancho
        self.tipo_pintura = tipo_pintura
        self.tipo_tela = tipo_tela
        self.precio =precio


    def __str__(self):
        return  f"{self.serial}--{self.nombre}--{self.artista}--{self.precio}"

    def __repr__(self):
        return str(self.serial)

    def apreciar(self, nuevo_precio):
        self.precio = nuevo_precio

    def cumple(self, especificacion):
        dict_Cuadro = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_Cuadro or dict_Cuadro[k] != especificacion.get_value(k):
                return False
        return  True

