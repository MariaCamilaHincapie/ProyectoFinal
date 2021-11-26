from Galeria.Dominio.EspecificacionCuadro import EspecificacionCuadro
from Galeria.Dominio.cuadro import Cuadro


class Inventario():

    def __init__(self):
        self.cuadros = []

    def agregar_cuadro(self,cuadro):
        if type(cuadro) == Cuadro:
            espec = EspecificacionCuadro()
            espec.agregar_parametro('serial', cuadro.serial)
            if len(list(self.buscar(espec))) == 0:
                self.cuadros.append(cuadro)
            else:
                raise Exception('Cuadro repetido')

    def buscar(self,especificacion):

        for c in self.cuadros:
            if c.cumple(especificacion):
                yield c
