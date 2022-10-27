#This code is to count the number of characters in a string
from ctypes.wintypes import PINT


print(len("This is the begining of string manipulation"))
print("this is a charcter indexikng"[0])

#('This is a new line for another code try')
num_char = len(input('what is your name:::'))

#The function str() converts the integer datatype to string
new_num_char = str(num_char)
print("Your name is " + new_num_char + " characters.")
print(type(num_char))



