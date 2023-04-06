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
                user_id SERIAL PRIMARY KEY,
                food VARCHAR (50),
                entertainment VARCHAR (50),
                transportation VARCHAR (50),
                other VARCHAR (50)
            )
        ''')
        self.conn.commit()
        print("[INFO] Tables created successfully")

    def add_food(self, food):
        sql = "INSERT INTO Expenses (food) VALUES (%s)"
        values = (food, )
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with food {food}, added to database")

    def add_entertainment(self, entertainment):
        sql = "INSERT INTO Expenses (entertainment) VALUES (%s)"
        values = (entertainment, )
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with entertainment {entertainment}, add to database")

    def add_transportation(self, transportation):
        sql = "INSERT INTO Expenses (transportation) VALUES (%s)"
        values = (transportation, )
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with entertainment {transportation}, add to database")

    def add_other(self, other):
        sql = "INSERT INTO Expenses (other) VALUES (%s)"
        values = (other, )
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with entertainment {other}, add to database")

    def get_cursor(self):
        return self.cur

    def get_food(self):
        self.cur.execute("SELECT SUM(CAST(food AS INTEGER)) FROM Expenses;")
        rows = self.cur.fetchone()
        return rows[0]

    def get_entertainment(self):
        self.cur.execute("SELECT SUM(CAST(entertainment AS INTEGER)) FROM Expenses;")
        rows = self.cur.fetchone()
        return rows[0]

    def get_transportation(self):
        self.cur.execute("SELECT SUM(CAST(transportation AS INTEGER)) FROM Expenses;")
        rows = self.cur.fetchone()
        return rows[0]

    def get_other(self):
        self.cur.execute("SELECT SUM(CAST(other AS INTEGER)) FROM Expenses;")
        rows = self.cur.fetchone()
        return rows[0]

    def get_all_expenses(self):
        self.cur.execute("SELECT SUM(CAST(food AS INTEGER)) + SUM(CAST(other AS INTEGER)) + SUM(CAST(transportation AS INTEGER)) + SUM(CAST(entertainment AS INTEGER)) FROM Expenses;")
        rows = self.cur.fetchone()
        return rows[0]

    def close_connection(self):
        self.cur.close()
        self.conn.close()
        print("[INFO] PostgreSQL connection closed")
