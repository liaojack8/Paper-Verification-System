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
res = collection.insert(template)
print(res)