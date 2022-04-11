import os
import psycopg2
import urllib.parse as urlparse
import random
import string

if os.getenv('DEV') == 'True':
    dbname = 'bardomalhado'
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = 'localhost'
    port='5432'
else:
    url = urlparse.urlparse(os.getenv('DATABASE_URL'))
    dbname = url.path[1:]
    user = url.username
    password = url.password
    host = url.hostname
    port = url.port


def conectar():
    conexao = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
    )

    cursor = conexao.cursor()

    return conexao, cursor

def selectAllProdutos(table):
    con, cur = conectar()
    cur.execute(f"SELECT * FROM {table} ORDER BY id;")
    comidas = cur.fetchall()

    cur.close()
    con.close()

    return comidas

def selectAllGrupos(table):
    con, cur = conectar()
    cur.execute(f"SELECT grupo FROM {table}")
    grupos = cur.fetchall()

    cur.close()
    con.close()
    return grupos

def selectDistinctGrupos(table):
    con, cur = conectar()
    cur.execute(f"SELECT DISTINCT grupo FROM {table}")
    grupos = cur.fetchall()

    cur.close()
    con.close()
    return grupos

def selectAllFromGrupo(table, grupo):
    con, cur = conectar()
    cur.execute(f"SELECT * FROM {table} WHERE grupo = '{grupo}'")
    grupos = cur.fetchall()

    cur.close()
    con.close()
    return grupos

def getFromId(table, id):
    con, cur = conectar()
    cur.execute(f"SELECT * FROM {table} WHERE id = {id}")
    produto = cur.fetchone()

    cur.close()
    con.close()

    return produto

def inserir(table, grupo, nome, descricao, preco):
    con, cur = conectar()
    preco = format(float(str(preco.replace(',', '.'))), '.2f')
    cur.execute(f"INSERT INTO {table} (grupo, nome, descricao, preco) VALUES ('{grupo}', '{nome}', '{descricao}', {preco})")
    
    con.commit()
    cur.close()
    con.close()

def alterar(table, id, grupo, nome, descricao, preco):
    con, cur = conectar()
    preco = format(float(str(preco.replace(',', '.'))), '.2f')
    cur.execute(f"""UPDATE {table}
                    SET grupo = '{grupo}',
                        nome = '{nome}',
                        descricao = '{descricao}',
                        preco = {preco}
                    WHERE id = {id}""")
    
    con.commit()
    cur.close()
    con.close()

def alterarGrupo(table, id, grupo):
    con, cur = conectar()
    cur.execute(f"UPDATE {table} SET grupo = '{grupo}' WHERE id = {id};")
    
    con.commit()
    cur.close()
    con.close()

def alterarNome(table, id, nome):
    con, cur = conectar()
    cur.execute(f"UPDATE {table} SET nome = '{nome}' WHERE id = {id};")
    
    con.commit()
    cur.close()
    con.close()

def alterarDescricao(table, id, descricao):
    con, cur = conectar()
    cur.execute(f"UPDATE {table} SET descricao = '{descricao}' WHERE id = {id};")
    
    con.commit()
    cur.close()
    con.close()

def alterarPreco(table, id, preco):
    con, cur = conectar()
    preco = str(preco)
    preco = format(float(preco.replace(',', '.')), '.2f')
    cur.execute(f"UPDATE {table} SET preco = '{preco}' WHERE id = {id};")
    
    con.commit()
    cur.close()
    con.close()

def generatekey():
    con, cur = conectar()
    key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
    cur.execute("DELETE FROM keys;")
    cur.execute(f"INSERT INTO keys (key) VALUES ('{key}');")

    con.commit()
    cur.close()
    con.close()
    return key

def getKey():
    con, cur = conectar()
    cur.execute(f"SELECT * FROM keys")
    key = cur.fetchone()
    
    cur.close()
    con.close()
    return key[0]
  
# conexao.commit()
# c.close()
# conexao.close()