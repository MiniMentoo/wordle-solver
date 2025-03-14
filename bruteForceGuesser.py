#GUESSLIST = "words.txt"
GUESSLIST = "shorter_guess_list.txt"
ANSWERLIST = "answers.txt" #this is an outdated answerlist but it'll do

from filter import filter_by_guess
from accuracy_finder import calculate_accuracy

with open(GUESSLIST, "r") as words:
    lines = words.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()
words.close()
with open(ANSWERLIST, "r") as words:
    valid_words = words.readlines()
for i in range(len(valid_words)):
    valid_words[i] = valid_words[i].rstrip()
words.close()



if __name__ == "__main__":
    num_valid_words = len(valid_words)
    candidateGuess_leaderboard = {}
    for candidateGuess in lines:
        total_answer_size = 0
        for answer in valid_words:
            accuracy = calculate_accuracy(candidateGuess, answer)
            possibleAnswers = filter_by_guess(candidateGuess, accuracy, valid_words)
            total_answer_size += len(possibleAnswers)
        average_possible_answers_after_guess = total_answer_size / num_valid_words
        candidateGuess_leaderboard[candidateGuess] = average_possible_answers_after_guess
    
    for (key, value) in sorted(candidateGuess_leaderboard.items(), key=lambda item: item[1]):
        print(f"{key} : {value}")