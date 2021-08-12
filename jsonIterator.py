import json
f=open('hosts.json')
data=json.load(f)
f.close()
f=open('request.json')
requests=json.load(f)
input='GAP'
for p in data['TLAS']:
    if(p['Customers']==input):
        newVal=(p['ENVS'])
requests['params']["hostids"]=newVal


with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(requests, f, ensure_ascii=False, indent=4)