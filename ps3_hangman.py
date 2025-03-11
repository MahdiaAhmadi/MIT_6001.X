# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
   
    '''secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise'''
    
    # FILL IN YOUR CODE HERE...
    for chars in secretWord:
        if chars not in lettersGuessed:
          return False
    return True 
    

print(isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's']))  # Expected: False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed_word =''
    for chars in secretWord:
        if chars in lettersGuessed:
            guessed_word += chars
        else:
            guessed_word += '_'
    return guessed_word.strip()

print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])) 



import string  # noqa: E402
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.ascii_lowercase  # Get all lowercase letters 'abcdefghijklmnopqrstuvwxyz'
    remain_letters = '' 
    for chars in alphabet:
        if chars not in lettersGuessed:
            remain_letters += chars
    return remain_letters

print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])) 

    

#last phase
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secretWord)} letters long.')
    print('------------')
    lettersGuessed= []
    mistakesMade=0
    guess_count=8
    while mistakesMade < guess_count:
        print(f'You have {guess_count - mistakesMade} guesses left.')
        print(f'Available letters: {getAvailableLetters(lettersGuessed)}')
        
        # Get user input and ensure it's lowercase
        guess = input('Please guess a letter: ').lower()
        
        # Check if the letter was already guessed
        if guess in lettersGuessed:
            print(f'Oops! You\'ve already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}')
        elif guess in secretWord:
            # Correct guess
            lettersGuessed.append(guess)
            print(f'Good guess: {getGuessedWord(secretWord, lettersGuessed)}')
        else:
            # Incorrect guess
            lettersGuessed.append(guess)
            mistakesMade += 1
            print(f'Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}')

        print('------------')

        # Check if the word has been completely guessed
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            return 
    
    # If out of guesses, reveal the word
    print(f'Sorry, you ran out of guesses. The word was {secretWord}.')

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print(hangman(secretWord))
