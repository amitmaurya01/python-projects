import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly choose something from the word
    # below while loop to make sure word doesn't include '-' or ' '
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what user has already guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a','b','cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ',
              ' '.join(used_letters))

        # what current word is (i.e. W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print("\nThat is not a valid letter.")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You have no more lives')
        print(f"The word was {word}.")
    else:
        print(f'Congrats you have guessed the word : {word}.')


hangman()
