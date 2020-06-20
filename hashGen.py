#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
debug = False
def hashGenerate(path, split_txt):
    f = open(path, "r")
    hash_list = []
    content_list = []
    #hash, get plagiarism
    for data in split_txt:
        hash = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
        if debug:print("[hashGenerate()] Sentence: ", data)
        if debug:print("[hashGenerate()] Hash: {}".format(hash))
        content_list.append(data)
        hash_list.append(hash)
    #get allhash combination's hash
    allhash_combination = ''.join(hash_list)
    allhash_combination_hash = hashlib.sha256(str(allhash_combination).encode('utf-8')).hexdigest()
    if debug:print("[hashGenerate()] AllhashComb:", allhash_combination)
    if debug:print("[hashGenerate()] Hash:", allhash_combination_hash)
    f.close()
    data_list = []
    data_list.append(hash_list)
    data_list.append(allhash_combination_hash)
    return data_list