#this is the Final Natural Language Processing project presented by
#Ali Fazeli 
import preprocessdata as ppd
#some complex stuff!
def printArray(array):
	for each in array:
		print each

def sentenceProbability(words, twoWordList, probMatrix):
	probability = 1
	#for each word in the sentence 
	for i in range(0,len(words) - 1):
		probability *= probMatrix[i][i+1]

	return probability


def GeneralBiGram(inputString1, wordList, twoWordList, totalSentences):
	print "For the sentence",inputString1,"using general approach :"
	Matrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	ProbabilityMatrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	dividedby = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	probability = 0

	words = inputString1.split()
	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i]+"-"+words[j] in twoWordList:
				Matrix[i][j] = twoWordList[words[i]+"-"+words[j]]

	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i] in wordList:
				dividedby[i][j] = wordList[words[i]]

	for i in range(0,len(ProbabilityMatrix)):
		for j in range(0,len(ProbabilityMatrix)):
			if dividedby[i][j] != 0:
				ProbabilityMatrix[i][j] = float(Matrix[i][j])/float(dividedby[i][j])
			else:
				ProbabilityMatrix[i][j] = 0

	if "-"+words[0] in twoWordList:
		probability = float(float(twoWordList["-"+words[0]]))/float(totalSentences)


	print '------------------------------- Matrix -----------------------------------------'
	printArray(Matrix)
	print '------------------------------- ProbabilityMatrix ------------------------------'
	printArray(ProbabilityMatrix)
	print '------------------------------- SentenceProbability ----------------------------'
	probability *= sentenceProbability(words, twoWordList, ProbabilityMatrix)

	return probability


def EnhancedBiGram(inputString1, wordList, twoWordList, totalWords, totalSentences):
	print " BiGram For the sentence",inputString1,"using Enhanced technique  (Add one) :"
	Matrix = [[1 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	ProbabilityMatrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	dividedby = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	probability = 0

	words = inputString1.split()
	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i]+"-"+words[j] in twoWordList:
				Matrix[i][j] += twoWordList[words[i]+"-"+words[j]]

	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i] in wordList:
				dividedby[i][j] = wordList[words[i]]+totalWords
			else:
				dividedby[i][j] = totalWords

	for i in range(0,len(ProbabilityMatrix)):
		for j in range(0,len(ProbabilityMatrix)):
			ProbabilityMatrix[i][j] = float(Matrix[i][j])/float(dividedby[i][j])

	if "-"+words[0] in twoWordList:
		probability = float(float(twoWordList["-"+words[0]]+1))/float(totalSentences+totalWords)


	print '------------------------------- Matrix ----------------------------------'
	printArray(Matrix)
	print '------------------------------- ProbabilityMatrix ------------------------------'
	printArray(ProbabilityMatrix)
	print '------------------------------- SentenceProbability ----------------------------'
	probability *= sentenceProbability(words, twoWordList, ProbabilityMatrix)

	return probability



def main():
	#some preprocess we've got here
	stringToProcess = ppd.getStringFromFile()
	stringToProcess = ppd.stringCleanUp(stringToProcess)
    #computing necessarily stuff
	wordList, totalWords, totalSentences = ppd.getEachWordFrequency(stringToProcess)
	twoWordList = ppd.getGivenPreviousWordNewWordFrequency(stringToProcess)
	inputString1 = "Hello there, what's up guys?! how are you donig? Hello!"
	inputString2 = "I'm Ali Fazeli and I'm Pleased to meet you."
	inputString1 = ppd.stringCleanUp(inputString1)
	inputString2 = ppd.stringCleanUp(inputString2)

	''' here we calculate the probability tables without any smoothing technique'''
	probability1 = GeneralBiGram(inputString1, wordList, twoWordList, totalSentences)
	print "Probability of sentence 1 is :", probability1,
	print "\n\n\n"
	probability2 = GeneralBiGram(inputString2, wordList, twoWordList, totalSentences)

	print "Probability of sentence 1 is :", probability1,"Probability of sentence 2 is", probability2
	print "\n\n\n"

	''' add one Enhanced technique '''
	probability1 = EnhancedBiGram(inputString1, wordList, twoWordList, totalWords, totalSentences)
	print "Probability of sentence 1 is :", probability1,
	print "\n\n\n"
	probability2 = EnhancedBiGram(inputString2, wordList, twoWordList, totalWords, totalSentences)

	print "Probability of sentence 1 is :", probability1,"Probability of sentence 2 is", probability2
	print "\n\n\n"


#we start from the main function
if __name__ == '__main__':
	main()