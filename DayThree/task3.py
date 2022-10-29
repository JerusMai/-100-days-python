##################################################################
### THIS PROGRAM WORKS OUT WEATHER IF A GIVEN YEAR IS LEAP YEAR###
##################################################################
_YEAR = int(input("which year do you want to check:::"))
if _YEAR % 4 == 0:
    print(f"Year {_YEAR} is a leap year")
    if _YEAR % 100 != 0 :
        print(f"Year {_YEAR} is a leap")
        if _YEAR % 400 == 0:
            print(f"Year {_YEAR} is a leap year")
else:
    print(f"Year {_YEAR} is not a leap year!")    
