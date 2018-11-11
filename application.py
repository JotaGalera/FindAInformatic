from flask import Flask,request
from src.mainProject import Informatic
import json

app = Flask(__name__)

inf = Informatic("Jota","qwerty",3)

@app.route('/',methods=['GET'])
def js():
    dato={"status": "OK"}
    asd = json.dumps(dato)
    return asd

@app.route('/ruta/<parametro>')
def ruta(parametro):
    datos={ parametro : "Parametro reconocido"}
    dat = json.dumps(dato)
    return dat

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
    datos = json.dumps(inf.showData())
    return datos


if __name__ == "__main__":
    app.run(debug = True)
