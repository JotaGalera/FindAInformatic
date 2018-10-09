from flask import Flask

app = Flask(__name__)


class Informatic:
    def __init__(self):
        self.name = " "
        self.cv = " "
        self.edad = " "

    @app.route('/status')
    def statusFun(self):
        return True

if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
