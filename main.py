from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def conectar_db():
    conn = sqlite3.connect('./bdm-produtos.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conexao = conectar_db()
    produtos = conexao.execute('SELECT * FROM comidas').fetchall()
    conexao.close()

    return render_template('index.html', produtos=produtos, format=format)

if __name__ == '__main__':
    app.run(debug=True)