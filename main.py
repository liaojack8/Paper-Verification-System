#!/usr/bin/python
# -*- coding: utf-8 -*-
import pdfAnalyser
import hashGen
debug = True

filePath = 'a.pdf'
splitSentence = pdfAnalyser.Analyser(filePath)
total_list = hashGen.hashGenerate(filePath, splitSentence)
hashNums = len(total_list[0])
HashList = total_list[0]
allHash = total_list[1]
if debug:print('Hash Nums (Sentence Nums):\n', hashNums)
if debug:print(hashNums, 'list:\n', HashList)
if debug:print('CombHash:\n', allHash)