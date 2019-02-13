# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)

@app.route('/add')
def add_operation():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))    
    result = add(a,b)
    return f'{result}'

@app.route('/sub')
def sub_operation():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))    
    result = sub(a,b)
    return f'{result}'

@app.route('/mult')
def mult_operation():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))    
    result = mult(a,b)
    return f'{result}'

@app.route('/div')
def div_operation():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))    
    result = div(a,b)
    return f'{result}'


