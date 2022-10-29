#################################################################################################
#This program takes your current age and output a message with your time left in days,weeks and month
##################################################################################################

age = input("what is your age?")
convert_age = int(age)
#This part converts the input age to days
days = (90 *  365) - (convert_age * 365)
weeks = (days // 7)
months = (weeks // 52)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
