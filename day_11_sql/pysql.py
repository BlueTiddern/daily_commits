from sqlalchemy import create_engine,text
import pandas as pd
from tabulate import tabulate


# creating the connection to the active MSSQL server

connection_string = (

    "mssql+pyodbc:///?"
    "odbc_connect=Driver={ODBC Driver 17 for SQL Server};"
    r"Server=3Dx2Y\SQLEXPRESS;"
    "Database=TaskDB;"
    "Trusted_Connection=yes;"

)

engine = create_engine(connection_string)


# running raw sql

with engine.connect() as conn:
    result = conn.execute(text("SELECT TOP 5 * FROM sqltsk.sony"))
    for row in result:
        print(row)

print("-----------------------------------------------------------------")

df = pd.read_sql("SELECT TOP 5 * FROM sqltsk.sony",engine)

print(tabulate(df, headers='keys',tablefmt='psql',showindex=False))