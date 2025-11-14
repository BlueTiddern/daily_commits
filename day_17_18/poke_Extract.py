import pandas as pd
import requests
from tabulate import tabulate
import json
from dotenv import load_dotenv
import os

load_dotenv()
env_url = os.getenv("API_URL")

def extract():
    url = env_url

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


    with open(r"data\poke.JSON", 'w') as f:
        json.dump(updated_resp_list, f, indent=4)

extract()








