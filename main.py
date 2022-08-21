from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/servers/monitoring", methods=['POST'])
def servers_monitoring():
    payload = request.json 
    return payload


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
