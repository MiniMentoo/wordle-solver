WORDLE_SIZE = 5
#comment whichever one you're not using, I recommend using the full words.txt since answers.txt is outdated and might miss answers
FILENAME = "words.txt"
#FILENAME = "answers.txt"

from string import ascii_lowercase
from analyser import Analyser
from filter import filter_by_guess

with open(FILENAME, "r") as words:
    lines = words.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()


def rankList(words):
    rankList = [] #stores 5 dictionaries, each keeping track of how many times the letter appeared in that position
    for i in range (WORDLE_SIZE):
        dict = {}
        for c in ascii_lowercase:
            dict.update({c : 0})
        rankList.append(dict)
    
    for x in range(len(words)-1, -1, -1):
        for i in  range(WORDLE_SIZE):
            c = words[x][i]
            rankList[i][c] = rankList[i][c] + 1    
    return rankList

def computeValue(word, rankList):
    value = 0
    for i in range(WORDLE_SIZE):
        value += rankList[i][word[i]]
    return value

def findBestGuess(words, rankList):
    bestVal = -1
    bestWord = None
    for word in words:
        val = computeValue(word, rankList)
        if val > bestVal:
            bestVal = val
            bestWord = word
    return bestWord

loop = True
print("----Finding best guess----")
print (findBestGuess(lines, rankList(lines)))
while (loop):
    word = input("Enter a 5 letter word: ")
    accuracy = input("How correct was the word? 0 = grey, 1 = yellow, 2 = green: ")
    lines = filter_by_guess(word, accuracy, lines)
    print(lines)
    print("----Finding best guess----")
    print (findBestGuess(lines, rankList(lines)))

    loop = len(lines) > 1

print("Jobs done!")