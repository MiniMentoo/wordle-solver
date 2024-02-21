from string import ascii_lowercase

class Analyser:
    def __init__(self, words : list[str]) -> None:
        self.words : list[str] = words.copy()
        self.WORDLE_SIZE : int = 5
        self.probability_list : list[dict[str, float]] = self.precompute_ranks()
    
    def eval_guess(self, guess : str) -> float:
        pass
        #should take a guess and give percentage the guess is good
        #guesses that narrow down the possible answerlist most should rank higher
        #guesses that are guaranteed to be correct should return 100
        #guesses that only gain one letter eg (c)atch (m)atch (w)atch should rank lower than
            #a guess which searches all these letters 
    
    def precompute_ranks(self) -> list[dict[str, float]]:
        rankList : list[dict[str, float]] = [] #stores 5 dictionaries, each keeping track of the probability of the letter being in that position
        length = len(self.words)
        for i in range (self.WORDLE_SIZE):
            dictionary = {}
            for c in ascii_lowercase:
                dictionary.update({c : 0})
            rankList.append(dictionary)
        
        #for every word, add each of its letters to its ranklist in the corresponding position
        for x in range(length-1, -1, -1):
            for i in  range(self.WORDLE_SIZE):
                c = self.words[x][i]
                rankList[i][c] = rankList[i][c] + 1    
        
        #dividing each entry in the list with the total number to get a probability between 0 and 1
        for i in range(self.WORDLE_SIZE):
            for key in rankList[i]:
                rankList[i][key] = rankList[i][key] / length
        return rankList