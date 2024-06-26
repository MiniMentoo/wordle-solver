def filter_by_guess(guess : str, accuracy : str, word_list : list[str]) -> list[str]:
    words = word_list.copy()
    dupes = [] #keeps a record of characters checked so it can track dupes
    remove = []
    for i in range (5):
        char = guess[i]
        acc = accuracy[i]
        if (acc == '0' and (char in dupes)):
            words = deleteDupes(char, i, words) #doesn't work if the word has 3 of the same letter (idk why you'd ever guess that)
        elif (acc == '1' and (char in dupes)):
            words = filterNonDupes(char, i, words)
        elif (acc == '2' and (char in dupes)): #for the edge case where a double letter is guessed and it goes yellow then green
            words = filterNonGreenDupes(char, i, words)
        elif (acc == '0'):
            remove.append(char)
        elif (acc == '1'):
            words = eliminateYellow(char, i, words)
            dupes.append(char)
        elif (acc == '2'):
            words = findMatch(char, i, words)
            dupes.append(char)
    while(remove):
        char = remove.pop()
        if (not char in dupes):
            words = eliminateLetter(char, words)
        else:
            words = deleteDupes(char, -1, words)
    return words

def len_filter_by_char(guess_char : str, accuracy_char : str, position : int, is_dupe : bool, word_list : list[str], length_original : int) -> int:
    words = word_list.copy()
    if (accuracy_char == '0' and is_dupe):
        words = deleteDupes(guess_char, position, words)
    elif (accuracy_char == '0'):
        words = eliminateLetter(guess_char, words)
    elif (accuracy_char == '2'):
        words = findMatch(guess_char, position, words)
    length = len(words)
    if length == 0:
        return 1
    if length == 1: #if this filter will get us to 1 possible guess, it's the best it can be
        #if this isn't set to 0 then near the end it'll be 1/3 due to the small size of the possible answerlist
        #so I'm setting it to 0 to encourage guesses that reduce down to 1 possible answer specifically
        return 0
    return length / length_original

def charInWord(char, word):
    for c in word:
        if(char == c):
            return True
    return False

def eliminateLetter(char, words):
    for x in range(len(words)-1, -1, -1):
        if charInWord(char, words[x]):
            words.pop(x)
    return words

def eliminateYellow(char, pos, words):
    for x in range(len(words)-1, -1, -1):
        if (not charInWord(char, words[x])):
            words.pop(x)
        elif (words[x][pos] == char):
            words.pop(x)
    return words

def findMatch(char, i, words):
    for x in range(len(words)-1, -1, -1):
        if (words[x][i] != char):
            words.pop(x)
    return words

def hasDupe(char, word):
    count = 0
    for c in word:
        if c == char:
            count += 1
    return count > 1

def deleteDupes(char, pos, words):
    for x in range(len(words)-1, -1, -1):
        if(hasDupe(char, words[x])):
            words.pop(x)
        elif (pos >= 0 and words[x][pos] == char):
            words.pop(x)
    return words

def filterNonDupes(char, pos, words):
    for x in range(len(words)-1, -1, -1):
        if (not hasDupe(char, words[x])):
            words.pop(x)
        elif (words[x][pos] == char):
            words.pop(x)
    return words

def filterNonGreenDupes(char, pos, words):
    for x in range(len(words)-1, -1, -1):
        if (not hasDupe(char, words[x])):
            words.pop(x)
        elif (words[x][pos] != char):
            words.pop(x)
    return words