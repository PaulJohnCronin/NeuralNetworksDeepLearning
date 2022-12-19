import torch
from torchtext.legacy import data
from torchtext.legacy import vocab
import csv
from sklearn.feature_extraction import DictVectorizer
from config import device
import student

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
busCat = []
ratCat = []
for i in range(50000):
    busCat.append(dataset[i].businessCategory)
    ratCat.append(dataset[i].rating)

f = open('bus_cat.txt', 'wb')
writer = csv.writer(f)
data_line = bytearray(busCat)
f.write(data_line)
f.close()

f = open('rat_cat.txt', 'wb')
writer = csv.writer(f)
data_line = bytearray(ratCat)
f.write(data_line)
f.close()

unique_words ={}
for i in range(50000):
    for word in dataset[i].reviewText:
        unique_words[word] = unique_words.get(word, 0) + 1

red_unique_words = {k:v for (k,v) in unique_words.items() if v > 10}

count1 =0
count2 =0
count3 =0
for word in range(19)

unique_zeroed = dict.fromkeys(sorted(red_unique_words, key=red_unique_words.get, reverse=True), 0)
count1 =0
count2 =0
count3 =0
for word in range(19)

#unique_zeroed = dict.fromkeys(sorted(unique_words, key=unique_words.get, reverse=True), 0)
f = open('reviews_ngramsXX.txt', 'wb')
writer = csv.writer(f)

#write the review data, in the form of ngrams, to file
for i in range(50000):
    dict_line = dict(unique_zeroed) #creates an empty dictionary, with correct ngram keys, but zeros for values
    for word in dataset[i].reviewText:  #goes through each review, and if possible, adds each ngram
        if word in unique_zeroed:
            dict_line[word] +=1
    data_line = bytearray(list(dict_line.values())) #creates line of data to be written to file
#    print(list(dict_line.values())[0:10])
#    print(dict_line.keys())
    f.write(data_line)
    if (i % 1000 == 0):
        print(i)
f.close()
print(len(unique_words))
print(len(red_unique_words))



#print(len(unique_words))
#decreasing = sorted(unique_words, key=unique_words.get, reverse=True)
#print(decreasing[1:100])
#print(unique_words[decreasing[1:10]])
#textField.build_vocab(dataset, vectors=student.wordVectors)

#trainLoader = data.BucketIterator(dataset, shuffle=True,
#                                  batch_size=student.batchSize,
#                                  sort_key=lambda x: len(x.reviewText),
#                                  sort_within_batch=True)

#for i, batch in enumerate(trainLoader):
#    print(textField.vocab.vectors.to(device))
#    inputs = textField.vocab.vectors[batch.reviewText[0]].to(device) #tensor of batchsize, no of padded GLOVES and size of GLOVE
#    length = batch.reviewText[1].to(device)
#    rating = batch.rating.to(device)
#    businessCategory = batch.businessCategory.to(device)
#    print(batch.reviewText)
#    print(list(inputs.size()))
#    print(length)
#    print(rating) #YAY! I understand this!!!
#    print(businessCategory) #YAY! I understand this!!!



