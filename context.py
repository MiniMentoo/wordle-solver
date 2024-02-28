from string import ascii_lowercase

class Context:
    def __init__(self, size : int) -> None:
        self.possibile_chars : list[dict[str, bool]]= []
        self.chars_in_word: list[str]= []
        self.WORDLE_SIZE = size
        chars = {}
        for char in ascii_lowercase:
            chars.update({char : True})
        for i in range(self.WORDLE_SIZE):
            self.possibile_chars.append(chars.copy())
    
    def process_grey(self, char : str) -> None:
        for i in range(self.WORDLE_SIZE):
            self.possibile_chars[i][char] = False
    
    def process_green(self, char: str, position : int) -> None:
        for c in ascii_lowercase:
            if c != char:
                self.possibile_chars[position][c] = False
            else:
                self.possibile_chars[position][c] = True
    
    def process_yellow(self, char : str, position : int) -> None:
        if not char in self.chars_in_word:
            self.chars_in_word.append(char)
        self.possibile_chars[position][char] = False