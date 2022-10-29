height = float(input("What is your height:::"))
if height >= 120:
    print("Can ride")
    age = int(input("Enter Your age:::"))
    if age < 12:
        strg = input("Do you want a photo?:::Ans yes or no:::")
        if strg == "yes":
            print("pay $8")
        else:
            print("Pay $5")
    
    elif age >= 12 and age <=17:
        strg = input("Do you want a photo?:::Ans yes or no:::")
        if strg == "yes":
            print("pay $10")
        else:
            print("pay $7")

    elif age >=18:
        strg = input("Do you want a photo?:::Ans yes or no:::")
        if strg == "yes":
            print("Pay $15")
        else:
            print("Pay $12")
else:
    print("Can't ride")