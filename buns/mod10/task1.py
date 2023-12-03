import requests
import json

starship_req = requests.get('https://swapi.dev/api/starships/10')
data = json.loads(starship_req.text)

pilots = []
for pilot in data['pilots']:
    pilot_info_all = json.loads(requests.get(pilot).text)

    pilot_info = {'name': pilot_info_all['name'],
                  'height': pilot_info_all['height'],
                  'mass': pilot_info_all['mass'],
                  'homeworld': json.loads(requests.get(pilot_info_all['homeworld']).text)['name'],
                  'homeworld_url': pilot_info_all['homeworld']}
    pilots.append(pilot_info)

starship_data = {'ship_name': data['name'],
                 'starship_class': data['starship_class'],
                 'max_atmosphering_speed': data['max_atmosphering_speed'],
                 'pilots': pilots}

with open('millenium_falcon.json', 'w') as file:
    json.dump(starship_data, file, indent=4)

with open('millenium_falcon.json', 'r') as file:
    millenium_falcon_data = json.dumps(starship_data, indent=4)

print(millenium_falcon_data)