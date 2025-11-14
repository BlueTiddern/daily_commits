import pandas as pd
import requests
from tabulate import tabulate

url = 'https://pokeapi.co/api/v2/pokemon/'

poke_list = ['dratini','raichu','moltres','articuno','zapdos']
resp_list = []
updated_resp_list = []
required_keys = ["id","name","height","weight","abilities","stats"]
for poke in poke_list:
    response = requests.get(url+poke).json()
    resp_list.append(response)

for each in resp_list:
    selective_dict = {k : each.get(k) for k in required_keys}
    updated_resp_list.append(selective_dict)


print(updated_resp_list[0])








