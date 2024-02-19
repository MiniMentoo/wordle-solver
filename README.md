# wordle-solver
A tool to help solve wordles!

I added two text files, "words.txt" a complete 12k long list words you can guess (around 3k of which are possible answers), and "answers.txt" an outdated list of over 2k possible answers (when NYT bought wordle they changed the list and haven't published the answers, so it's quite possible the solver won't show the answer if you're just using answers.txt.

# The design is very human!  
  -Solver asks you for a 5 letter word
  
  -Solver asks for accuracy (5 numbers 0=Grey 1=Yellow 2=Green)
  
  -Solver filters invalid words and shows you possible ones

Quite a simple tool! I got super into Wordle and now I've successfully ruined the game for myself 😢. I'll try not to use it too much.

# EDIT!
A friend gave me an idea and it's lodged itself in my head, so I'm continuing work on this thing!
First of all, the filtering works fine now! (No more edge cases!).
Second I'm trying to make it produce GOOD guesses, including some system of ranking what makes a good guess. I'll be experimenting with a variety of my own ideas, including loading the answer list and having it prefer those, and also grouping first and last two letters toghether to try and recognise real words.

Currently my solver can get the wordle by itself MOST of the time, it can get trapped if it guessed too many greens first, as it'll never not stop guessing a green after it finds one.
