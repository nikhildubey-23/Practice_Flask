# hello world program using flask
from flask import Flask
def hello():
    return 'hello world'
app = Flask(__name__)
app.add_url_rule('/', 'hello', hello)
app.run()
