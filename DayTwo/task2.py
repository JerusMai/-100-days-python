####################################################################################
#This program is to calculate the Body Mass index(BMI) from a users weight and height
#####################################################################################

height = input("Enter your height in m:::")
weight = input("Enter your Weight in kg:::")
bmi = float(weight) / float(height**2)

print("Your BMI :::", round(bmi))
