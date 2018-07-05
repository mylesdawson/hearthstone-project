import requests
import json

# Not well documented api....fkin hell
valid_sets = ['The Grand Tournament', 'Goblins vs Gnomes', 'Blackrock Mountain', 'The League of Explorers', 'Whispers of the Old Gods', 'Kobolds & Catacombs', 'The Witchwood', "Journey to Un'Goro", 'Mean Streets of Gadgetzan', 'Naxxramas', 'One Night in Karazhan', 'Goblins vs Gnomes', 'Basic', 'Classic', 'Knights of the Frozen Throne',  ]

headers = { 'X-Mashape-Key': 'P5bBTHueMlmshzOOP2U2DwwtvJRgp1zrMbfjsnORZtXnhg0I8P' }
r = requests.get('https://omgvamp-hearthstone-v1.p.mashape.com/cards?collectible=1', headers=headers)

r = json.loads(r.text)

# Discarding useless info like missions, credits and debug cards
data = {}
for key, value in r.items():
    if key in valid_sets:
        data[key] = value

cards = open('cards.json', 'w')

# Writing to json file in lines format
for key, value in r.items():
    for item in r[key]:
        json.dump(item, cards)
        cards.write('\n')

cards.close()
