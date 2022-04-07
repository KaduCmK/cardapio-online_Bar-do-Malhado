import os
import psycopg2

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

def conectar():
    conexao = psycopg2.connect(
    host=os.getenv('DATABASE_URL'),
    database=os.getenv('DATABASE'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
    )

    cursor = conexao.cursor()

    return conexao, cursor

def selectAllProdutos(table):
    con, cur = conectar()
    cur.execute(f"SELECT * FROM {table};")
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

def getByGrupo(table, grupo):
    con, cur = conectar()
    cur.execute(f"SELECT * FROM {table} WHERE grupo = '{grupo}'")
    grupos = cur.fetchall()

    cur.close()
    con.close()
    return grupos

def inserir(table, grupo, nome, descricao=' ', preco=00.00):
    con, cur = conectar()
    cur.execute(f"INSERT INTO {table} (grupo, nome, descricao, preco) VALUES ('{grupo}', '{nome}', '{descricao}', {preco})")
    
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

# inserir('Bernardo', 'Santos', 8)
  
# conexao.commit()
# c.close()
# conexao.close()