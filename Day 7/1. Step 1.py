# Step 1

word_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable callen choosen_word
import random
choosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
guess = input('Guess the letter ').lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in range(0, len(choosen_word)):
    if guess == choosen_word[i]:
        print('Right')
    else:
        print('Wrong')


