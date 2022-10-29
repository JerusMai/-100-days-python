###THIS PROGRAM CHECK IF AN INPUT FROM A USER IS EVEN OR ODD, THIS IS CARRED OUT USING THE MODULOS OPERATOR###
###Even numbers are numbers can be divided by 2::: Odd numbers are numbers that cannot be divided by 2####
num = input("Enter a number:")
num_int = int(num)
### The if condition checks for if the condition is true or false.
if num_int % 2 == 0 :
    print("The number is even")
else:
    print("The number is odd")
