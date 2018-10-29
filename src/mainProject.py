from flask import Flask
import json

app = Flask(__name__)


class Informatic:

    def __init__(self,name,cv,edad):
        self.name = name
        self.cv = cv
        self.age = edad

    

    @app.route('/status')
    def statusFun(self):
        return True

    #Modificaciones de datos propios de cada informatico
    @app.route('/chname')
    def changeName(self,new_name):
        if(self.name != new_name and len(new_name)>2):
            self.name = new_name
        return self.name

    @app.route('/chcv')
    def changeCv(self,new_cv):
        if(self.cv != new_cv):
            self.cv = new_cv
        return self.cv

    @app.route('/chage')
    def changeAge(self,new_age):
        if(self.age != new_age):
            self.age = new_age
        return self.age

    #Mostrando datos
    @app.route('/showAll')
    def showData(self):
        if(len(self.name)>0 and len(self.cv)>0 and self.age>0):
            print("Nombre:",self.name)
            print("CV",self.cv)
            print("Edad",self.age)

if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
