import json
f=open('jsonDirs/hosts.json')
data=json.load(f)
f.close()
f=open('jsonDirs/request.json')
requests=json.load(f)
input='SAS'
for p in data['TLAS']:
    if(p['Customers']==input):
        newVal=(p['ENVS'])
requests['params']["hostids"]=newVal


with open('jsonDirs/output.json', 'w', encoding='utf-8') as f:
    json.dump(requests, f, ensure_ascii=False, indent=4)
