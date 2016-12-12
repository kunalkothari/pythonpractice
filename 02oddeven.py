try: 
	num = int(input("Enter a number to find if it is odd or even: "))
	if num % 2 == 0:
		print(str(num) + " is an even number!")	
	else:
		print(str(num) + " is a odd number!")
except ValueError:
	print("Please enter a numeric value")


