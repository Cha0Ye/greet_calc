from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    '''returns simple welcome greeting'''
    return '''<!doctype html>
              <html>
                <head>
                <title>Welcome</title>
              </head>
                <body>
                    <h1>Welcome</h1>
                <body>
              </html>'''

@app.route('/welcome/home')
def welcome_home():
    '''returns welcome home'''
    return  '''<!doctype html>
              <html>
                <head>
                <title>Welcome home</title>
              </head>
                <body>
                    <h1>Welcome home</h1>
                <body>
              </html>'''

@app.route('/welcome/back')
def welcome_back():
    '''returns welcome back'''
    return  '''<!doctype html>
              <html>
                <head>
                <title>Welcome back</title>
              </head>
                <body>
                    <h1>Welcome back</h1>
                <body>
              </html>'''