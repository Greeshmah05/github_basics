#python -m venv env 
#.\env\Scripts\Activate
# pip install Flask
from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/abc")
def abc():
    return "This is ABC route." #http://127.0.0.1:5000/abc

@app.route("/<name>")
def greet(name):
    return f"Hello, {name}!"

if __name__=="__main__":
    app.run(debug=True)