import pymongo
import time
import hashlib
Client = pymongo.MongoClient("mongodb://localhost:27017/")
DB = Client["BPSS"]
collection = DB['paper']
template = {
	'title': 'ABCTitle',
	'numOfSentence': 12345,
	'pdfHash': 'ABCHash',
	'allList': ['A','B','C'],
	'combHash:': 'ABCCombHash',
	'timestamp': time.time()
	}
# result = collection.insert(template)
# print(result)
# for x in collection.find({}):
# 	print(x['title'])

# L1 = ['a','b','c','d','1','2','3','4']
# L2 = ['a','2','3','4']
# print(type(len(set(L1)&set(L2))))
# print(len(set(L1)&set(L2)))
file = "a.pdf" # Location of the file (can be set a different way)
BLOCK_SIZE = 65536 # The size of each read from the file

file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
with open(file, 'rb') as f: # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    while len(fb) > 0: # While there is still data being read from the file
        file_hash.update(fb) # Update the hash
        fb = f.read(BLOCK_SIZE) # Read the next block from the file

print (file,file_hash.hexdigest()) # Get the hexadecimal digest of the hash