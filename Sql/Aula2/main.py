# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= 'Nando@123',
    database= 'exe_data',
)

with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(  # type: ignore
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )

        cursor.execute(f' TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

 # COMEÇAR A MANIPULAR DADOS.
 # INSERINDO UM VALOR
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Luiz', 18)
        result = cursor.execute(sql, data)  # type: ignore
        # print(sql, data)
        # print(sql, data)
        # print(result)
    connection.commit()

 # INSERINDO VALORES (DICIONÁRIOS)

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "age": 37,
            "name": "Le",
        }
        result = cursor.execute(sql, data2)  # type: ignore

 # INSERINDO VARIOS VALORES (DICIONÁRIOS)

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Sah", "age":33, },
            {"name": "Julia", "age":50, },
            {"name": "Raissa", "age":73, },
            {"name": "Sabrina", "age":45, },
            )
        result = cursor.executemany(sql, data3)  # type: ignore
        # print(sql)
        # print(data3)
        # print(result)
    connection.commit()

 # LENDO VALORES DO BANCO DE DADOS!

    with connection.cursor() as cursor:
            menor_id = 1
            maior_id = 8
            
            
            sql = (
                 f'SELECT * FROM {TABLE_NAME} '
                 'WHERE id BETWEEN %s AND %s '
            )
            cursor.execute(sql, (menor_id, maior_id)) # type: ignore
            # print(cursor.mogrify(sql, (menor_id, maior_id)))
            data5 = cursor.fetchall()

            # for row in data5:
            #      print(row)


# Apagando valores 

    with connection.cursor() as cursor:        

        sql = (
                f'DELETE FROM {TABLE_NAME} '
                'WHERE id = 4 '
        )
        cursor.execute(sql)
        cursor.execute(F'SELECT * FROM {TABLE_NAME}')
        connection.commit() # type: ignore

        # for row2 in cursor.fetchall():
        #     print(row2)
        
# Editando Dados

    with connection.cursor() as cursor:        

        sql = (
                f'UPDATE {TABLE_NAME} '
                'SET nome=%s,  idade=%s '
                'WHERE id=%s'
        )
        cursor.execute(sql, ('nando', 23, 1))
        cursor.execute(F'SELECT * FROM {TABLE_NAME}') # type: ignore
        connection.commit()

        for row2 in cursor.fetchall():
            print(row2)
