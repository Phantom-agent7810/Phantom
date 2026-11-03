from memory.database import Database


class MemoryManager:
    def __init__(self):
        self.db = Database()

    def remember(self, key, value):
        self.db.cursor.execute(
            "INSERT OR REPLACE INTO memory (key, value) VALUES (?, ?)",
            (key, value)
        )
        self.db.connection.commit()

    def recall(self, key):
        self.db.cursor.execute(
            "SELECT value FROM memory WHERE key=?",
            (key,)
        )
        result = self.db.cursor.fetchone()

        if result:
            return result[0]

        return None

    def update(self, key, value):
        self.db.cursor.execute(
            "UPDATE memory SET value=? WHERE key=?",
            (value, key)
        )
        self.db.connection.commit()

    def forget(self, key):
        self.db.cursor.execute(
            "DELETE FROM memory WHERE key=?",
            (key,)
        )
        self.db.connection.commit()
