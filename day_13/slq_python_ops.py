#imports

import sqlite3
import pandas as pd
from tabulate import tabulate


## code block creates table 1:
# -----------------------------------------------------------------------

conn = sqlite3.connect('opsBD')

conn.execute("DROP TABLE cust;")

conn.execute("""

CREATE TABLE IF NOT EXISTS cust (

id INTEGER PRIMARY KEY,
affinity VARCHAR(15),
name VARCHAR(50),
age INTEGER,
salary INTEGER

);

""")

conn.execute("""

INSERT INTO cust VALUES(1,'Intelligence','Invoker',20, 200000),(2,'Strength','Pudge',55,300000),(3,'Agility','Jugg',38,900000),(4,'Agility','Morph',99,1000000);

""")

#conn.execute("""SELECT * FROM cust""")

cust_df = pd.read_sql("SELECT * FROM cust",conn)

print("\n#########################\nCreating the table 1.....\n#########################\n\nThe created table has the following value\n",tabulate(cust_df,headers='keys',tablefmt='psql',showindex=False))
# -----------------------------------------------------------------------

## code block creates table 2:
# -----------------------------------------------------------------------

conn.execute("""

             CREATE TABLE IF NOT EXISTS types (

                 type_id VARCHAR(10) PRIMARY KEY,
                 primary_boost VARCHAR(20),
                 type_color VARCHAR(20),
                 suggested_item VARCHAR(20)

                 );

             """)

conn.execute("""

             INSERT INTO types VALUES('Intelligence','Mana','Blue','Archane staff'),('Agility','Attack Speed','Green','Butterfly'),('Strength','Health','Red','Heart of Turrask');

             """)

#conn.execute("""SELECT * FROM cust""")

types_pd = pd.read_sql("SELECT * FROM types",conn)

print("\n#########################\nCreating the table 2.....\n#########################\n\nThe created table has the following value\n",tabulate(types_pd,headers='keys',tablefmt='psql',showindex=False))
# -----------------------------------------------------------------------


## code block for filtering
# -----------------------------------------------------------------------
print()
where_pd = pd.read_sql("SELECT affinity,name,age,salary FROM cust WHERE age > 20",conn)
print("\n#########################\nApplying WHERE filter....\n#########################\n\nThe filtered Age values are\n",tabulate(where_pd,headers='keys',tablefmt='psql',showindex=False))
# -----------------------------------------------------------------------

## code block for ordering the table
# -----------------------------------------------------------------------
print()
order_pd = pd.read_sql("SELECT affinity,name,age,salary FROM cust ORDER BY age DESC",conn)
print("\n#########################\nOrdering on age -> DESC..\n#########################\n\nThe sorted Age values are\n",tabulate(order_pd,headers='keys',tablefmt='psql',showindex=False))
# -----------------------------------------------------------------------

## code block for limiting the result
# -----------------------------------------------------------------------
print()
limit_pd = pd.read_sql("SELECT affinity,name,age,salary FROM cust ORDER BY age DESC LIMIT 2",conn)
print("\n#########################\nLIMIT(ing) the result....\n#########################\n\nResult limitted to 2\n",tabulate(limit_pd,headers='keys',tablefmt='psql',showindex=False))
# -----------------------------------------------------------------------

## code block for limiting the result
# -----------------------------------------------------------------------
print()
join_pd = pd.read_sql("""

WITH cte AS (

SELECT 
    c.name as Hero_name,
    c.affinity as Hero_affinity,
    c.age as Hero_age,
    c.salary as Hero_gold,
    t.primary_boost as Hero_strong_point,
    t.suggested_item as Buy_this
FROM cust as c JOIN types as t ON c.affinity = t.type_id
)

SELECT
    ROW_NUMBER() OVER(ORDER BY Hero_gold) AS Hero_id, *
FROM cte;
    
""",conn)
print("\n#########################\nJoining the tables....\n#########################\n\nResult of JOIN\n",tabulate(join_pd,headers='keys',tablefmt='psql',showindex=False))
# -----------------------------------------------------------------------
