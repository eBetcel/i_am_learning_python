from flask import Flask, flash, redirect, render_template, request, session, url_for
from usuario import Usuario


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo("Tetris", "Puzzle", "Atari")
jogo2 = Jogo("God of War", "Rack n Slash", "PS2")
jogo3 = Jogo("Mortal Kombat", "Luta", "PS2")
lista = [jogo1, jogo2, jogo3]

usuario1 = Usuario("Emanuel", "ebetcel", "alohomora")
usuario2 = Usuario("Maria", "mbetcel", "bts")
usuario3 = Usuario("Flor", "flor", "miau")
users = {usuario1.nickname : usuario1,
        usuario2.nickname : usuario2,
        usuario2.nickname : usuario2,
}

app = Flask(__name__)
app.secret_key = "alura"


@app.route("/")
def index():
    return render_template("lista.html", titulo="Jogos", jogos=lista)


@app.route("/novo")
def novo():
    if "usuario_logado" not in session or session["usuario_logado"] == None:
        return redirect(url_for("login", proxima=url_for("novo")))
    return render_template("novo.html", titulo="Novo Jogo")


@app.route(
    "/criar",
    methods=[
        "POST",
    ],
)
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for("index"))


@app.route("/login")
def login():
    proxima = request.args.get("proxima")
    return render_template("login.html", proxima=proxima)


@app.route(
    "/autenticar",
    methods=[
        "POST",
    ],
)
def autenticar():
    if request.form["usuario"] in users:
        usuario = users[request.form['usuario']]
        if request.form["senha"] == usuario.senha:        
            session["usuario_logado"] = usuario.nickname
            flash("Usuário" + session["usuario_logado"] + "logado com sucesso!")
            return redirect("/")
    else:
        flash("Usuário não logado")
        proxima_pagina = request.form["proxima"]
        return redirect(proxima_pagina)


@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Logout realizado com sucesso")
    return redirect(url_for("index"))


app.run(debug=True)
