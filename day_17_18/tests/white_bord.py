
import pandas as pd
from tabulate import tabulate

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

example = {'id': 147, 'name': 'dratini', 'height': 18, 'weight': 33, 'abilities': [{'ability': {'name': 'shed-skin', 'url': 'https://pokeapi.co/api/v2/ability/61/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'marvel-scale', 'url': 'https://pokeapi.co/api/v2/ability/63/'}, 'is_hidden': True, 'slot': 3}], 'stats': [{'base_stat': 41, 'effort': 0, 'stat': {'name': 'hp', 'url': 'https://pokeapi.co/api/v2/stat/1/'}}, {'base_stat': 64, 'effort': 1, 'stat': {'name': 'attack', 'url': 'https://pokeapi.co/api/v2/stat/2/'}}, {'base_stat': 45, 'effort': 0, 'stat': {'name': 'defense', 'url': 'https://pokeapi.co/api/v2/stat/3/'}}, {'base_stat': 50, 'effort': 0, 'stat': {'name': 'special-attack', 'url': 'https://pokeapi.co/api/v2/stat/4/'}}, {'base_stat': 50, 'effort': 0, 'stat': {'name': 'special-defense', 'url': 'https://pokeapi.co/api/v2/stat/5/'}}, {'base_stat': 50, 'effort': 0, 'stat': {'name': 'speed', 'url': 'https://pokeapi.co/api/v2/stat/6/'}}]}

raw_df = pd.DataFrame([example])

test_df = pd.json_normalize(example).drop(["abilities","stats"],axis=1)

ability_df = pd.json_normalize(example, record_path='abilities', meta=['id','name'],sep='_').drop(["is_hidden","ability_url"], axis=1)
stat_df = pd.json_normalize(example, record_path='stats', meta=['id','name'],sep='_').drop(["effort","stat_url"], axis=1)

print(tabulate(test_df,headers="keys",tablefmt="psql",showindex=False))

print(tabulate(ability_df,headers="keys",tablefmt="psql",showindex=False))

print(tabulate(stat_df,headers="keys",tablefmt="psql",showindex=False))

merge_df = test_df.merge(ability_df,how='inner',on=['id','name'])
merge_df = merge_df.merge(stat_df,how='inner',on= ['id','name'])

print(tabulate(merge_df,headers="keys",tablefmt="psql",showindex=False))