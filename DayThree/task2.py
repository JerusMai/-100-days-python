### THIS PROGRAM INTERPRETES THE BODY MASS INDEX (BMI) BASED ON A USERS WEIGHT AND HEIGHT###
height = float(input("Enter your height in m:::"))
weight = float(input("Enter your weight in kg:::"))
bmi = round(weight / (height**2))

###This condition checks for the relative value of the BMI###
if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight")
elif bmi >= 18 and bmi < 25:
    print(f"Your bmi is {bmi}, You have a normal weight")
elif bmi > 25 and bmi < 30:
    print(f"Your bmi is {bmi}, You are overweight")
else:
    print(f"Your bmi is {bmi}, You are clincally obese")
