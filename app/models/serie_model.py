import psycopg2 

class Serie:
    def __init__(self, serie, seasons, released_date, genre, imdb_rating) -> None:
        self.serie = serie
        self.seasons = seasons
        self.released_date = released_date
        self.genre = genre
        self.imdb_rating = imdb_rating

    def create_serie(data):
        conn = psycopg2.connect(host="localhost", database="kenzies", user="hank", password="1234")
        create_table()
        cur = conn.cursor()
        series = (data["serie"].title(), data["seasons"],data["released_date"],data["genre"].title(),data["imdb_rating"])
        query = """
            INSERT INTO ka_series
                (serie, seasons, released_date, genre, imdb_rating)
            VALUES  
                (%s, %s,%s,%s,%s)
            RETURNING *;
        """
        try:
            cur.execute(query, series)
            registros = cur.fetchone()
            FIELDNAMES = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]
            processed_data = dict(zip(FIELDNAMES, registros))
            conn.commit()
            cur.close()
            conn.close()
            return processed_data
        except psycopg2.errors.UniqueViolation:
            cur.close()
            conn.close()
            return 'erro'

    def get_all_series():
        create_table()
        conn = psycopg2.connect(host="localhost", database="kenzies", user="hank", password="1234")
        cur = conn.cursor()
        cur.execute("SELECT * from ka_series;")
        registros = cur.fetchall()
        FIELDNAMES = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]
        processed_data = [dict(zip(FIELDNAMES, row)) for row in registros]
        conn.commit()
        cur.close()
        conn.close()
        return processed_data

    def filter_serie(id):
        create_table()
        conn = psycopg2.connect(host="localhost", database="kenzies", user="hank", password="1234")
        cur = conn.cursor()
        cur.execute(f"SELECT * from ka_series WHERE id={id}")
        registros = cur.fetchone()
        FIELDNAMES = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]
        try:
            processed_data = dict(zip(FIELDNAMES, registros))
        except TypeError:
            processed_data = None
        conn.commit()
        cur.close()
        conn.close()
        return processed_data



def create_table():
    conn = psycopg2.connect(host="localhost", database="kenzies", user="hank", password="1234")
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS ka_series (
                id BIGSERIAL PRIMARY KEY,
                serie VARCHAR(100) NOT NULL UNIQUE,
                seasons INTEGER NOT NULL,
                released_date DATE NOT NULL,
                genre VARCHAR(50) NOT NULL,
                imdb_rating FLOAT(2) NOT NULL
            );
        """)
    conn.commit()
    return conn

