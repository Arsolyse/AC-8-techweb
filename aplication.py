from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/HomePage.html')
def HomePage():
    return render_template("HomePage.html")


@app.route('/DetalheDeCurso.html')
def detalhe():
    return render_template("DetalheDeCurso.html")


@app.route('/Disciplina.html')
def Disciplina():
    return render_template("Disciplina.html")


@app.route('/ListaDeCurso.html')
def lista():
    return render_template("ListaDeCurso.html")


@app.route('/Noticias.html')
def Noticias():
    return render_template("Noticias.html")


app.run()
