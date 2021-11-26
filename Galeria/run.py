import json
from flask import Flask
from waitress import serve

from Galeria.Infraestructura.PersistenciaCuadro import PersistenciaCuadro

class HolaMundo():

    def on_get(self, req, resp, uuid):
        db=PersistenciaCuadro()
        cua = db.load_json('16aa7a38-95e6-4764-8da4-30a907239b8a.json')
        mensajes = ['Hola Mundo', 'Hola que hace', 'Adios', 'Ciao']
        resp.body = json.dump(cua)


app = Flask(__name__)

@app.route("/proyecto")
def hello():
    return "<h1 style='color:blue'> HOLA! </h1>"

if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    serve(app, host='0.0.0.0', port=5000, url_scheme = 'https')
