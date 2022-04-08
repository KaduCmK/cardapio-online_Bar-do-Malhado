from flask import Flask, render_template, request, redirect
import os
import random
import string
import database as db

app = Flask(__name__)
if os.getenv('DEV') == 'True':
    app.debug = True
else:
    app.debug = False


@app.route('/')
def index():
    comidas = db.selectAllProdutos('comidas')
    gruposcomidas = db.selectDistinctGrupos('comidas')
    bebidas = db.selectAllProdutos('bebidas')
    gruposbebidas = db.selectDistinctGrupos('bebidas')

    return render_template('index.html', comidas=comidas, gruposcomidas=gruposcomidas, bebidas=bebidas, gruposbebidas=gruposbebidas)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        senha = request.form['senha']
        if senha == os.getenv('SENHA_ACESSO'):
            db.generatekey()
            key = db.getKey()
            return redirect(f'/admin/{key}')
        else:
            return render_template('login.html', msg='senha incorreta')
        
    return render_template('login.html')


@app.route('/adicionar')
@app.route('/admin')
def redirecionar():
    return redirect('/login')


@app.route(f'/admin/<link>', methods=['GET', 'POST'])
def admin(link):
    key = db.getKey()
    if link != key:
        return redirect('/login')

    comidas = db.selectAllProdutos('comidas')
    bebidas = db.selectAllProdutos('bebidas')
        
    return render_template('admin.html', comidas=comidas, bebidas=bebidas, key=key)


@app.route(f'/adicionar/<link>', methods=['GET', 'POST'])
def adicionar(link):
    key = db.getKey()
    if link != key:
        return redirect('/login')
    
    if request.method == 'POST':
        table = request.form['table']
        grupo = request.form['grupo']
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        db.inserir(table, grupo, nome, descricao, preco)

        return redirect(f'/admin/{key}')
    
    return render_template('adicionar.html', key=key)
    

if __name__ == '__main__':
    app.run()