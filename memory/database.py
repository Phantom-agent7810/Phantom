import sqlite3


class Database:
    def __init__(self, db_name="phantom.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)

        self.connection.commit()

    def close(self):
        self.connection.close()
