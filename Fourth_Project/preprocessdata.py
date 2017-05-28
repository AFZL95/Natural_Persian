# this is the Final Natural Language Processing project presented by
# Ali Fazeli
import re

# removing the exact "\n" character function
def removeNewLineChar(stringToProcess):
    return stringToProcess.replace("\n", " ")

# deviding the corpus in lines with the "." stop word
def splitInLines(stringToProcess):
    return stringToProcess.replace(" . ", "\n")

# removing the redundent symbols like dash or single quotation
def removeSpecialCharacter(stringToProcess):
    stringToProcess = stringToProcess.replace("'", " ").replace(
        '"', " ").replace('-', " ").replace("`", " ")
    stringToProcess = stringToProcess.replace(
        ",", " ").replace("\\", " ").replace("/", " ").lower()
    stringToProcess = re.sub(' +', ' ', stringToProcess)
    return stringToProcess

#reindent the whole text, in order to remove two or three trailed spaces
def removeTrailingSpaces(stringToProcess):
    stringList = stringToProcess.split("\n")
    stringToProcess = ""
    for each in stringList:
		#the strip() function removes all spaces in the given string
        stringToProcess += each.strip() + "\n"
    return stringToProcess

# as the name of function stands...
def getStringFromFile():
    data = ""
    with open("corpus.txt", "r+") as f:
        data = f.read()
    return data

'''a usefull handy function that calculates these stuff:
1- "WordList" : the tokens which stored in a list
2- "total words" : sum up all words in a numerical variable
3- "len(stringList)" : how many character that string have
'''
def getEachWordFrequency(stringToProcess):
    stringList = stringToProcess.split("\n")
    wordList = {}
    totalWords = 0
	#i've got no clue to process this without two for loops!!!
    for each in stringList:
        lineWords = each.strip().split()
        for eachWord in lineWords:
            if eachWord in wordList:
                wordList[eachWord] += 1
            else:
                totalWords += 1
                wordList[eachWord] = 1

    return wordList, totalWords, len(stringList)


def getGivenPreviousWordNewWordFrequency(stringToProcess):
    stringList = stringToProcess.split("\n")
    wordList = {}
    for each in stringList:
        lineWords = each.strip().split()
        for i in range(0, len(lineWords)):
            if i == 0:
                key = "-" + lineWords[i]
                if key in wordList:
                    wordList[key] += 1
                else:
                    wordList.update({key: 1})
            else:
                key = lineWords[i - 1] + "-" + lineWords[i]
                if key in wordList:
                    wordList[key] += 1
                else:
                    wordList.update({key: 1})

    # print wordList
    return wordList

# summing up the base functions into an individual method
def stringCleanUp(stringToProcess):
    stringToProcess = removeNewLineChar(stringToProcess)
    stringToProcess = splitInLines(stringToProcess)
    stringToProcess = removeSpecialCharacter(stringToProcess)
    stringToProcess = removeTrailingSpaces(stringToProcess)
    return stringToProcess
