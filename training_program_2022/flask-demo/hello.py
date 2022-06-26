from urllib import response
from flask import Flask, make_response, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World!</h1> \n <p>Your browser is {}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/400')
def error_400():
    return '<h1>Error: %s</h1>' % 400

@app.route('/set-cookie')
def go_set_cookie():
    response = make_response('<h1> This document carries a cookie. </h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirect')
def go_redirect():
    return redirect('http://www.baidu.com')

@app.route('/index')
def home():
    return render_template('index.html')