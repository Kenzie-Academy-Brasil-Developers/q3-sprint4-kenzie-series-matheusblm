import psycopg2

def create_table():
    conn = psycopg2.connect(host="localhost", database="kenzeis", user="hank", password="1234")
    cur = conn.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS ka_series(
                            id BIGSERIAl PRIMARY KEY,
                            serie VARCHAR(100) PRIMARY KEY,
                            seasons integer not null,
                            genre VARCHAR(50) not null,
                            imdb_rating FLOAT(2) not null,
    );""")
    conn.commit()
    cur.close()
    conn.close()

def get_table():
    create_table()
    conn = psycopg2.connect(host="localhost", database="kenzeis", user="hank", password="1234")
    cur = conn.cursor()
    cur.execute(""" SELECT * FROM ka_series""")
    registros = cur.fetchall()
    FIELDNAMES = ["id", "series", "seasons", "genre", "imdb_rating"]
    processed_data = [dict(zip(FIELDNAMES, row)) for row in registros]
    conn.commit()
    cur.close()
    conn.close()
    return processed_data

def create_serie(date):
    create_table()
    conn = psycopg2.connect(host="localhost", database="kenzeis", user="hank", password="1234")
    cur = conn.cursor()
    serie = (date.get("serie"),date.get("seasons"),date.get("genre"),date.get("imdb_rating"), )
    query = 'INSERT INTO ka_series (serie,seasons,genre, imdb_rating) VALUES (%s,%s,%s,%s)'
    cur.execute(query, serie)
    conn.commit()
    cur.close()
    conn.close()
    return date

def filter_serie(id):
    create_table()
    conn = psycopg2.connect(host="localhost", database="kenzeis", user="hank", password="1234")
    cur = conn.cursor()
    query = 'SELECT * FROM ka_series WHERE id like (%s)'
    cur.execute(query, id)
    registros = cur.fetchall()
    FIELDNAMES = ["id", "series", "seasons", "genre", "imdb_rating"]
    processed_data = [dict(zip(FIELDNAMES, row)) for row in registros]
    conn.commit()
    cur.close()
    conn.close()
    return processed_data