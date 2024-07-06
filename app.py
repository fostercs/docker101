import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/starships')
def starship():
    req = requests.get('https://swapi.dev/api/starships/')
    fmt = req.text
    return fmt