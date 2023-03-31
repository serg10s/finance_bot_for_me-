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
                food DECIMAL(10, 2),
                entertainment DECIMAL(10, 2),
                transportation DECIMAL(10, 2),
                other DECIMAL(10, 2)
            )
        ''')
        self.conn.commit()
        print("[INFO] Tables created successfully")

    def add_food(self, food):
        sql = "INSERT INTO Expenses (food) VALUES (%s)"
        values = (food,)
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with food {food}, add to database")


    def add_entertainment(self, entertainment):
        sql = "INSERT INTO Expenses (entertainment) VALUES (%s)"
        values = (entertainment,)
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with entertainment {entertainment}, add to database")


    def add_transportation(self, transportation):
        sql = "INSERT INTO Expenses (transportation) VALUES (%s)"
        values = (transportation,)
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with entertainment {transportation}, add to database")


    def add_other(self, other):
        sql = "INSERT INTO Expenses (other) VALUES (%s)"
        values = (other,)
        self.cur.execute(sql, values)
        self.conn.commit()
        print(f"Expenses with entertainment {other}, add to database")

    def close_connection(self):
        self.cur.close()
        self.conn.close()
        print("[INFO] PostgreSQL connection closed")
