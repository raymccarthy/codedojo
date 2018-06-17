import random
import re
import os
from array import array
b = 0
hangman = [\
'  -------    \n'\
'  |          \n'\
'  |          \n'\
'  |          \n'\
'  |          \n'\
'  |          \n'\
'  |          \n'\
'-----        ',
'  -------    \n'\
'  |     |    \n'\
'  |     O    \n'\
'  |          \n'\
'  |          \n'\
'  |          \n'\
'  |          \n'\
'-----        ',
'  -------    \n'\
'  |     |    \n'\
'  |     O    \n'\
'  |   -----  \n'\
'  |   |   |  \n'\
'  |          \n'\
'  |         \n'\
'-----        ',
'  -------    \n'\
'  |     |    \n'\
'  |     O    \n'\
'  |   -----  \n'\
'  |   | | |  \n'\
'  |     |    \n'\
'  |          \n'\
'-----        ',
'  -------    \n'\
'  |     |    \n'\
'  |     O    \n'\
'  |   -----  \n'\
'  |   | | |  \n'\
'  |     |    \n'\
'  |    / \   \n'\
'-----        ']
print("Let's play hangman!\nClue: The word is a superhero or a superhero's alter ego;)")
wordlist = ["greenarrow", "flash", "superman", "clarkkent", "barryallen", "oliverqueen"]
word = random.choice(wordlist) 
letter_display = []
for i in range(len(word)):
        letter_display.append('.')
print("".join(letter_display))

wrong = 0

while "".join(letter_display) != word and wrong < 4: 
    guess = input("Guess a letter: ")
    os.system('clear') 

    xa = None
    for xa in re.finditer(guess, word):
        letter_display[xa.start()] = guess

    if xa is None:
        wrong = wrong + 1
        print("You have been wrong {} times".format(wrong))
        print(hangman[wrong - 1])
    else:
        print(hangman[wrong])
    
    print("".join(letter_display))
    
    
    

os.system('clear') 
print(hangman[wrong])
if "".join(letter_display) == word:
    print("Well done! ")
else:
    print("Ooops! Try again :-)")


    
