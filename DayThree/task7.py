print("Welcome to the Love Calculator")
name1 = input("what is your name?:::\n")
name2 = input("what is their name?:::\n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

for_name1_t = name1.count("t")
for_name2_t = name2.count("t")

if "true" in lower_name1 or lower_name2 :
    _t = lower_name1.count("t") + lower_name2.count("t")
    _r = lower_name1.count("r") + lower_name2.count("r")
    _u = lower_name1.count("u") + lower_name2.count("u")
    _e = lower_name1.count("e") + lower_name2.count("e")
    for_true = _t + _r + _u + _e
    #print(for_true)
if "love" in lower_name1 or lower_name2 :
    _l = lower_name1.count("l") + lower_name2.count("l")
    _o = lower_name1.count("o") + lower_name2.count("o")
    _v = lower_name1.count("v") + lower_name2.count("v")
    _e = lower_name1.count("e") + lower_name2.count("e")
    for_love = _l + _o + _v + _e
    print(f" Your score is {for_true}{for_love}, You are alright together")

if for_true >=1 or for_love == 0:
    print(f" Your score is {for_true}{for_love}, You are alright together")
elif for_true <=9 or for_love == 0:
    print(f"Your is {for_true}{for_love}, you go together like coke and mentos")
elif for_true ==4 or for_love<= 9:
    print(f"Your score is{for_true}{for_love}, you alright together")
elif for_true == 5 or for_love == 0:
    print(f"Your score is {for_true}{for_love}, you alright together")
else:
    print(f"Score is {for_true}{for_love}")


    
