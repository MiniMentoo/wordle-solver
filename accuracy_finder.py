'''
Calculate accuracy
    - for each duplicate letter in guess
        - green all the ones in the right place first
        - then yellow any others until num(green+yellow)==freq(char in word)
        - grey the rest
        - mark all of that character as checked
    - iterate through unchecked letters
        - if letter in word but wrong place, yellow
        - if letter in right place, green
        - if letter not in word, grey
'''
def calculate_accuracy(guess : str, answer: str) -> str:
    accuracy=['5','5','5','5','5'] # 5 represents an unchecked char
    ## checking for dupes first
    dupes=[]
    letter=[]
    for char in guess:
        if ((char in letter) and (not char in dupes)):
            dupes.append(char)
        else:
            letter.append(char)
    ## sorting duplicates
    for duplicate in dupes:
        x_in_guess = numOf(duplicate, guess)
        x_in_answer = numOf(duplicate, answer)
        for i in range (5): #If char is placed right, green it
            if(answer[i] == duplicate and guess[i] == answer[i]):
                accuracy[i] = '2'
                x_in_guess -= 1
                x_in_answer -= 1
        while(x_in_answer > 0 and x_in_guess > 0): #Yellow the non greens until we have the same amount of greens+yellows as number of that char in the answer (or we run out of number of that char in the guess)
            index = findUncheckedChar(duplicate, accuracy, guess)
            if(index == 99):
                print(f"Error at Duplicate:{duplicate} Accuracy:{accuracy} Guess:{guess}")
            accuracy[index] = '1'
            x_in_answer -= 1
            x_in_guess -= 1
        if(x_in_guess > 0): #Grey the rest
            for i in range (5):
                if(accuracy[i] == '5' and guess[i] == duplicate):
                    accuracy[i] = '0'

    ##Normal filter
    for i in range (5):
        char = guess[i]
        if (accuracy[i] == '5'):
            if(guess[i] == answer[i]):
                accuracy[i] = '2'
            elif (guess[i] in answer):
                accuracy[i] = '1'
            else:
                accuracy[i] = '0'
    accuracy=''.join(accuracy)
    #print(f"GUESS:{guess}  ANSWER:{answer}  ACCURACY:{accuracy}")
    return accuracy

def findUncheckedChar(letter : str, accuracy:str, word:str) -> int:
    for i in range(5):
        if(word[i]==letter and accuracy[i] == '5'):
            return i
    return 99 ##throws index out of bounds hopefully

def numOf(letter : str, word : str) -> int:
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count