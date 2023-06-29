# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
from random import randint

lucky = randint(0, len(names) - 1)

print(f'{names[lucky]} is going to buy the meal today!')

# print(f'{names[randint(0, len(names) - 1)]} is going to buy the meal today!')