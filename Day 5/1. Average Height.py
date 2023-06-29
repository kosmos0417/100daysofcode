# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
all = 0
for i in range(len(student_heights)):
    all += student_heights[i - 1]
    i += 1
print(round(all / i))