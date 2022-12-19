import torch
from torchtext.legacy import data
from torchtext.legacy import vocab
import csv
from sklearn.feature_extraction import DictVectorizer
from config import device
import student
import csv

print("Using device: {}"
      "\n".format(str(device)))
file = open('optimal_ngrams.csv')
optimal_ngrams = csv.reader(file)
rows = []
for row in optimal_ngrams:
    rows.append(int(row[0]))
#print(rows[:1000])
file.close()


# defines datatype textField
textField = data.Field(lower=True, include_lengths=True, batch_first=True,use_vocab=True,
                       tokenize=student.tokenise,
#                       preprocessing=student.preprocessing,
#                       postprocessing=student.postprocessing,
                       stop_words=student.stopWords)

# defines datatype labelField
labelField = data.Field(sequential=False, use_vocab=False, is_target=True)

# this loads all the data
dataset = data.TabularDataset('train.json', 'json',
                              {'reviewText': ('reviewText', textField),
                               'rating': ('rating', labelField),
                               'businessCategory': ('businessCategory', labelField)})

unique_words ={}
for i in range(50000):
    for word in dataset[i].reviewText:
        unique_words[word] = unique_words.get(word, 0) + 1

red_unique_words = {k:v for (k,v) in unique_words.items() if v > 30}
gross_stop_words = {k:v for (k,v) in unique_words.items() if v < 31}

ngram = list(red_unique_words)
print([ngram[i] for i in rows[:10000]])

#print(gross_stop_words.keys())

#unique_zeroed = dict.fromkeys(sorted(red_unique_words, key=red_unique_words.get, reverse=True), 0)
##unique_zeroed = dict.fromkeys(sorted(unique_words, key=unique_words.get, reverse=True), 0)
#f = open('reviews_ngrams.txt', 'wb')
#writer = csv.writer(f)

##write the review data, in the form of ngrams, to file
#for i in range(50000):
#    dict_line = dict(unique_zeroed) #creates an empty dictionary, with correct ngram keys, but zeros for values
#    for word in dataset[i].reviewText:  #goes through each review, and if possible, adds each ngram
#        if word in unique_zeroed:
#            dict_line[word] +=1
#    data_line = bytearray(list(dict_line.values())) #creates line of data to be written to file
##    print(list(dict_line.values())[0:10])
##    print(dict_line.keys())
#    f.write(data_line)
#    if (i % 1000 == 0):
#        print(i)
#f.close()
#print(len(unique_words))
#print(len(red_unique_words))






