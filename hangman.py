import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word 
    used_letters = set() # what the user has guessed
    alphabet = string.ascii_uppercase
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        #letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'

        print(f"You have {lives} lives left and used these letters: " , " ".join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"{user_letter} is not in the word!")
        elif user_letter in used_letters:
            print(f"You have already used '{user_letter}'. Try another one.")
        else:
            print(f"Invalid character. Please try again.")
    #gets here when len(word_letters == 0) or lives == 0
    if lives == 0:
        print(f"You died. The word was: {word}")
    else:
        print(f"You guessed the word: {word}!!")

print(hangman())