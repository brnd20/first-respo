
condition = True
while condition:
    firstNum = int(input("FIRST NUMBER: "))
    secondNum = int(input("SECOND NUMBER: "))
    sum = firstNum + secondNum

    print("The sum of", firstNum, "and", secondNum, "is: ", sum)
    print()
    choice = input("Do you want to try again? type \"Y/y\" for yes and \"N/n\" for no: ")

    if choice == "y" or choice == "Y":
        condition = True
    elif choice == "n" or choice == "N":
        print("THANK YOU")
        condition = False

        