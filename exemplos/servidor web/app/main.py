from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/hello/<nome>')
def hello_nome(nome):
    return "Hello " + nome

@app.route('/formulario')
def formulario():
    return render_template('formulario_imc.html')

@app.route('/imc', methods=['POST'])
def imc():
    peso = float(request.form.get('Peso'))
    altura = float(request.form.get('Altura'))
    imc = peso / (altura * altura)
    return render_template('resposta_imc.html', imc=imc)

app.run()
