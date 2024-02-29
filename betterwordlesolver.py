WORDLE_SIZE = 5
GUESSLIST = "words.txt"
ANSWERLIST = "answers.txt" #this is an outdated answerlist but it'll do

from string import ascii_lowercase
from analyser import Analyser
from filter import filter_by_guess

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
    analist = Analyser(valid_words, lines)
    loop = True
    print("----Finding best guess----")
    #(word, score) = (analist.find_best_guess())
    #print(f"{word} with score {score}")
    print ("soare from prcomputation") #this is the precomputed best guess, uncomment the first two lines if you want to verify, will take a minute to run
    while (loop):
        word = input("Enter a 5 letter word: ")
        accuracy = input("How correct was the word? 0 = grey, 1 = yellow, 2 = green: ")
        analist.filter(word, accuracy)
        print(analist.valid_words)
        print("----Finding best guess----")
        (word, score) = analist.find_best_guess()
        print(f"{word} with score {score}")

        loop = len(analist.valid_words) > 1

    print("Jobs done!")