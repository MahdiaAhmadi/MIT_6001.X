# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    
  
    total_score = 0

    for chars in word:
        total_score +=SCRABBLE_LETTER_VALUES[chars]


    total_score *= len(word)

    if len(word)==n:
        total_score +=50

    return total_score

   

print(getWordScore('weed',4))#32


    

    









#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    new_hand = hand.copy()
    for chars in word:
        if chars in new_hand:
           new_hand [chars] -= 1

           if new_hand[chars] == 0:
              del new_hand[chars]
    
    return new_hand   

print(updateHand({'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1},'quail')) # return l m  


    



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    if word not in wordList:
        return False
    hand_copy= hand.copy()

    for char in word:
        if char in hand_copy and hand_copy[char]>0:
            hand_copy[char] -=1
        else: 
            return False
    return True
   
    
wordList = ['quail', 'cat', 'weed', 'waybill']
hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
print(isValidWord('quail', hand, wordList))  # Expected output: True
print(isValidWord('cat', hand, wordList))    #









#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    new_hand = hand.copy()
    total_length = 0  # Initialize the counter

    # Loop through each character in the new hand
    for chars in new_hand:
        # Check if the character has a count greater than 0
        if new_hand[chars] > 0:
            # Add the count to total_length
            total_length += new_hand[chars]
        # If the count is zero, continue to the next character
        elif new_hand[chars] == 0:
            continue
        else:
            return 0  # This case shouldn't occur, but it's here for safety

    return total_length

print(calculateHandlen({'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}))  # Expected output: 7
print(calculateHandlen({'a': 0, 'b': 0, 'c': 0}))   



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    total_score =0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
       print('Current Hand: ', end='')
       displayHand(hand)# Display the hand
       
          

       # Ask user for input
       word = input( 'Enter word, or a "." to indicate that you are finished: ')
       # If the input is a single period:
        
            # End the game (break out of the loop)
       if word == '.':
           print('Good bye! Total score: ', total_score, 'points')
           break
       # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)
       else:
           if not isValidWord(word,hand,wordList):
               print("Invalid word, please try again.")
               print() #blank line display

                # Otherwise (the word is valid):


                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
           else: 
               word_score= getWordScore(word,n)
               total_score +=word_score

               print('"{}" earned {} points. Total: {} points'.format(word,word_score,total_score))
               print()
               
               # Update the hand by removing used letters
               hand = updateHand(hand,word)
                
       if calculateHandlen(hand) ==0:
           print('Run out of letters. Total score: ',total_score,'points' )   
        
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

wordList = loadWords()
print(playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7))
    
     
#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand=None # Store the last hand for replay
    n=HAND_SIZE # Define HAND_SIZE (e.g., 7)

    while True:
        user_input=input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        
        if user_input == 'n':
            hand=dealHand(n) # Deal a new random hand
            playHand(hand,wordList,n)
        elif user_input =='r':
            if hand is None:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                playHand(hand,wordList,n)
        elif user_input == 'e':
            print('Thanks for playing! Goodbye! ')
            break

        else:
            print('Invalid command')
    
wordList = loadWords()
print(playGame(wordList))




#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
