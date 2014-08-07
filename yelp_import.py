import json
from py2neo.neo4j import CypherQuery, GraphDatabaseService, WriteBatch
from py2neo import neo4j

db = neo4j.GraphDatabaseService()

business_index_query = CypherQuery(db, "CREATE INDEX ON :Business(id)")
business_index_query.execute()

create_business_query = '''
// MERGE ON categories
CREATE (b:Business)
'''