import json
from py2neo.neo4j import CypherQuery, GraphDatabaseService, WriteBatch
from py2neo import neo4j

db = neo4j.GraphDatabaseService()

business_index_query = CypherQuery(db, "CREATE INDEX ON :Business(id)")
business_index_query.execute()

category_index_query = CypherQuery(db, "CREATE INDEX ON :Category(name)")
category_index_query.execute()

create_business_query = '''
// MERGE ON categories
CREATE (b:Business {id: {business_id}, name: {name}, lat:{latitude}, lon:{longitude},
	stars: {stars}, review_count: {review_count}})
'''

merge_category_query = '''
MATCH (b:Business {id: {business_id}})
MERGE (c:Category {name: {category}})
CREATE UNIQUE (c)<-[:IS_IN]-(b)
'''

print "Beginning business batch"
with open('data/yelp_academic_dataset_business.json', 'r') as f:
	business_batch = WriteBatch(db)
	count = 0
	for b in (json.loads(l) for l in f):
		business_batch.append_cypher(create_business_query, b)
		count += 1
		if count >= 10000:
			business_batch.run()
			business_batch.clear()
			count = 0
	if count > 0:
		business_batch.run()

print "Beginning category batch"
with open('data/yelp_academic_dataset_business.json', 'r') as f:
	category_batch = WriteBatch(db)
	count = 0
	for b in (json.loads(l) for l in f):
		for c in b['categories']:
			category_batch.append_cypher(merge_category_query, {'business_id': b['business_id'], 'category': c})
			count += 1
			if count >= 10000:
				category_batch.run()
				category_batch.clear()
				count = 0
	if count > 0:
		category_batch.run()