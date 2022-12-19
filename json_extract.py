from extract import json_extract

names = json_extract(r.json(), 'conversations')

print(names)
