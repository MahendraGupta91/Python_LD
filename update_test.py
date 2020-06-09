import json
import re
dict1={"a":"aaaa","b":"bbbb"}
dict2={"c":"ccc"}
dict1.update(dict2)
print(dict1)
#def update_Words(newWords):
#        with open('.json') as dict_reader:
#                oldWords=json.load(dict_reader)
#            print(oldWords)
#            print("File opened")
#            print(newWords)
#            oldWords=oldWords.update(newWords)
#            print("Dict Updated  values after update ")
#            print(oldWords)
#                   
#        with open('Hindi_English_words_12Apr.json', 'w') as dict_writer:
#            json.dump(oldWords,dict_writer)
#            print("Dictionary written")
f = open("english13.text", "r")
#for i in range(20):
word_text=f.read()
word_text=re.split("\n",word_text)
print(len(word_text))
def update_Words(newWords):
        with open('Hindi_English_words_12Apr.json') as dict_reader:
            oldWords=json.load(dict_reader)
            print(word_text[7720])
            print(len(oldWords))
            print(oldWords[word_text[3940]]["En"])
            print(oldWords[word_text[3940]]["Hi"])
update_Words(dict1)
total=0
with open('Hindi_English_words_12Apr.json') as dict_reader:
            oldWords=json.load(dict_reader)
            for a in oldWords.keys():
                if oldWords[a]["Hi"]!="NA":
                    total=total+1
print(total)