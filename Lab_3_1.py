#Пункт 1
import http.client
import json
conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('GET', '/number/1',)
r1 = conn.getresponse().read().decode()
r1_json = json.loads(r1)
print(r1_json['number'])
#Пункт 2
conn.request('GET', '/number/?option=1',)
r2 = conn.getresponse().read().decode()
r2_json = json.loads(r2)
print(r2)
res = r1_json['number'] * r2_json['number']
print(res)
#Пункт 3
headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/number/', 'option=1', headers)
r3 = conn.getresponse().read().decode()
r3_json = json.loads(r3)
print(r3)
res2 = r3_json['number'] - r2_json['number']
print(res2)
#Пункт 4
headers = {'Content-type': 'application/json'}
conn.request('PUT', '/number/', '{"option":1}', headers)
r4 = conn.getresponse().read().decode()
r4_json = json.loads(r4)
print(r4_json)
res3 = r4_json['number']//r3_json['number']
print(res3)
#Пункт 5
conn.request('DELETE', '/number/', '{"option":1}',)
r5 = conn.getresponse().read().decode()
r5_json = json.loads(r5)
print(r5_json)
res4 = r5_json['number'] + r4_json['number']
print(res4)

