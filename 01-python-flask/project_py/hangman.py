# import random
# # import nltk
# import string
# from words import words
# from hangman_visuals import lives_visual_dict
# # nltk.download('words')
# # from nltk.corpus import words
# word_list = words.words()#randomly chooses something from the list
# def get_valid_word(word_list):
#     word=random.choice(word_list)
#     while '-'in word or ' ' in word:
#         word=random.choice(word_list)
    
#     return word.upper()

# def hangman():
#     word=get_valid_word(words)
#     word_letters=set(word) #letters in the word
#     alphabets=set(string.ascii_uppercase)
#     used_letters=set()  #what the user has guessed


#     lives=7
#     # getting user input 
#     while len(word_letters)>0:
#         # letter used in the game
#         # used ' '.join() to join the word into the list 
#         print(f"You have {lives} & You have used these letters:{' '.join(used_letters)}")
        
#         guess_word_list=[letter if  letter in used_letters else '-' for letter in words]
#         print(f"Guess word:{' '.join(guess_word_list)}")

#         user_letter=input("Guess a letter : ").upper()
#         if user_letter in alphabets - used_letters:
#             used_letters.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#                 print('')

#             else:
#                 lives=lives-1
#                 print(f"You letter {user_letter} is not in the word.")
        
#         elif user_letter in user_letter:
#             print("you have already used this character .Please try again")
#         else:
#             print("Invalid Character.Please try Again")
#     if lives==0:
#         print(lives_visual_dict[lives])
#         print(f"You died ,sorry the word was : {word}")
#     else:
#         print(f"Ya! You guessed the word {word} !! Enjoy your game")
    
# if __name__=="__main__":
#     hangman()

import random
import string
from words_file_1 import words
# print(words)
from hangman_visuals import lives_visual_dict

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    word = get_valid_word(words)  # Corrected this to use word_list
    word_letters = set(word)  # Letters in the word
    alphabets = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed

    lives = 7

    # Getting user input 
    while len(word_letters) > 0 and lives > 0:  # Game continues until the word is guessed or lives run out
        # Letters used in the game
        print(f"\nYou have {lives} lives left and you have used these letters: {' '.join(used_letters)}")
        
        # Show current guess with dashes for missing letters
        guess_word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"Guess word: {' '.join(guess_word_list)}")

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"\nYour letter {user_letter} is not in the word.")
                print(lives_visual_dict[lives])

        elif user_letter in used_letters:
            print("\nYou have already used this letter. Please try again.")
        else:
            print("\nInvalid character. Please try again.")

    # End of game
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"Sorry, you died. The word was: {word}")
    else:
        print(f"Yay! You guessed the word {word} !!")

if __name__ == "__main__":
    hangman()