import sqlite3

def init_db(path="songs.db"):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS songs USING fts5(
        author,
        title,
        lyrics,
        url
    );
    """)

    conn.commit()
    conn.close()

init_db("dat.db")
