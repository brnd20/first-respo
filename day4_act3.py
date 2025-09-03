
condition = True
wordList =[]
while condition:
    word = input("ENTER A WORD: ")
    wordList.append(word)
    
    print()

    choice = input("Do you want to try again? type \"Y/y\" for yes and \"N/n\" for no: ")

    if choice == "y" or choice == "Y":
        condition = True
    elif choice == "n" or choice == "N":
        print("THE STORED WORD ARE: ", wordList)
        print("THE NUMBER OF WORDS STORED IS: ", len(wordList))
        print("THANK YOU")
        condition = False
