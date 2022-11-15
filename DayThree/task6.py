###This program is an automatic pizza program###
################################################

#Small pizza $15
#mediun pizza $20
#Large pizza $25

#Pepperoni for small Pizza: +$2
#Pepperoni for medium and large Pizza: +$3
#Extra cheese for a size pizza: +$1
small_size = 15
medium_size = 20
large_size = 25
pepperoni_small = 2
pepperoni_med_large = 3
extra_cheese = 1
print("Welcome to python Pizza Deliveries")
size = input("what size pizza do you want? S, M, L:::")
add_pep = input("Do you want pepperoni? Y or N:::")
extra_chs = input("Do you want extra cheese? Y or N:::")
if size == "S":
    if add_pep == "Y":
        if extra_chs == "Y":
            print(f"Your bill is:::${small_size + pepperoni_small + extra_cheese}")
        else:
            print(f"Your Bill is:::${small_size + pepperoni_small}")
    else:
        print(f"Your Bill is:::${small_size}")
######################################################################################
######################################################################################
if size == "M":
    if add_pep == "Y":
        if extra_chs == "Y":
            print(f"Your bill is:::${medium_size + pepperoni_med_large + extra_cheese}")
        else:
            print(f"Your Bill is:::${medium_size + pepperoni_med_large}")
    else:
        print(f"Your Bill is:::${medium_size}")
##########################################################################################
##########################################################################################
if size == "L":
    if add_pep == "Y":
        if extra_chs == "Y":
            print(f"Your bill is:::${small_size + pepperoni_med_large + extra_cheese}")
        else:
            print(f"Your Bill is:::${small_size + pepperoni_med_large}")
    else:
        print(f"Your Bill is:::${large_size}")