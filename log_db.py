import sqlite3

LOG_DB = "logs_db.db"


with sqlite3.connect(LOG_DB) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS logs (
      d integer PRIMARY KEY,
        key_pressed integer NOT NULL,
        coordinate_x integer NOT NULL,
        coordinate_y integer NOT NULL,
        action_description TEXT
    );"""  
    sqlite_conn.execute(sql_request)


def clean_table():
    with sqlite3.connect(LOG_DB) as sqlite_conn:
        # Очистити таблицю
        clear_query = "DELETE FROM logs;"
        sqlite_conn.execute(clear_query)


