#!/usr/bin/python
# -*- coding: utf-8 -*-
import PyPDF2
import hashlib
import regularExpression as RE
debug = False

def Analyser(filePath):
    file = open(filePath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(file)
    numberOfPages = pdfReader.getNumPages()
    if debug:print('[Analyser()] Pages:', numberOfPages)
    allData = []
    for page in range(numberOfPages):
        pageObj = pdfReader.getPage(page)
        page_content = pageObj.extractText()
        if debug:print('[Analyser()] Page ',page, 'content:\n',page_content)
        normal_content = RE.splitIntoSentences(page_content)
        for i in range(len(normal_content)):
            allData.append(normal_content[i])
    file.close()
    if debug:print([Analyser()], allData)
    return allData