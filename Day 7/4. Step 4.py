# Step 4

import random


end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
choosen_word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {choosen_word}.')

#Create blanks
display = []
for i in range(0, len(choosen_word)):
    display.append('_')


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(*display)

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in choosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print('You lose')

    # Join all the elements in the list and turn it into a String.
    # print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.