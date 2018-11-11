from flask import Flask
import json

app = Flask(__name__)


class Informatic:

    def __init__(self,name,cv,edad):
        self.name = name
        self.cv = cv
        self.age = edad



    def statusFun(self):
        return True


    def changeName(self,new_name):
        if(self.name != new_name and len(new_name)>2):
            self.name = new_name
        return self.name

    def changeCv(self,new_cv):
        if(self.cv != new_cv):
            self.cv = new_cv
        return self.cv

    def changeAge(self,new_age):
        if(self.age != new_age):
            self.age = new_age
        return self.age

    def showData(self):
        if(len(self.name)>0 and len(self.cv)>0 and int(self.age) > 0):
            dato = {'Nombre':self.name, 'CV':self.cv, 'Edad':self.age}
        else:
            dato = "Error en los datos del usuario."
        return dato


if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
