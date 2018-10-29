from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def js():
    dato={ "status": "OK" }
    asd = json.dumps(dato)
    return asd

if __name__ == "__main__":
    server_name = app.config['SERVER_NAME']
    if server_name and ':' in server_name:
        host, port = server_name.split(":")
        port = int(port)
    else:
        port = 5000
        host = "localhost"
    app.run(host=host, port=port)
