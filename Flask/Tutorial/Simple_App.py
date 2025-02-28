from flask import Flask

#Creates WSGI Application
app = Flask(__name__)

# Decorator which takes URL
@app.route('/')
def welcome():
    return "welcome to flask"

# To access this, use the url generated and in address bar type '/hello'
@app.route('/hello')
def hello():
    return "Hello"

if __name__ == '__main__':
    app.run(debug = True)
