#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def index2(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def index3(parameter):
    return '\n'.join(map(str, range(parameter)))+'\n'

@app.route('/math/<int:param1>/<operation>/<int:param2>')
def index4(param1, operation, param2):
    if operation == '+':
        result = param1 + param2
    elif operation == '-':
        result = param1 - param2
    elif operation == '*':
        result = param1 * param2
    elif operation == 'div':
        if param2 != 0:
            result = param1 / param2
    elif operation == '%':
        if param2 != 0:
            result = param1 % param2
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
