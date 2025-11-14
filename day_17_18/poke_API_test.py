import pandas as pd
import requests
from tabulate import tabulate

url = 'https://pokeapi.co/api/v2/pokemon/rhydon'

response = requests.get(url).json()

stat_df = pd.DataFrame(response['stats'])

stats_normalize = pd.json_normalize(response['stats'])

stats_normalize = stats_normalize.rename(columns={'stat.name' : 'state_name'}).drop(columns=["stat.url"])

print(tabulate(stat_df, headers="keys", tablefmt="psql", showindex=False))

print(tabulate(stats_normalize, headers="keys", tablefmt="psql", showindex=False))

print("\n")

print(type(response))


