from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def hello_world():
    # return 'hello world'
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True,port=8888)
@app.route("/about")
def about():
    return render_template("about.html")
