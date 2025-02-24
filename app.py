from flask import Flask, render_template

app = Flask(__name__, static_folder='./static', template_folder='./templates')

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/cadastro/")
def cadastro():
  return render_template("cadastro.html")

@app.route("/login/")
def login():
  return render_template("login.html")

@app.route("/baixar/")
def baixar():
  return render_template("baixar.html")


