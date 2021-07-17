import random
from words import words
import string
def get_valid_words(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:            # filtering bad characters
        word= random.choice(words)
    return word                             


def hint_word(word):     #giving Hints to player
    hint=''
    hidden=True
    for i in range(len(word)):
        if hidden:
            hint+=word[i]
        else:
            hint+='-'
        hidden=not hidden
    return hint


def guessing_game():          #game begins
    word=get_valid_words(words).upper()
    
    hint=hint_word(word)
    
    print(f'Hint for word is {hint} ')

    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
     
    while len(word_letters) > 0 :
        print('you have used these letters ',' '.join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word ]
        print('Current Word ',' '.join(word_list))

        user_letter=input("Guess a Letter ").upper()
        if user_letter in alphabet - used_letters:
           used_letters.add(user_letter)
           if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that word,Keep Guessing New ones ')
        else:
            print('You hane entered an Invalid character ')

name=input("Enter Your Name  ")
print(f'welcome,{name}')
guessing_game()
