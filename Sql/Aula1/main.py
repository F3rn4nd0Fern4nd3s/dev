import sqlite3 
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

conection = sqlite3.connect(DB_FILE)
cursor = conection.cursor()
# CUIDADO: DELETANDO TODAS AS COLUNAS

# CRUD - Create Read   Update  Delete
# SQL - INSERT  SELECT UPDATE  DELETE
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
# )
# conection.commit()


# # Criar tabela
# cursor.execute(
#     f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
#     '('
#     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#     'name TEXT,'
#     'weight REAL'
#     ')'
# )
# conection.commit()

# # Registrar valores nas colunas da tabela
# # CUIDADO: sql injection
# sql = (
#     f'INSERT INTO {TABLE_NAME}' 
#     '(name, weight) '
#     'VALUES'
#     '(:nome, :peso)'
# )
# #cursor.execute(sql, ['Fernando', 820])
# # cursor.executemany(sql, [['Fernando', 820], ['bruno', 500]])
# cursor.execute(sql, {'nome' : 'Sem nome', 'peso': 30})
# cursor.executemany(sql,(
#     {'nome' : 'Joao', 'peso': 2},
#     {'nome' : 'Joana', 'peso': 33},
#     {'nome' : 'carlos', 'peso': 25},
#     {'nome' : 'joaquim', 'peso': 42}
# )
# )
# conection.commit()

# if '__name__' == '__main__':
#     print(sql)

cursor.execute(
    f'UPDATE {TABLE_NAME}'
    'SET name="IGOR GAY" '
    'WHERE id = 1'
)
conection.commit()

cursor.close()
conection.close()
