# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / (height ** 2))
if  BMI <= 18.5:
    print(f'Your BMI is {BMI}, you are underweight.')
elif 25 >= BMI >= 18.5:
    print(f'Your BMI is {BMI}, you have a normal weight.')
elif 30 >= BMI >= 25:
    print(f'Your BMI is {BMI}, you are slightly overweight.')
elif 35 >= BMI >= 30:
    print(f'Your BMI is {BMI}, you are obese.')
elif 35 <= BMI :
    print(f'Your BMI is {BMI}, you are clinically obese.')