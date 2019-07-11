# while :; do :; done (use to test 100% cpu core load for at most one of the 6 cores):w

import json

with open('data.json', 'r') as fp:
        obj = json.load(fp)

Core1 = obj['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value']
Core2 = obj['Children'][0]['Children'][1]['Children'][0]['Children'][1]['Value']
Core3 = obj['Children'][0]['Children'][1]['Children'][0]['Children'][2]['Value']
Core4 = obj['Children'][0]['Children'][1]['Children'][0]['Children'][3]['Value']
Core5 = obj['Children'][0]['Children'][1]['Children'][0]['Children'][4]['Value']
Core6 = obj['Children'][0]['Children'][1]['Children'][0]['Children'][5]['Value']

print(Core1 + "\n")
print(Core2 + "\n")
print(Core3 + "\n")
print(Core4 + "\n")
print(Core5 + "\n")
print(Core6 + "\n")




