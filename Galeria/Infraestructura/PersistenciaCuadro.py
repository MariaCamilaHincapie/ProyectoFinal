import pickle
import sqlite3
import jsonpickle

from Galeria.Dominio.cuadro import Cuadro


class PersistenciaCuadro():

    def connect(self):
        self.con = sqlite3.connect("Galeria_Hincapie.sqlite")
        self.__crear_tabla()


    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE CUADRO(serial text primary key, nombre text," \
                " artista text, descripcion text, alto float," \
                " ancho float, tipo pintura text, tipo tela text, precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_cuadro(self,cuadro : Cuadro):
        cursor = self.con.cursor()
        query = "insert into CUADRO(serial , nombre ," \
                " artista , descripcion , alto ," \
                " ancho , tipo pintura , tipo tela, precio ) values(" \
                f" ?,?,?,?,?,?,?,?,?)"
        cursor.execute(query,(str(cuadro.serial),cuadro.nombre,cuadro.artista,
                              cuadro.descripcion,str(cuadro.alto),
                              str(cuadro.ancho),cuadro.tipo_pintura,cuadro.tipo_tela, str(cuadro.precio)))
        self.con.commit()

    @classmethod
    def save(cls, cuadro):
        binary_open = open("files/"+str(cuadro.serial) + '.cua', mode='wb')
        pickle.dump(cuadro, binary_open)
        binary_open.close()


    @classmethod
    def load(cls, file_name):
        binary_open = open("files/"+file_name, mode='rb')
        cuadro = pickle.load(binary_open)
        binary_open.close()
        return cuadro


    @classmethod
    def save_json(cls, cuadro):
        text_open = open("files/"+str(cuadro.serial) + '.json', mode='w')
        json_gui = jsonpickle.encode(cuadro)
        text_open.write(json_gui)
        text_open.close()


    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_gui = text_open.readline()
        cuadro = jsonpickle.decode(json_gui)
        text_open.close()
        return cuadro