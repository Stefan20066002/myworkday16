#Slot machine
import random
import time

print("╔═╗───╔╗─────────╔╗╔╗")
print("║═╬╗╔═╣╚╗╔══╦═╗╔═╣╚╬╬═╦╦═╗")
print("╠═║╚╣╬║╔╣║║║║╬╚╣═╣║║║║║║╩╣")
print("╚═╩═╩═╩═╝╚╩╩╩══╩═╩╩╩╩╩═╩═╝")


total = []
print("┏━━┓" * 10)
print("-" * 40)
def moni():
    try:
        global money
        money = int(input("Please enter the ammount of money: "))
    except ValueError:
        print("Please use only numbers.")
        moni()
    finally:
        total.append(money)
        print(f"You placed {money} $ in the slot machine: ")
        print("-" * 40)
        print("┗━━┛" * 10)
    
moni()

#"$","#","&",
Slot_options = {"@":"@","*":"*","$":"$"}
s = list(Slot_options)


print ("The game starts in ")

for x in range (5,0,-1):
    print (x)
    time.sleep (1)
print("┏━━┓" * 10)

for l_1_AA in random.choices(s[1]):
    for l_1_A in random.choices(s):
        for l_2_B in random.choices(s):
            for l_3_C in random.choices(s):
                print("")
for l1_1_A in random.choices(s):
    for l1_2_B in random.choices(s):
        for l1_3_C in random.choices(s):
           print("")
            
for l2_1_A in random.choices(s):
    for l2_2_B in random.choices(s):
        for l2_3_C in random.choices(s):
            print("")
    
slot_machine_border = {"z":"|"}
for key, value in slot_machine_border.items():
    print (f"{value} {l_1_A} {value} {l_2_B} {value} {l_3_C} {value}")
    print ("-" * 13)
    print (f"{value} {l1_1_A} {value} {l1_2_B} {value} {l1_3_C} {value}")
    print ("-" * 13)
    print (f"{value} {l2_1_A} {value} {l2_2_B} {value} {l2_3_C} {value}")
    print("")
    print("")
    print("")
print("┗━━┛" * 10)    
    


if l1_1_A == l1_2_B == l1_3_C:
    print ("{{{ 3x win }}}")
    calcul = money * 7
    print ("-" * 20)
    print ("")
    print (f"Your total income is {calcul} $")
    print("See you next time")
elif l1_1_A == l1_2_B or l1_2_B == l1_3_C:
    print ("{{{ 2x win }}}")
    calcul2 = money * 2
    print ("")
    print (f"Your total income is {calcul2} $")
    print("See you next time")
else:
    print("You lost all your money")
    print("See you next time")








        


