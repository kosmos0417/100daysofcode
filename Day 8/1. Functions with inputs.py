# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print('Hello')
    name = input("What's your name? ")
    print(f'Welcome, {name}')

def greet_with_name(name):
    print(f'Hello, {name}')
    print(f'How is the weather today {name}')

def greeting_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet()
greet_with_name('Amir')
greeting_with('Amirolimkhon', 'Barcelona')

