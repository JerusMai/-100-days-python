###THIS PROGRAM CALCULATE AND SHARE A BILL AMONG A NUMBER OF PERSONS AND ADD A PERCENTAGE OF TIP TO THE TOTAL AMOUNT###
print(" Welcome To The Tip Calculator")
bill = input("what is the total bill $")
#convert the string input into integer
int_bill = int(bill)
tip = input("What percentage tip wuold you like to give? 10, 12, or 15 ")
#convert the string input into integer
int_tip = int(tip)
mem = input("How many people are splitting the bill? ")
#convert the string input into integer
int_mem = int(mem)
#The entire expression of the program is followed by the code below
result = round((int_bill + ((int_tip/100) * int_bill)) / int_mem, 2)
print(f"Each person should pay:{result}")