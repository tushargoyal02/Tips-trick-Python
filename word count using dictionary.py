import pprint

#counting each letter in string

message ='hey bella how are you ?'

wordCount = {}

for i in message:
    wordCount.setdefault(i,0)

    wordCount[i] = wordCount[i] + 1

# print(wordCount)

# pprint is used to show list or dictionary in nicer manner

pprint.pprint(wordCount)