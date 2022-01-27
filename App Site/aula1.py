from distutils.log import debug
from flask import Flask
from templates import *

app = Flask(__name__)

@app.route('/')
def raiz ():
    return 'Olá mundo'


app.run(debug=True)
