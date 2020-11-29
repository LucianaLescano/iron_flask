from flask import Flask, request
import markdown.extensions.fenced_code
import random
import tools.getdata as get
import json
import tools.postdata as pos


app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string



@app.route("/ejemplo1")
def datitos():
    diccionario = { "Nombre" : "Fer",
    "Amigos" : ["Dobby", "Ras", "Sherriff", "Ignacio"],
    "Edad" : 28
    }
    return diccionario



@app.route("/tiraeldado")
def dados():
    dado = random.choice(range(1,7))
    return f"{dado}"



@app.route("/frases/<personaje>")
def frasepersonaje(personaje):
    frases = get.mensajepersonaje(personaje)
    return json.dumps(frases)



@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    escena = request.form.get("scene")
    personaje = request.form.get("character_name")
    frase = request.form.get("dialogue")
    pos.insertamensaje(escena, personaje, frase)
    return "Mensaje introducido correctamente en la base de datos"




















app.run(debug=True)