from string import ascii_lowercase
from filter import filter_by_guess, findDupes

class Analyser:
    def __init__(self, answers : list[str], all_guesses : list[str]) -> None:
        self.valid_words : list[str] = answers.copy()
        self.all_guesses : list[str] = all_guesses.copy()
        self.WORDLE_SIZE : int = 5
        self.probability_list : list[dict[str, float]] = self.precompute_ranks()
        self.frequency_list : dict[str, float] = self.precompute_frequencies()
    
    def find_best_guess(self) -> str:
        bestVal = -1
        bestWord = None
        for word in self.all_guesses:
            val = self.eval_guess(word)
            if val > bestVal:
                bestVal = val
                bestWord = word
        return bestWord
    
    def eval_guess(self, guess : str) -> float:
        return self.score_guess(guess) #TODO implement cool info theory stuff later
    
        #should take a guess and give percentage the guess is good
        #guesses that narrow down the possible answerlist most should rank higher
        #guesses that are guaranteed to be correct should return 100
        #guesses that only gain one letter eg (c)atch (m)atch (w)atch should rank lower than
            #a guess which searches all these letters 
    
    def precompute_ranks(self) -> list[dict[str, float]]:
        rankList : list[dict[str, float]] = [] #stores 5 dictionaries, each keeping track of the probability of the letter being in that position
        length = len(self.valid_words)
        for i in range (self.WORDLE_SIZE):
            dictionary = {}
            for c in ascii_lowercase:
                dictionary.update({c : 0})
            rankList.append(dictionary)
        
        #for every word, add each of its letters to its ranklist in the corresponding position
        for x in range(length-1, -1, -1):
            for i in  range(self.WORDLE_SIZE):
                c = self.valid_words[x][i]
                rankList[i][c] = rankList[i][c] + 1    
        
        #dividing each entry in the list with the total number to get a probability between 0 and 1
        for i in range(self.WORDLE_SIZE):
            for key in rankList[i]:
                rankList[i][key] = rankList[i][key] / length
        return rankList
    
    def precompute_frequencies(self) -> dict[str, float]:
        dictionary = {}
        length = len(self.valid_words)
        for c in ascii_lowercase:
            dictionary.update({c : 0})
            
        for word in self.valid_words:
            for char in word:
                dictionary[char] = dictionary[char] + 1
        
        for key in dictionary:
            dictionary[key] = dictionary[key] / length
        
        return dictionary
    
    def probability_char_in_answer(self, char : str) -> float:
        return self.frequency_list[char]
    
    def probability_char_goes_green(self, char : str, index : int) -> float:
        return self.probability_list[index][char]
    
    def score_guess(self, guess : str) -> float:
        dupes = []
        score = 0
        #juvenile function, adds probabilities each letter in guess is in word (taking into account dupes)
        # and adds probabilities the letter goes green aswell
        for i in range(self.WORDLE_SIZE):
            char = guess[i]                        
            score += self.probability_char_goes_green(char, i)
            prob_yellow = self.probability_char_in_answer(char)
            if char not in dupes:
                score += prob_yellow
                dupes.append(char)
            elif prob_yellow > 1:
                score += prob_yellow - 1
        return score