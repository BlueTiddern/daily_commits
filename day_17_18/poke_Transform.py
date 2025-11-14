import pandas as pd
import json
from tabulate import tabulate

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

def transform():
    with open("poke.JSON", 'r') as f:
        data = json.load(f)


    # Pokemon List : Dimension Pokemon

    raw_df = pd.DataFrame(data).drop(['abilities','stats'],axis=1)

    raw_df.to_csv('Poke_list.csv')

    print(tabulate(raw_df, headers="keys", tablefmt= 'psql', showindex=False))

    # Ability List : Dimension

    ability_df = pd.json_normalize(data, record_path='abilities', meta=['id','name'], sep='_').drop(['is_hidden','ability_url'], axis=1)

    ability_df.to_csv('Ability_list.csv')

    print(tabulate(ability_df, headers="keys", tablefmt= 'psql', showindex=False))

    # Stats list : Dimension

    stat_df = pd.json_normalize(data, record_path='stats', meta=['id','name'],sep='_').drop(["effort","stat_url"], axis=1)

    stat_df.to_csv('Stat_list.csv')

    print(tabulate(stat_df, headers="keys", tablefmt= 'psql', showindex=False))