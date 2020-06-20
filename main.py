#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Response
import pdfAnalyser
import hashGen
import pymongo
import hashlib
import base64
import time
debug = False
threshold = 0.3
if debug:filePath = 'a.pdf'
Client = pymongo.MongoClient("mongodb://localhost:27017/")
DB = Client["BPSS"]
collection = DB['paper']
pdfHash = ''

def getHash(filePath):
	splitSentence = pdfAnalyser.Analyser(filePath)
	total_list = hashGen.hashGenerate(filePath, splitSentence)
	hashNums = len(total_list[0])
	HashList = total_list[0]
	allHash = total_list[1]
	if debug:
		print('[getHash()] Hash Nums (Sentence Nums):\n', len(total_list[0]))
		print('[getHash()] ', len(total_list[0]), 'list:\n', total_list[0])
		print('[getHash()] CombHash:\n', total_list[1])
	return total_list

def fileHash(filePath):
	file = filePath # Location of the file (can be set a different way)
	BLOCK_SIZE = 65536 # The size of each read from the file
	file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
	with open(file, 'rb') as f: # Open the file to read it's bytes
		fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
		while len(fb) > 0: # While there is still data being read from the file
			file_hash.update(fb) # Update the hash
			fb = f.read(BLOCK_SIZE) # Read the next block from the file
	return file_hash.hexdigest()

def checkExist(pdfHash):
	content_pointer = collection.find_one({'pdfHash': pdfHash})
	if debug:print('[checkExist()] ', content_pointer)
	if content_pointer == None: # not exist
		if debug:print("[checkExist()] pdfHash doesn't exist!")
		return True
	else:
		if debug:print("[checkExist()] pdfHash already exist!")
		return False

def checkPlagiarism(TList):
	for x in collection.find({}):
		if debug:print("[checkPlagiarism()] ", x['_id'], x['title'], x['timestamp'])
		plagiarismPercentage = len(set(TList[0])&set(x['allList'])) / len(TList[0])
		if debug:print("[checkPlagiarism()] ", plagiarismPercentage)
		if plagiarismPercentage >= threshold:
			return False
		else:
			return True

def upload(title, pdfHash, TList, ts):
	collection = DB['paper']
	uploadData = {
	'title': title,
	'numOfSentence': len(TList[0]),
	'pdfHash': pdfHash,
	'allList': TList[0],
	'combHash:': TList[1],
	'timestamp': ts
	}
	return collection.insert(uploadData)

def flask_func(title, content, timestamp = time.time()):
	receivePdf = open('./bin/temp.fdp', 'bw')
	receivePdf.write(base64.b64decode(content))
	receivePdf.close()
	TList = getHash('./bin/temp.fdp')
	pdfHash = fileHash('./bin/temp.fdp')
	if checkExist(pdfHash):
		if checkPlagiarism(TList):
			res = upload(title, pdfHash, TList, timestamp)
			if debug: print('[checkPlagiarism()] Obj_Id@Mongo:', res)
			if debug: print('[checkPlagiarism()] status: Sent')
			return Response(
				str('Sent'),
				status=200
			)
	else:
		if debug:print('[checkPlagiarism()] status: This paper has been submitted before.')
		return Response(
			'This paper has been submitted before.',
			status=200
		)