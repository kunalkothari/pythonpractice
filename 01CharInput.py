from datetime import datetime
name = input("Please enter your name: ")
age = int(input("Enter your age: "))
currentyear = datetime.today().year
yearwhenhundred = currentyear - age + 100
print (name + " You will be a hundered year old in the year " + str(yearwhenhundred) + " !!" )