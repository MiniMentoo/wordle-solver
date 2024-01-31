# wordle-solver-FINISHED-
A tool to help solve wordles!

I added two text files, "words.txt" a complete 12k long list words you can guess (around 3k of which are possible answers), and "answers.txt" an outdated list of over 2k possible answers (when NYT bought wordle they changed the list and haven't published the answers, so it's quite possible the solver won't show the answer if you're using answers.txt.

# The design is very human!  
  -Solver asks you for a 5 letter word
  
  -Solver asks for accuracy (5 numbers 0=Grey 1=Yellow 2=Green)
  
  -Solver filters invalid words and shows you possible ones
  
  -Solver asks if you want to filter by another word

Quite a simple tool! I got super into Wordle and now I've successfully ruined the game for myself 😢. I'll try not to use it too much.

Oh! One small edge case it doesn't take into account is if you find out the word has a double letter in it, the solver doesn't filter all words that only have 1 of that letter. Might fix that later idk 🤷
