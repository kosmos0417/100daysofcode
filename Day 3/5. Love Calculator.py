# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# true love
t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e =  name1.count('e') + name2.count('e')

true = str(t + r + u + e)

l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')
e = name1.count('e') + name2.count('e')

love = str(l + o + v + e)

final = int(true + love)
if final <  10 or final > 90:
    print(f'Your score is {final}, you go together like coke and mentos.')
elif 40 <=final <= 50 :
    print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}.")