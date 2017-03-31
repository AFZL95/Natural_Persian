#this is the first project of natural language processing course, Ali Fazeli
# -*- coding: utf-8 -*-
import codecs
import json
import io
import re
import string
from collections import Counter
import occurrence

#including some list to append data into it
wordfreq = []
wordlist=[]
#reguar expression pattern for the detection of the IP
expression = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

            ### getting the input data from the user ###

#opening a file for reading the context
input_text =  "Normalized.txt" #input("Please Enter The full address of source File  : ")

#creating a file for writing the spilited words with punctuations
output_text_1 =  "OutPut_with_Punctuation.txt" #input("Please Enter The full address of destination File :")

#creating a file for writing the spilited words without punctuations
output_text_2 =  "OutPut_without_Punctuation.txt" #input("Please Enter The full address of destination File :")

#creating file streams for writing the outputed results to the files, strict define br "utf-8" encoding ("OutPut_with_Punctuation.txt")
file_1 = codecs.open(output_text_1, "w","utf-8")

#creating file streams for writing the outputed results to the files, strict define br "utf-8" encoding ("OutPut_without_Punctuation.txt")
file_2 = codecs.open(output_text_2, "w","utf-8")

            ### opening the input_text_1 file and writing the tokenized string with their punctuations ###
with codecs.open(input_text,encoding="utf-8") as fp:
    for line in fp:
        result = expression.findall(line)
        print(result)
        #appending the context to a list and splitting into individual chunks
        list = line.split()
        for word in list:
            wordfreq.append(list.count(word))
            #writing the results
            file_1.write(word +'\r\n')
#closing the file stream
file_1.close()

            ###opening the input_text_2 file and writing the tokenized string without the punctuations ###

#using "mktrans" method to replace nothing for the punctuation stuff in the context
translator = str.maketrans('', '', string.punctuation)
wordstring = codecs.open('Normalized.txt', 'r+', encoding='utf-8')
data = wordstring.read()
#print(data)
wordlist = data.split()
message = 'the string without the punctuation marks is : '
file_2.write(message)
file_2.write(str(data.translate(translator)))
file_2.close()

#the area for counting the occurrence of words in the input file
for w in wordlist:
    wordfreq.append(wordlist.count(w))


            ###console demonstrating area ###

#printing the results
print("Original String:\n" + data +"\n")
print("Words in order of List\n" + str(wordlist) + "\n")
print("the text without duplicate words: \n" + str(occurrence.uniquify(data)))
#demonstarting the barebone text without punctuation marks
print(" \n number of the all words are:"+ str(len(wordlist)))
print("the inputed text without punctuation marks is: \n" + str(data.translate(translator)))
modified_data=data.translate(translator)
print("Number of Distinct Words in the Text: " + str(Counter(modified_data.split())))
print("Frequencies\n" + str(wordfreq) + "\n")


data = {'Original_Text ': data,
        'Splited_Text' : wordlist,
        'Text_without_Duplicate' : occurrence.uniquify(data),
        'Text_without_Punctuation' : data.translate(translator),
        'Total_words' : len(wordlist),
        'Distinct_word_Frequencies': Counter(modified_data.split())
        }
            ### and in the last area, JSON manipulating ###

# Define data

# Write JSON file
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ':'), ensure_ascii=False)
    outfile.write(str_)

# Read JSON file for the test
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

#print(data_loaded)
#print(data == data_loaded)

