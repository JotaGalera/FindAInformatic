from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def js():
    dato={ "status": "OK" }
    asd = json.dumps(dato)
    return asd

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0')
