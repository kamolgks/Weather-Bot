import sqlite3

class Database:
    def __init__(self, db_path='database/data.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                nickname TEXT,
                city TEXT
            )
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()

    def add_user(self, user_id, username, nickname):
        self.cursor.execute(
            "INSERT OR IGNORE INTO users (user_id, username, nickname) VALUES (?, ?, ?)",
            (user_id, username, nickname)
        )
        self.conn.commit()

    def update_user_city(self, user_id, city):
        self.cursor.execute(
            "UPDATE users SET city = ? WHERE user_id = ?",
            (city, user_id)
        )
        self.conn.commit()

    def get_user_city(self, user_id):
        self.cursor.execute(
            "SELECT city FROM users WHERE user_id = ?",
            (user_id,)
        )
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def get_user_by_id(self, user_id):
        self.cursor.execute(
            "SELECT * FROM users WHERE user_id = ?",
            (user_id,)
        )
        return self.cursor.fetchone()
