# import random
# import re
# from array import array

# wordlist = ["Green Arrow", "Flash", "Superman", "Clark Kent", "Barry Allen", "Oliver Queen"]
# word = random.choice(wordlist) 
# word = "envelope"
 
# letter_display = []
 
# for i in range(len(word)):
#     letter_display.append('_')
 
# print(" ".join(letter_display))
 
# guess = input("Let's play hangman!\nGuess a letter: ")
 
# for x in re.finditer(guess, word):
#     letter_display[x.start()] = guess

 
# print(" ".join(letter_display))
 
# hangman0 = \
# '  -------    \n'\
# '  |          \n'\
# '  |          \n'\
# '  |          \n'\
# '  |          \n'\
# '  |          \n'\
# '  |          \n'\
# '-----        '
# hangman1 = \
# '  -------    \n'\
# '  |     |    \n'\
# '  |     O    \n'\
# '  |          \n'\
# '  |          \n'\
# '  |          \n'\
# '  |          \n'\
# '-----        '
# hangman2 = \
# '  -------    \n'\
# '  |     |    \n'\
# '  |     O    \n'\
# '  |   -----  \n'\
# '  |   |   |  \n'\
# '  |          \n'\
# '  |         \n'\
# '-----        '
# hangman3 = \
# '  -------    \n'\
# '  |     |    \n'\
# '  |     O    \n'\
# '  |   -----  \n'\
# '  |   | | |  \n'\
# '  |     |    \n'\
# '  |          \n'\
# '-----        '

# hangman4 = \
# '  -------    \n'\
# '  |     |    \n'\
# '  |     O    \n'\
# '  |   -----  \n'\
# '  |   | | |  \n'\
# '  |     |    \n'\
# '  |    / \   \n'\
# '-----        '


# print(hangman0)
import urllib.request
import re
import requests
from bs4 import BeautifulSoup
import ssl
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
print("Wait a moment...")
wordlist = ["greenarrow", "flash", "superman", "clarkkent", "barryallen", "oliverqueen"]

context = ssl._create_unverified_context()
response = urllib.request.urlopen('https://www.vocabulary.com/lists/52473', context=context)

soup = BeautifulSoup(response, "html.parser")

for a in soup.find_all('a','word dynamictext'):
    wordlist.append(a.string)
word = random.choice(wordlist)
print("Let's play hangman!")

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
    print("Ooops! Try again :-){}".format(word))
 








#if guess in word:
    #print("Yes!")