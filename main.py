import os
import time

print("Welcome to the ultimate Python girlfriend simulator")
print("Choose a option from the menu you can also type h so you know how everything works")
print("1-Start Simulator")
print("2-Waifu mode")
print("3-exit")
print("h-help")
print("Choose a option: ")
usrinp = input()


if usrinp == "1":
    os.system('cls')
    print("Starting simulator")
    time.sleep(3)
    print("So in order to experience the ultimate girlfriend experience we need to set up your code girlfriend")
    print("Choose a hair color:")
    print("1)Brunette")
    print("2)Blonde")
    print("3)Redhead")
    print("Select a color:")
    himp = input()
    if himp == "1":
        os.system('cls')
        hclr = "Brunette"
    elif himp == "2":
        os.system('cls')
        hclr = "Blonde"
    elif himp == "3":
        os.system('cls')
        hclr = "Redhead"
    
    print("You selected " + hclr)

    time.sleep(2)
    os.system('cls')
    print ("Choose your body type now:")
    print("1)Flat")
    print("2)Curvy")
    print("3)Athletic")
    print('4)Chubby')
    bimp = input()

    if bimp == "1":
        os.system('cls')
        btyp = "Flat"

    elif bimp == "2":
        os.system('cls')
        btyp = "Curvy"

    elif bimp == "3":
        os.system('cls')
        btyp = "Athletic"
    
    elif bimp == "4":
        os.system('cls')
        btyp = "Chubby"
    
    print("You chose " + btyp)



elif usrinp == "2":
    print("Hi sempai w-w-welcome to the ultimate Python girlfriend simulator")
    print("Pwease choose a option sempai if you are confused pwease press h for help")
    print("1-Swart the simulator uwu")
    print("2-Regular mode")
    print("3-exit")
    print("h-help")
    print("Choose a option uwu: ")  
    uwuput = input()
    if uwuput == "1":
        print("Starting the experience sempai")

elif usrinp == "3":
    os.system('cls')
    print("See you next time in this down bad app")
    quit()
    

else:
    print("Error please rerun the script")
    quit()
