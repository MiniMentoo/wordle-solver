# wordle-solver
A tool to help solve wordles!

I added two text files, "words.txt" a complete 12k long list words you can guess (around 3k of which are possible answers), and "answers.txt" an outdated list of over 2k possible answers (when NYT bought wordle they changed the list and haven't published the answers, so it's quite possible the solver won't show the answer if you're just using answers.txt.

# The design is very human!
  - Run betterwordlesolver.py (yea it's an odd name sorry about that), make sure the words.txt and answers.txt are in the same directory with the same names!
  - Solver will show you a precomputed 5 letter guess (SOARE, you can run it yourself by uncommenting lines in main, it will take a couple of minutes though)
  - You can choose to input that same word or your own guess!
  - The solver will then ask for the accuracy of that guess (give it 5 numbers 0=Grey 1=Yellow 2=Green)
  - Solver filters down the possible answers and shows you all remaining possible guesses, then computes the best guess based on your context!
  - Rinse and repeat until it finds the answer!

Very simple tool, I thought I ruined wordle for myself but in an odd way I think I've enjoyed building this tool more than anything else. I have no idea why I built it in python but my skills in this language have definately improved!

# Why did I make this?
The TLDR of it is that I got very into wordle a while back, unfortunately, I'm quite bad at wordle! So on a particularly difficult day (LEGGY) I decided to make the first "wordlesolver.py". In hindisht calling it a solver was incredibly arrogant, but we move. I iteratively improved on it in my free time, eventually making a working filter. I showed it off to one of my professors that I work with, and he asked me "why not make it come up with guesses?"
About 10 hours of work later I managed to make it make decent guesses! But I was struggling with the "-ATCH" example (if the solver finds a lot of greens like the the last 4 letters ATCH, there are many different first letters to guess, catch, latch, batch, match etc and the wordle will never make an exploratory guess, instead it will just wildly guess). I was introduced to the idea of information theory by a friend I work with (this was conveniently a topic adjacent to his PHD).
Another 15 hours at this laptop and I've managed to finish this thing! Funnily enough, in implementing this information theory it made a lot of the previous guesses better (even when they were already pretty good and not the edge case I was considering?). I'm very proud of this, as it's the first project I can confidently say I've finished, there is room for improvement though...

# Room for improvement!
  - I have not tested my low level functions nearely enough. I honestly thought this would be a quick project and it's not worth it, I now see the error of my ways. There are most likely bugs down there, especially in the functions used by score_info_gained in the analyser.
  - There is 1 edge case not considered in my filter.py where the input given has 3 of the same letter and 2 are in the final word (I commented where it is). It hasn't come up yet but should be a relatively easy patch.
  - The user input leaves something to be desired, perhaps there's a way to load the guess box automatically with the guess the solver produces? I also think there should be a way to turn off the list of all possible guesses to make it look nicer.

# How this works?
I'll leave this mainly as a reminder for myself incase I begin working on this again in a year or 2. Good luck 🙂!

# Final notes
This has been an irresponsible investment of my time at best. I got way into this project and I have coursework deadlines looming above me! But honestly I'd do it all again.

I'll take a break and clear out this essay before getting into my next project, I'm hoping I won't have to use python on it!

- Mostafa 🍬
