# wordle-solver
A python CLI application to solve Wordle puzzles.

# Instructions
Run `python main.py` to launch the script.

You'll be asked to enter the green letters of your word so far, with any other letters denoted by an underscore ('\_').
For example, if you know your word has the letters `c` and `e` in positions 4 and 5, enter `_ _ _ c e`. 
If you have no green letters so far, enter '\_\_\_\_\_'.

You'll then be asked to enter the yellow letters of your word so far. 
For example, if you have the yellow letters 'f' and 'a', enter 'fa'. 
If you have no yellow letters, just leave this blank and hit enter.

Finally, you'll be asked to enter any incorrect (grey) letters of your word so far.
For example, if you know the letters 'g' and 'h' are definitely not included in your word, enter 'gh'.
If you have no grey letters, just leave this blank and hit enter.

You'll then be given a list of possible five-letter words. 
