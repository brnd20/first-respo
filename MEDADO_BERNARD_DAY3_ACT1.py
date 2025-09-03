while True:
    name = input("NAME: ")
    if name.replace(" ","").isalpha():
        name = name.title()
        break
    else: 
         print("INVALID INPUT, YOU CAN ONLY TYPE LETTERS!!!")


while True:
    math = input("MATH GRADE: ")
    if math.isdigit() and len(math) <=  2:
        math = int(math)
        break
    else:
         print("INVALID INPUT, YOU CAN ONLY TYPE NUMBERS AND THE INPUT SHOULD HAVE 13 NUMBERS!!!")


while True:

    science = input("SCIENCE GRADE: ")
    if science.isdigit() and len(science) <=  2:
        science = int(science)
        break
    else:
         print("INVALID INPUT, YOU CAN ONLY TYPE NUMBERS AND THE INPUT SHOULD HAVE 13 NUMBERS!!!")



while True:
    english = input("ENGLISH GRADE: ")
    if english.isdigit() and len(english) <=  2:
        english = int(english)
        break
    else:
         print("INVALID INPUT, YOU CAN ONLY TYPE NUMBERS AND THE INPUT SHOULD HAVE 13 NUMBERS!!!")
       

average = (math + science + english) / 3
average = float(average)

if average < 75:
    status = "FAILED"
else:
    status = "PASSED"

print()
print("=====INFORMATION=====")
print("NAME: "+name)
print("MATH GRADE: ",math)
print("SCIENCE GRADE: ",science)
print("ENGLISH GRADE: ",english)
print("AVERAGE: ", average)
print("STATUS: ",status)
