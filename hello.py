from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! zuleth cochi no se bana lol</p>"

@app.route("/saludo")
def saludoatodos():
    return "<center>Saludos a todos"

@app.route("/correo")
def sobremi():
    return"<marquee><h3> laura.zayola@uabc.edu.mx </h3></marquee>"