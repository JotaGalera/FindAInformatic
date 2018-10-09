#import bin.main
import unittest
import flask 
from src.mainProject import Informatic

app = flask.Flask(__name__)

class testProject(unittest.TestCase):
    def setUp(self):
        self.inf = Informatic()

    def test_Status(self):
        self.assertEqual(self.inf.statusFun(),True,"Devuelve OKEY")
