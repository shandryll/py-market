import sqlite3


def create_database() -> None:
    """."""
    conn = sqlite3.connect("storage.db")
    print('Opened "storage" database successfully.')

    conn.execute("""CREATE TABLE IF NOT EXISTS 'products'
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL)
    """)
    print("Table created successfully.")

    conn.close()


create_database()
