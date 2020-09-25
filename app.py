from flask import Flask

app = Flask(__name__)

#define root/starting point
@app.route('/')

def hello_world():
    return 'Hello world'
  