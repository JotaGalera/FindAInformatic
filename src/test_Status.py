import unittest
import flask
from src.mainProject import Informatic

app = flask.Flask(__name__)

class testProject(unittest.TestCase):
    def setUp(self):
        self.inf = Informatic("Carlos","CV old",18)
        return self.inf

    def test_Status(self):
        self.assertEqual(self.inf.statusFun(),True,"Devuelve OKEY")

    def test_changeName(self):
        self.assertEqual(self.inf.changeName("Javier"),"Javier","Nombre cambiado")

    def test_changeCv(self):
        self.assertEqual(self.inf.changeCv("Cambio mi cv"),"Cambio mi cv","CV cambiado")

    def test_changeAge(self):
        self.assertEqual(self.inf.changeAge(25),25,"Edad cambiada")


if __name__ == '__main__':
    unittest.main()
