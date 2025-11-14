from email.quoprimime import header_decode

import pandas as pd
import sqlite3
from tabulate import tabulate


def load():
    # Loading CSVs into DataFrames
    poke_df = pd.read_csv("Poke_list.csv")
    ability_df = pd.read_csv("Ability_list.csv")
    stat_df = pd.read_csv("Stat_list.csv")

    # Connecting to SQLite DB (creates file if not exists)
    conn = sqlite3.connect("poke_db.db")

    # Writing DataFrames to SQLite tables
    poke_df.to_sql("pokemon", conn, if_exists="replace", index=False)
    ability_df.to_sql("abilities", conn, if_exists="replace", index=False)
    stat_df.to_sql("stats", conn, if_exists="replace", index=False)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS combined AS 
    
    SELECT p.id AS ID,
            p.name AS pokemon_name,
            p.height AS pokemon_height_inchs,
            p.weight AS pokemon_weight_lbs,
            a.ability_name AS ability_name, 
            s.base_stat AS base_stat, 
            s.stat_name AS stat_name
        FROM pokemon AS p INNER JOIN abilities AS a ON p.id = a.id AND p.name = a.name
        INNER JOIN stats AS s ON p.id = s.id AND p.name = s.name;
    """)



    output_df = pd.read_sql("SELECT * FROM combined", conn)

    output_df.to_csv("final.csv")

    print(tabulate(output_df, headers="keys",tablefmt="psql", showindex=False))

    conn.close()




