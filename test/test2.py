import json

data = open('data.txt','r')

tmp = json.dumps(json.loads(data), indent=4,sort_keys=False,ensure_ascii=False)
print(tmp)