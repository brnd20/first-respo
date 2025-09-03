while True:
    name = input("NAME: ")
    if name.replace(" ","").isalpha():
        name = name.title()
        break
    else: 
         print("INVALID INPUT, YOU CAN ONLY TYPE LETTERS!!!")

print()
print("WHAT OFFICE ARE YOU IN?")
print("[1]IT")
print("[2]ACCT")
print("[3]HR")

while True:
    choice = input("TYPE THE NUMBER OF YOUR OFFICE: ")
    if choice.isdigit() and choice in {"1", "2", "3"}:
        choice = int(choice)
        break
    else:
        print("INVALID INPUT, PLEASE ENTER 1, 2, OR 3!")

if choice == 1:
    office = "IT"
elif choice == 2:
    office = "ACCT"
elif choice == 3:
    office = "HR"

print()

while True:
    years = input("NUMBER OF YEARS IN SERVICE: ")
    if years.isdigit() and len(years) <=  3:
        years = int(years)
        break
    else:
         print("INVALID INPUT, YOU CAN ONLY TYPE NUMBERS AND THE INPUT SHOULD HAVE 13 NUMBERS!!!")


if office == "IT":
    if years >= 10:
        bonus = 10000
    else:
        bonus = 5000
elif office == "ACCT":
    if years >= 10:
        bonus = 12000
    else:
        bonus = 6000
elif office == "HR":
    if years >= 10:
        bonus = 15000
    else:
        bonus = 7500


print()
print("=====INFORMATION=====")
print("NAME: "+name)
print("OFFICE: "+office)
print("BONUS:", bonus)