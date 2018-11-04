from flask import Flask,request
from src.mainProject import Informatic
import json

app = Flask(__name__)



@app.route('/',methods=['GET'])
def js():
    dato={"status": "OK"}
    asd = json.dumps(dato)
    return asd

@app.route('/ruta/<parametro>')
def ruta(parametro):
    dato={ parametro : "Parametro reconocido"}
    asd = json.dumps(dato)
    return asd



if __name__ == "__main__":
    app.run(debug = True)
