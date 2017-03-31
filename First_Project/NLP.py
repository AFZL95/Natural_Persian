#this is the first project of natural language processing course, Ali Fazeli
# -*- coding: utf-8 -*-
import codecs
import re
import string
from collections import Counter
import occurrence
        ### getting the inpute data from the user ###

#opening a file for reading the context
input_text =  "converted.txt" #input("Please Enter The full address of source File  : ")

#creating a file for writing the spilited words
output_text =  "output.txt" #input("Please Enter The full address of destination File :")

#creating file streams for writing the outputed results to the files, strict define br "utf-8" encoding
file = codecs.open(output_text, "w","utf-8")

wordfreq = []
wordlist=[]
#opening the input_text variable and initializing for process
with codecs.open(input_text,encoding="utf-8") as fp:
    for line in fp:
        #appending the context to a list and spliting into individual chunks
        wordlist.append(line.split())
        #wordlist = input_text.split()
        for word in wordlist:
            wordfreq.append(wordlist.count(word))
            #print(str(word))
            #writing the results
        file.write(str(wordlist)+ "\n")

#closing the file stream
file.close()

#using "mktrans" method to replace nothing for the punctuation stuff in the context
translator = str.maketrans('', '', string.punctuation)

#the area for counting the occurrence of words in the input file
wordstring = codecs.open('converted.txt', 'r+', encoding='utf-8')
data = wordstring.read()
#print(data)
wordlist = data.split()

for w in wordlist:
    wordfreq.append(wordlist.count(w))


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


