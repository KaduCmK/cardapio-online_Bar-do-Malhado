from flask import Flask, render_template
import database as db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yakirfppeqwbec:d4f0c4c8203aa70da0c5e11269f7c2f7e1860b7626555eb4d356b9f6a1dec449@ec2-3-230-122-20.compute-1.amazonaws.com:5432/dijc1fnk918ej'
SQLAlchemy(app)

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
    app.run(debug=True)