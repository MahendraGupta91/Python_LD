# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:03:41 2020

@author: Mahendra
"""
import json
global newWords
newWords={'with':'used to say that people or things are in a place together or are doing something together'}
def update_Words(newWords):
    print("Update_Word Called")
    #newWords={'ahahah':'jajajajajajajaj'}
    print(newWords)
    with open('dictionary_words.json') as dict_reader:
        print("Dictionary is red..............0")
        #print(json.load(dict_reader))
        print('......................1')
        oldWords=json.load(dict_reader)
        print('......................2')
        oldWords.update(newWords)
        print(oldWords)
    with open('dictionary_words.json', 'w') as dict_writer:
        json.dump(oldWords, dict_writer)
        print("Dictionary is written")
        newWords={}
update_Words(newWords)