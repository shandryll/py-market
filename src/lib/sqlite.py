import os
import sqlite3
from sqlite3 import Connection as SqliteConnection


class SqliteConnectionHandler:
    def __init__(self, connection_string: str = "storage.db") -> None:
        self.__connection_string = connection_string
        self.__conn = None

    def connect(self) -> SqliteConnection:
        """."""
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        self.__conn = conn
        return conn

    def get_connection(self) -> SqliteConnection:
        """."""
        return self.__conn


def create_database(database_name: str) -> None:
    """."""
    conn = sqlite3.connect(database_name)

    conn.execute("""CREATE TABLE IF NOT EXISTS 'products'
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL)
    """)

    conn.close()


def delete_database(database_name: str) -> None:
    """."""
    try:
        os.remove(database_name)
    except FileNotFoundError:
        print(f"Database '{database_name}' not found.")
    except Exception as e:
        print(f"Error removing database: {e}")
