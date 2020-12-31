x = 1
for x in range (1,101):
	if(x%3 == 0)and(x%5 == 0):
		print("FizzBuzz \r")
		continue
	elif x%3==0:
		print("Fizz \r")
		continue
	elif x%5==0:
		print("Buzz \r")
		continue
	print(str(x) + "\r")

