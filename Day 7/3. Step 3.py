# Step 3

import random
word_list = ["ardvark", "baboon", "camel"]
choosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {choosen_word}.')

#Create blanks
display = []
for i in range(0, len(choosen_word)):
    display.append('_')

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while display != list(choosen_word):
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if guess == letter:
            display[position] = guess

    print(*display)
