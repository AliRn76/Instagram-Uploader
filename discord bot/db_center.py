import sqlite3

con = sqlite3.connect("ImagineDB.db")
cur = con.cursor()


def add(content: tuple) -> bool:
    cur.execute(
        "INSERT INTO Content(id, path, watermark) VALUES(?,?,?,?)", content)
    if con.commit():
        return True
    else:
        return False
