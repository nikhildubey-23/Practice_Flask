#first we import the module 
from flask import Flask
# then we create the object of the module
app = Flask(__name__)
#creating the decorator for routing the packet 
@app.route("/")
# function to print the hello world in the web app
def helloworld():
    return 'Hello world'
#executing the program
if __name__ == "__main__":
    app.run(debug = True , port=8888)
    