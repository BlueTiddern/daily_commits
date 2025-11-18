import json

def json_load() -> dict:

    with open("straw_hats.json", "r") as f:
        data = json.load(f)

    print(f"The available keys for the dict are : {data['straw_hat_crew'][0].keys()}")

    if "Monkey D. Luffy" in data['straw_hat_crew'][0].values():
        print(f"""
                    
                The captain of the crew is : {data['straw_hat_crew'][0]['name']}
                Bounty on his head : {data['straw_hat_crew'][0]['bounty']}
                His ambition is : {data['straw_hat_crew'][0]['dream']}

                    """)
    return data

def json_write(data : dict):

    print("""    **...adding new key values\n   ->Devil fruit powers...\n""")
    data['straw_hat_crew'][0]['Devil_fruit_power'] = "Zoan Type Nika"
    data['straw_hat_crew'][5]['Devil_fruit_power'] = "Human Human"
    data['straw_hat_crew'][6]['Devil_fruit_power'] = "Flower Flower"
    data['straw_hat_crew'][8]['Devil_fruit_power'] = "Soul Soul"

    with open('New_straws.json', 'w') as f:
        json.dump(data,f,indent=4)


if __name__ == '__main__':
    data = json_load()
    json_write(data)


