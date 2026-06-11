weight = float(input("enter your weight (kg): "))
height = float(input("enter your height (cm): "))
height_m = height / 100  # სიმაღლის გადაყვანა მეტრებში
bmi = weight / (height_m ** 2)
if bmi < 19:
    print("BMI: {:.2f} - Underweight".format(bmi))
elif 19 <= bmi <= 25:
    print("BMI: {:.2f} - Normalweight".format(bmi))
else:
    print("BMI: {:.2f} - Overweight".format(bmi))