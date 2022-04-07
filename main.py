from flask import Flask, render_template
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    comidas = db.selectAllProdutos('comidas')
    gruposcomidas = db.selectDistinctGrupos('comidas')
    bebidas = db.selectAllProdutos('bebidas')
    gruposbebidas = db.selectDistinctGrupos('bebidas')

    return render_template('index.html', comidas=comidas, gruposcomidas=gruposcomidas, bebidas=bebidas, gruposbebidas=gruposbebidas)

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=False)