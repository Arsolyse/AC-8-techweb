from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/HomePage')
def HomePage():
    return render_template("HomePage.html")


@app.route('/DetalheDeCurso')
def detalhe():
    return render_template("DetalheDeCurso.html")


@app.route('/Disciplina')
def Disciplina():
    return render_template("Disciplina.html")


@app.route('/ListaDeCurso')
def lista():
    return render_template("ListaDeCurso.html")


@app.route('/Noticias')
def Noticias():
    return render_template("Noticias.html")


app.run()
