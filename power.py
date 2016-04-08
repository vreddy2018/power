# def power(originalBase, exponent):
# 	count = 0
# 	notconverted = True
# 	base = 1
# 	while notconverted == True:
# 		try:
# 			originalBase = float(originalBase)
# 			exponent = int(exponent)
# 			
# 		except ValueError:
# 			print('Sorry not a valid number. Run again.')
# 			quit()
# 		else: 
# 			notconverted = False
# 			
# 	while count < exponent:
# 		base = base * originalBase
# 		count += 1
# 		
# 	return base
#  
#  
# originalBase = raw_input("Enter a base (can be decimal or negative): ")
# exponent = raw_input("Enter an exponent (must be an integer): ")



	

def power_recursive(base, exponent):
	
	if exponent == 0:
		return 1

	output = base * power_recursive(base, exponent - 1)

	return output
	


def int_input(prompt):
	answer = raw_input(prompt)
	
	try:
		return int(answer)
	except ValueError:
		return (int_input("That wasn't a number. Try again."))
	
	
#test cases

print(power_recursive(5, 0))
print(power_recursive(2, 6))
print(power_recursive(4, 3))
print(power_recursive(8, 3))
print(power_recursive(0, 3))


#main program


userBase = int_input("Tell me a base: ")
userExponent = int_input("Tell me a Exponent: ")


print(power_recursive(userBase,userExponent))