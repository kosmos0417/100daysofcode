rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
from random import choice

user = input().lower()
comp = choice(['scissors', 'rock', 'paper'])
print(comp)
if user == 'rock':
    print(rock)
elif user == 'paper':
    print(paper)
elif user == 'scissors':
    print(scissors)

print()

if comp == 'rock':
    print(rock)
elif comp == 'paper':
    print(paper)
else:
    print(scissors)


if comp == user:
    print('Draw')

elif comp == 'scissors':
    if user == 'paper':
        print("You lose")
    if user == 'rock':
        print('You won!')

elif comp == 'rock':
    if user == 'paper':
        print('You won')
    elif user == 'scissors':
        print('You lose')

else:
    if user == 'scissors':
        print('You won')
    elif user == 'rock':
        print('You lose')
