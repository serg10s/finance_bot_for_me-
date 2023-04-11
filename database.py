import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


class Finance:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("Host"),
            user=os.getenv("User"),
            password=os.getenv("Password"),
            database=os.getenv("Database")
        )
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS Expenses (
                id SERIAL PRIMARY KEY,
                user_id INTEGER,
                food VARCHAR (50),
                entertainment VARCHAR (50),
                transportation VARCHAR (50),
                other VARCHAR (50)
            )
        ''')

        self.conn.commit()
        print("[INFO] Tables created successfully")

    def add_food(self, food, user_id):
        sql = "INSERT INTO Expenses (food, user_id) VALUES (%s, %s)"
        values = (food, user_id)
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with food {food}, added to database")

    def add_entertainment(self, entertainment, user_id):
        sql = "INSERT INTO Expenses (entertainment, user_id) VALUES (%s, %s)"
        values = (entertainment, user_id)
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with entertainment {entertainment}, add to database")

    def add_transportation(self, transportation, user_id):
        sql = "INSERT INTO Expenses (transportation, user_id) VALUES (%s, %s)"
        values = (transportation, user_id)
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with entertainment {transportation}, add to database")

    def add_other(self, other, user_id):
        sql = "INSERT INTO Expenses (other, user_id) VALUES (%s, %s)"
        values = (other, user_id)
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with entertainment {other}, add to database")

    def get_food(self, user_id):
        self.cur.execute("SELECT SUM(CAST(food AS INTEGER)) FROM Expenses WHERE user_id = %s", (user_id,))
        rows = self.cur.fetchone()
        return rows[0]

    def get_entertainment(self, user_id):
        self.cur.execute("SELECT SUM(CAST(entertainment AS INTEGER)) FROM Expenses WHERE user_id = %s", (user_id,))
        rows = self.cur.fetchone()
        return rows[0]

    def get_transportation(self, user_id):
        self.cur.execute("SELECT SUM(CAST(transportation AS INTEGER)) FROM Expenses WHERE user_id = %s", (user_id,))
        rows = self.cur.fetchone()
        return rows[0]

    def get_other(self, user_id):
        self.cur.execute("SELECT SUM(CAST(other AS INTEGER)) FROM Expenses WHERE user_id = %s", (user_id,))
        rows = self.cur.fetchone()
        return rows[0]

    def get_all_expenses(self, user_id):
        self.cur.execute("SELECT SUM(CAST(food AS INTEGER)) + SUM(CAST(other AS INTEGER)) + SUM(CAST(transportation AS INTEGER)) + SUM(CAST(entertainment AS INTEGER)) FROM Expenses WHERE user_id = %s", (user_id,))
        rows = self.cur.fetchone()
        return rows[0]

    def get_user_id(self):
        self.cur.execute("SELECT user_id FROM Expenses")
        rows = self.cur.fetchone()
        return rows[0]

    def close_connection(self):
        self.cur.close()
        self.conn.close()
        print("[INFO] PostgreSQL connection closed")
