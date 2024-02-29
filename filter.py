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
        elif (words[x][pos] == char):
            words.pop(x)
    return words

def filterNonDupes(char, pos, words):
    for x in range(len(words)-1, -1, -1):
        if (not hasDupe(char, words[x])):
            words.pop(x)
        elif (words[x][pos] == char):
            words.pop(x)
    return words
