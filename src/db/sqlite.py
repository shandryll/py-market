import os
import sqlite3


def create_database(database_name: str) -> None:
    """."""
    conn = sqlite3.connect(database_name)
    print(f"Opened {database_name} database successfully.")

    conn.execute("""CREATE TABLE IF NOT EXISTS 'products'
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL)
    """)
    print("Table created successfully.")

    conn.close()


def delete_database(database_name: str) -> None:
    """."""
    try:
        os.remove(database_name)
        print(f"Database '{database_name}' successfully removed.")
    except FileNotFoundError:
        print(f"Database '{database_name}' not found.")
    except Exception as e:
        print(f"Error removing database: {e}")


create_database("storage.db")
