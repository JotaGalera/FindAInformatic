from flask import Flask,request,jsonify
from src.mainProject import Informatic
import json

app = Flask(__name__)

inf = Informatic("Jota","qwerty",3)

@app.route('/',methods=['GET'])
def satus():
    dato={"status":"OK"}
    return jsonify(dato)

@app.route('/ruta/<parametro>')
def ruta(parametro):
    datos={ parametro : "Parametro reconocido"}
    return jsonify(datos)

@app.route('/changeName/<newname>',methods=['GET'])
def changeName(newname):
    cambio = inf.changeName(newname)
    return "Nombre Cambiado: "+cambio

@app.route('/changeCv/<newcv>',methods=['GET'])
def changeCv(newcv):
    cambio = inf.changeCv(newcv)
    return "Cambio CV: "+cambio

@app.route('/changeAge/<newage>',methods=['GET'])
def changeAge(newage):
    cambio = inf.changeAge(newage)
    return "Cambio de la edad: "+cambio

@app.route('/showData')
def showAll():
    return jsonify(inf.showData())


if __name__ == "__main__":
    app.run(debug = True)
