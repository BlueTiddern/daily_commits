import pandas as pd
from tabulate import tabulate
import sqlite3

conn = sqlite3.connect('opsBD')

data_df = pd.read_sql("SELECT * FROM cust;",conn)

print("\n############################\nThe loaded pandas df from DB\n############################\n")
print(tabulate(data_df,headers='keys',tablefmt='psql',showindex=False))


print("\nAdding a new row to Update and Delete later......\n")

conn.execute("INSERT INTO cust VALUES (5,'Intelligence','Puck',17,440000)")

print("\nNew Records added....\n")
print("\n############################\nThe loaded pandas df from DB\n############################\n")

new_data_df = pd.read_sql("SELECT * FROM cust;",conn)
print(tabulate(new_data_df,headers='keys',tablefmt='psql',showindex=False))

print("\nUpdating the new record......\n")
conn.execute("UPDATE cust SET age = 20 WHERE id = 5;")

print("\nUpdated the Record.....\n")
print("\n############################\nThe loaded pandas df from DB\n############################\n")
up_df = pd.read_sql("SELECT * FROM cust WHERE id = 5;",conn)
print(tabulate(up_df,headers='keys',tablefmt='psql',showindex=False))

print("\nDeleting the record added.....\n")

conn.execute("DELETE FROM cust WHERE id = 5;")

print("\nRecord DELETED.....\n")

final_df = pd.read_sql("SELECT * FROM cust;",conn)
print("\n############################\nThe loaded pandas df from DB\n############################\n")
print(tabulate(final_df,headers="keys",tablefmt="psql",showindex=False))

