import sqlite3
import pandas as pd
from tabulate import tabulate


class DataBase:
    def __init__(self,db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE);
        """)

    def data_load(self,data):
        for r in data:
            self.conn.execute(f"""
            INSERT INTO users VALUES({r[0]},'{r[1]}','{r[2]}');
            """)

    def data_print(self):
        data_df = pd.read_sql("SELECT * FROM users",self.conn)
        return tabulate(data_df,headers='keys',tablefmt='psql',showindex=False)


def main():
    data_arr = [[1,"JU","JU@gmail.com"],[2,"XU","XU@gmail.com"],[3,"ZU","ZU@gmail.com"]]
    db = DataBase("taskDB")
    db.data_load(data_arr)
    print(db.data_print())

if __name__ == "__main__":
    main()




