from flask import Flask, render_template, request

app = Flask(__name__)

lista_produtos = [
        {"nome": "tapioca", "descricao": "inves de farinha, cocaina"},
        {"nome": "feijão", "descricao": "hmmmmm feijãozim"},
        {"nome": "batata", "descricao": "nunca te esqueceremos sasha"}
    ]

@app.route("/")

def homekkj():
    return render_template("index.html")

@app.route("/desconhecido")
def pagina_desconhecido():
    return render_template("desconhecido.html")

@app.route("/contato")
def pagina_contato():
    return render_template("contato.html")

@app.route("/produtos")
def pagina_produtos():
    return render_template("produtos.html", produtos = lista_produtos)

@app.route("/produtos/cadastro")
def pagina_cadastrar_produtos():
    return render_template("cadastrar_produto.html")

@app.route("/produtos", methods=['POST'])
def cadastar_produto():
    nome = request.form['nome_do_produto']
    descricao = request.form['descricao_do_produto']
    produto = {"nome": nome, "descricao": descricao}
    lista_produtos.append(produto)
    return render_template("produtos.html", produtos = lista_produtos)