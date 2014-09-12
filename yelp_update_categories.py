import json
from py2neo import neo4j

db = neo4j.GraphDatabaseService("http://192.241.222.136:7474/db/data/")

merge_category_query = '''
MATCH (b:Business {business_id: {business_id}})
MERGE (c:Category {name: {category}})
CREATE UNIQUE (c)<-[:IS_IN]-(b)
'''

print "Beginning category batch"
with open('data/yelp_academic_dataset_business.json', 'r') as f:
	category_batch = neo4j.WriteBatch(db)
	count = 0
	for b in (json.loads(l) for l in f):
		for c in b['categories']:
			category_batch.append_cypher(merge_category_query, {'business_id': b['business_id'], 'category': c})
			count += 1
			if count >= 10000:
				category_batch.run()
				category_batch.clear()
				print "Running batch"
				count = 0
	if count > 0:
		category_batch.run()