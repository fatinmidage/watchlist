from flask import Flask, url_for

app = Flask(__name__)

@app.route('/index')
@app.route('/home')
@app.route('/')
def hello():
    return '<h1>hello totoro</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/u/<username>')
def username(username):
    return username

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('username',username='greyli'))
    print(url_for('username',username='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'