from string import ascii_lowercase
from filter import filter_by_guess, len_filter_by_char
from itertools import product

class Analyser:
    def __init__(self, answers : list[str], all_guesses : list[str]) -> None:
        self.valid_words : list[str] = answers.copy()
        self.valid_guesses : list [str] = all_guesses.copy()
        self.all_guesses : list[str] = all_guesses.copy()
        self.greys : list[str] = []
        self.WORDLE_SIZE : int = 5
        self.guessess_remaining : int = 6
        self.VALUE_OF_NEW_INFO : int = 3 #the coefficient of info to score in my eval function
        self.probability_list : list[dict[str, float]] = self.precompute_ranks()
        self.frequency_list : dict[str, float] = self.precompute_frequencies()
        self.best_score : int = 0
    
    def find_best_guess(self) -> tuple[str, float]:
        bestVal = -1
        bestWord = None
        length = len(self.valid_words)
        for word in self.all_guesses:
            val = self.eval_guess(word, length)
            if val > bestVal:
                bestVal = val
                bestWord = word
        return (bestWord, bestVal)
    
    def eval_guess(self, guess : str, length_original : int) -> float:
        score = self.score_guess(guess)
        if (self.guessess_remaining == 0 or length_original <= 2): 
            #if this is the last guess, don't bother with info theory, just try to guess the word
            #if this is a 50/50 or less just guess the word
            return score
        score_diff = max(score - self.best_score, 0) #i want the diff to be positive to not so highly discourage exploratory guesses
        
        return score_diff + (self.VALUE_OF_NEW_INFO * self.score_info_gained(guess, length_original))
        # score increases as rounds go on, not indicitive of info gained however
        # info gained will be 0 when guesslist is 1 (there is no more filtering that can be done)
    
    def filter(self, guess : str, accuracy : str) -> None:
        self.valid_words = filter_by_guess(guess, accuracy, self.valid_words)
        self.valid_guesses = filter_by_guess(guess, accuracy, self.valid_guesses)
        
        for acc, char in zip(accuracy, guess):
            if acc == "0":
                self.greys.append(char)
        
        #if the wordle of the day isn't in our answerlist, answerlist will become empty as we filter down
        # so make the entire remaining guesslist left our possible answerlist (should be very similar)
        if not self.valid_words:
            self.valid_words = self.valid_guesses
            
        self.frequency_list = self.precompute_frequencies()
        self.probability_list = self.precompute_ranks()
        self.guessess_remaining-=1
        self.best_score = max(self.score_guess(guess), self.best_score)
    
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
    
    def probability_char_in_answer(self, char : str, is_dupe : bool) -> float:
        prob_yellow = self.frequency_list[char]
        if not is_dupe:
            # need to make sure no probability added exceeds 1, and cus of duplicates prob_yellow can do so
            prob_yellow = min(prob_yellow, 1)
        elif prob_yellow > 1:
            # adding min here because otherwise the solver is biased for triplets
            prob_yellow = min(prob_yellow - 1, 1)
        else:
            prob_yellow = 0
        return prob_yellow
    
    def probability_char_goes_green(self, char : str, index : int) -> float:
        return self.probability_list[index][char]
    
    def score_guess(self, guess : str) -> float:
        dupes = []
        score = 0
        #juvenile function, adds probabilities each letter in guess is in word (taking into account dupes)
        # and adds probabilities the letter goes green aswell
        # min is 0 (the guess is so shit none of the letters could possibly be in the answer)
        # max is 10 (it is certain this is the only possible answer left)
        for i in range(self.WORDLE_SIZE):
            char = guess[i]                        
            score += self.probability_char_goes_green(char, i)
            score += self.probability_char_in_answer(char, char in dupes)
            dupes.append(char)
        return score
    
    def score_info_gained(self, guess : str, length_original : int) -> float:
        dividing_factor = 0
        dupes = []
        for i in range(self.WORDLE_SIZE): #function bugged, not finding the answer when it's narrowed it down to 1, produces random guess
            char = guess[i]
            if char in dupes:
                isDupe = True
            else:
                isDupe = False
                dupes.append(char)
            fraction1 = 1 - len_filter_by_char(char, "0", i, isDupe, self.valid_words, length_original)       
            dividing_factor += (1 - self.probability_char_in_answer(char, isDupe)) * fraction1
            fraction = 1 - len_filter_by_char(char, "2", i, isDupe, self.valid_words, length_original)
            dividing_factor += self.probability_char_goes_green(char, i) * fraction
        return dividing_factor