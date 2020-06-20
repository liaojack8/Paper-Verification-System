import pymongo
import time
Client = pymongo.MongoClient("mongodb://localhost:27017/")
DB = Client["BPSS"]
template = {
	'title': 'ATitle',
	'numOfSentence': 2,
	'pdfHash': 'AHash',
	'allList': ['A', 'B'],
	'combHash:': 'ACombHash',
	'timestamp': time.time()
	}
collection = DB['paper']
collection.insert(template)
DB = Client["BPSS"]
template = {
	'file:': 'xxx',
	'timestamp': time.time()
	}
collection = DB['pdfFile']
collection.insert(template)