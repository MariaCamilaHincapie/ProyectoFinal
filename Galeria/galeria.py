from Galeria.Dominio.Inventario import Inventario
from Galeria.Dominio.cuadro import Cuadro
from Galeria.Infraestructura.PersistenciaCuadro import PersistenciaCuadro

inventario=Inventario()
import random
import os

if __name__== '__main__':
    saver = PersistenciaCuadro()
    saver.connect()
    nombres = ['Jinete fantasma', 'Caballo', 'Geisha']
    artistas= ['H.Hincapie M.','Macahlu','Jennifer Luna']
    descripcion = ""
    altos = [1.00, 1.20, 1.60, 2.00, 2.30]
    anchos = [1.00, 1.20, 1.60, 2.00, 2.30]
    tipos_tela = ['Lona Costeña']
    tipos_pintura =['Oleo','Vinilo']
    precios = [3000000, 5000000, 10000000]

    nombre = random.choice(nombres)
    artista = random.choice(artistas)
    alto = random.choice(altos)
    ancho = random.choice(anchos)
    tipo_tela = random.choice(tipos_tela)
    tipo_pintura = random.choice(tipos_pintura)
    precio = random.choice(precios)

    c = Cuadro(nombre, artista, descripcion, alto, ancho, tipo_pintura, tipo_tela, precio)
    PersistenciaCuadro.save(c)
    PersistenciaCuadro.save_json(c)
    inventario = Inventario()
    inventario_json=Inventario()
    for file in os.listdir("./files"):
        if '.cua' in file:
            inventario.agregar_cuadro(PersistenciaCuadro.load(file))
        if '.json' in file:
            inventario_json.agregar_cuadro(PersistenciaCuadro.load_json(file))
    for c in inventario.cuadros:
        saver.guardar_cuadro(c)
        PersistenciaCuadro.save(c)
        PersistenciaCuadro.save_json(c)





    





