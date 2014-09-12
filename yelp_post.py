import json
import requests

url = "http://192.241.222.136:7474/scdemo/scdemo/node"
headers = {'Content-type': 'application/json'}
count = 0

with open('data/yelp_academic_dataset_business.json', 'r') as f:
	for b in (json.loads(l) for l in f):
		data = {
			'name': b['name'],
			'business_id': b['business_id'],
			'lat': b['latitude'],
			'lon': b['longitude'],
			'addresss': b['full_address']
		}
		count = count + 1
		print count
		if count > 36395:
			r = requests.post(url, data=json.dumps(data), headers=headers)
			print r
