# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height = float(height)
weight = float(weight)
BMI = weight / height ** 2
print("Your BMI is " + str(int(BMI)))

#extra que eu fiz

if BMI < 18.5:
    print("You're underweight")
elif BMI > 18.5 and BMI < 24.9:
    print("You're in normal weight")
elif BMI > 25 and BMI < 29.9:
    print("You're overweight")
elif BMI > 30 and BMI < 30.4:
    print("You're obese")
elif BMI > 35:
    print("You're extremely obese")
