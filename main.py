from flask import Flask, render_template, request, redirect
import os
import database as db
import codigoQR

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
            key = db.generatekey()
            return redirect(f'/admin/{key}')
        else:
            return render_template('login.html', msg='senha incorreta')
        
    return render_template('login.html')


@app.route('/pagar', methods=['GET', 'POST'])
def pagar():
    if request.method == 'POST':
        valor = str(format(float(request.form['valor']), '.2f'))
        codigoQR.gerarQRCode(valor)

    return render_template('pagar.html', valor=valor)


@app.route('/adicionar')
@app.route('/admin')
def redirecionar():
    return redirect('/login')


@app.route(f'/admin/<link>', methods=['GET', 'POST'])
def admin(link):
    key = db.getKey()
    if link != key:
        return redirect('/login')
    
    if request.method == 'POST':
        db.alterar(
            request.form['table'],
            request.form['id'],
            request.form['grupo'],
            request.form['nome'],
            request.form['descricao'],
            request.form['preco']
        )

    comidas = db.selectAllProdutos('comidas')
    bebidas = db.selectAllProdutos('bebidas')
        
    return render_template('admin.html', comidas=comidas, bebidas=bebidas, key=key, remover=db.remover)


@app.route(f'/adicionar/<link>', methods=['GET', 'POST'])
def adicionar(link):
    key = db.getKey()
    if link != key:
        return redirect('/login')
    
    if request.method == 'GET':
        table = request.args['table']
    
    if request.method == 'POST':
        table = request.form['table']
        grupo = request.form['grupo']
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        db.inserir(table, grupo, nome, descricao, preco)

        return redirect(f'/admin/{key}')
    
    return render_template('adicionar.html', key=key, table=table)
    

@app.route(f'/editar/<table>/<id>/<link>', methods=['GET', 'POST'])
def editar(table, id, link):
    key = db.getKey()
    if link != key:
        return redirect('/login')
    
    if request.method == 'POST':
        produto = db.getFromId(table, id)

    return render_template('editar.html', produto=produto, table=table, key=key)


@app.route(f'/remover/<link>', methods=['POST'])
def remover(link):
    key = db.getKey()
    if link != key:
        return redirect('/login')

    table = request.form['table']
    id = request.form['id']
    db.remover(table, id)

    return redirect(f'/admin/{key}')


if __name__ == '__main__':
    app.run()